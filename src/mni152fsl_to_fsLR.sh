# This script will convert a decoder volume from MNI152FSL 2mm into fsLR 91k grayordinate space.

# Standard templates for 91282 space grayordinates are available from
# https://github.com/Washington-University/HCPpipelines/tree/master/global/templates/91282_Greyordinates


# HCP Template files are required.
HCP_TEMPLATE_DIR=/data/decoders/HCP_Templates
for TEMPLATE_FILE in "91282_Greyordinates.dscalar.nii" "Atlas_ROIs.2.nii.gz" "L.atlasroi.32k_fs_LR.shape.gii" "R.atlasroi.32k_fs_LR.shape.gii"; do
  if [[ ! -f "${HCP_TEMPLATE_DIR}/${TEMPLATE_FILE}" ]]; then
    curl -o "${HCP_TEMPLATE_DIR}/${TEMPLATE_FILE}" \
    "https://raw.githubusercontent.com/Washington-University/HCPpipelines/master/global/templates/91282_Greyordinates/${TEMPLATE_FILE}"
  fi
done
for TEMPLATE_FILE in "MNI152_T1_2mm.nii.gz"; do
  if [[ ! -f "${HCP_TEMPLATE_DIR}/${TEMPLATE_FILE}" ]]; then
    curl -o "${HCP_TEMPLATE_DIR}/${TEMPLATE_FILE}" \
    "https://raw.githubusercontent.com/Washington-University/HCPpipelines/master/global/templates/${TEMPLATE_FILE}"
  fi
done

# The decoder must be in MNI152FSL (91x109x91, 2mm isotropic)
# The FSL supplied template has a few more rows of data in the neck,
# but appears identical to HCP's otherwise.
DECODER_FILE="$1"
if [[ ! -f "$DECODER_FILE" ]]; then
  echo "The decoder $DECODER_FILE does not exist."
  exit 1
fi
DECODER_FILENAME="${DECODER_FILE##*/}"
DECODER_PATH="${DECODER_FILE%/*}"
if [[ "$DECODER_FILE" == *.nii.gz ]]; then
  DECODER_STEM="${DECODER_FILENAME:0: -7}"
elif [[ "$DECODER_FILE" == *.*.gii ]]; then
  DECODER_STEM="${DECODER_FILENAME%.*}"
  DECODER_STEM="${DECODER_STEM%.*}"
else
  DECODER_STEM="${DECODER_FILENAME%.*}"
fi
# If a space was specified in the nifti volume, remove it for cifti
if [[ "${DECODER_STEM}" == *space-* ]]; then
  P0="${DECODER_STEM%_space-*}"
  P1="${DECODER_STEM#*_space-}"
  P2="${P1#*_}"
  DECODER_STEM="${P0}_${P2}"
fi

# Per Tim Coalson at https://groups.google.com/a/humanconnectome.org/g/hcp-users/c/cDmsGbP2V0Y/m/ttnyaEdlAAAJ
# this is the most straight-forward way to convert MNI152FSL to fsLR.
# First, convert cortical data to surface
OUTPUT_DIR="/data/decoders/space-fsLR"
# Map cortical voxels onto vertices in the cortical sheet
for HEMI in L R; do
  if [[ -f "${OUTPUT_DIR}/${DECODER_STEM}_${HEMI}.func.gii" ]]; then
    echo "Skipping ${OUTPUT_DIR}/${DECODER_STEM}_${HEMI}.func.gii; it already exists."
  else
  	echo "Building ${HEMI} hemisphere surface"
    wb_command -volume-to-surface-mapping \
      "${DECODER_FILE}" \
      "${HCP_TEMPLATE_DIR}/S1200.${HEMI}.midthickness_MSMAll.32k_fs_LR.surf.gii" \
      "${OUTPUT_DIR}/${DECODER_STEM}_${HEMI}.func.gii" \
      -ribbon-constrained \
      "${HCP_TEMPLATE_DIR}/S1200.${HEMI}.midthickness_MSMAll.32k_fs_LR.surf.gii" \
      "${HCP_TEMPLATE_DIR}/S1200.${HEMI}.pial_MSMAll.32k_fs_LR.surf.gii"
    if [[ "$?" == "0" ]]; then
      echo "  built ${OUTPUT_DIR}/${DECODER_STEM}_${HEMI}.func.gii."
    fi
  fi
done
# Then, combine subcortical voxels with cortical sheets into one dscalar.nii file.
if [[ -f "${OUTPUT_DIR}/${DECODER_STEM}.dscalar.nii" ]]; then
  echo "Skipping ${OUTPUT_DIR}/${DECODER_STEM}.dscalar.nii; it already exists."
else
  echo "Combining voxels and vertices."
  wb_command -cifti-create-dense-from-template \
    "${HCP_TEMPLATE_DIR}/91282_Greyordinates.dscalar.nii" \
    "${OUTPUT_DIR}/${DECODER_STEM}.dscalar.nii" \
    -volume-all "${DECODER_FILE}" \
    -metric CORTEX_LEFT "${OUTPUT_DIR}/${DECODER_STEM}_L.func.gii" \
    -metric CORTEX_RIGHT "${OUTPUT_DIR}/${DECODER_STEM}_R.func.gii"
  if [[ "$?" == "0" ]]; then
    echo "  built ${OUTPUT_DIR}/${DECODER_STEM}.dscalar.gii."
    rm -v "${OUTPUT_DIR}/${DECODER_STEM}_L.func.gii"
    rm -v "${OUTPUT_DIR}/${DECODER_STEM}_R.func.gii"
  fi
fi

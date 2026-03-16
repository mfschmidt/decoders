import argparse
from datetime import datetime
from pathlib import Path
import subprocess
import nibabel as nib


decoders = {
    'adoration_occipital': {
        'name': 'Adoration',
        'filename': 'PLS_betas_Adoration.nii.gz',
        'citation': 'Kragel, et al., 2019',
        'title': 'Emotion schemas are embedded in the human visual system',
        'doi': 'https://doi.org/10.1126/sciadv.aaw4358',
        'coverage': 'occipital',
    },
    'aestheticappreciation_occipital': {
        'name': 'Aesthetic Appreciation',
        'filename': 'PLS_betas_Aesthetic Appreciation.nii.gz',
        'citation': 'Kragel, et al., 2019',
        'title': 'Emotion schemas are embedded in the human visual system',
        'doi': 'https://doi.org/10.1126/sciadv.aaw4358',
        'coverage': 'occipital',
    },
    'amusement_occipital': {
        'name': 'Amusement',
        'filename': 'PLS_betas_Amusement.nii.gz',
        'citation': 'Kragel, et al., 2019',
        'title': 'Emotion schemas are embedded in the human visual system',
        'doi': 'https://doi.org/10.1126/sciadv.aaw4358',
        'coverage': 'occipital',
    },
    'anxiety_occipital': {
        'name': 'Anxiety',
        'filename': 'PLS_betas_Anxiety.nii.gz',
        'citation': 'Kragel, et al., 2019',
        'title': 'Emotion schemas are embedded in the human visual system',
        'doi': 'https://doi.org/10.1126/sciadv.aaw4358',
        'coverage': 'occipital',
    },
    'awe_occipital': {
        'name': 'Awe',
        'filename': 'PLS_betas_Awe.nii.gz',
        'citation': 'Kragel, et al., 2019',
        'title': 'Emotion schemas are embedded in the human visual system',
        'doi': 'https://doi.org/10.1126/sciadv.aaw4358',
        'coverage': 'occipital',
    },
    'boredom_occipital': {
        'name': 'Boredom',
        'filename': 'PLS_betas_Boredom.nii.gz',
        'citation': 'Kragel, et al., 2019',
        'title': 'Emotion schemas are embedded in the human visual system',
        'doi': 'https://doi.org/10.1126/sciadv.aaw4358',
        'coverage': 'occipital',
    },
    'confusion_occipital': {
        'name': 'Confusion',
        'filename': 'PLS_betas_Confusion.nii.gz',
        'citation': 'Kragel, et al., 2019',
        'title': 'Emotion schemas are embedded in the human visual system',
        'doi': 'https://doi.org/10.1126/sciadv.aaw4358',
        'coverage': 'occipital',
    },
    'craving_wholebrain': {
        'name': 'Craving',
        'filename': 'craving_wmapN99_boot10K_02-May-2022.nii.gz',
        'citation': 'Koban, et al., 2022',
        'title': 'A neuromarker for drug and food craving distinguishes drug users from non-users',
        'doi': 'https://doi.org/10.1038/s41593-022-01228-w',
        'coverage': 'whole brain',
    },
    'craving_occipital': {
        'name': 'Craving',
        'filename': 'PLS_betas_Craving.nii.gz',
        'citation': 'Kragel, et al., 2019',
        'title': 'Emotion schemas are embedded in the human visual system',
        'doi': 'https://doi.org/10.1126/sciadv.aaw4358',
        'coverage': 'occipital',
    },
    'disgust_occipital': {
        'name': 'Disgust',
        'filename': 'PLS_betas_Disgust.nii.gz',
        'citation': 'Kragel, et al., 2019',
        'title': 'Emotion schemas are embedded in the human visual system',
        'doi': 'https://doi.org/10.1126/sciadv.aaw4358',
        'coverage': 'occipital',
    },
    'empathiccare_wholebrain': {
        'name': 'Empathic Care',
        'filename': 'Ashar_2017_empathic_care_marker.nii.gz',
        'citation': 'Ashar, et al., 2017',
        'title': 'Empathic care and distress: Predictive brain markers and dissociable brain systems',
        'doi': 'https://dx.doi.org/10.1016/j.neuron.2017.05.014',
        'coverage': 'whole brain',
    },
    'empathicdistress_wholebrain': {
        'name': 'Empathic Distress',
        'filename': 'Ashar_2017_empathic_distress_marker.nii.gz',
        'citation': 'Ashar, et al., 2017',
        'title': 'Empathic care and distress: Predictive brain markers and dissociable brain systems',
        'doi': 'https://dx.doi.org/10.1016/j.neuron.2017.05.014',
        'coverage': 'whole brain',
    },
    'empathicpain_occipital': {
        'name': 'Empathic Pain',
        'filename': 'PLS_betas_Empathic Pain.nii.gz',
        'citation': 'Kragel, et al., 2019',
        'title': 'Emotion schemas are embedded in the human visual system',
        'doi': 'https://doi.org/10.1126/sciadv.aaw4358',
        'coverage': 'occipital',
    },
    'entrancement_occipital': {
        'name': 'Entrancement',
        'filename': 'PLS_betas_Entrancement.nii.gz',
        'citation': 'Kragel, et al., 2019',
        'title': 'Emotion schemas are embedded in the human visual system',
        'doi': 'https://doi.org/10.1126/sciadv.aaw4358',
        'coverage': 'occipital',
    },
    'excitement_occipital': {
        'name': 'Excitement',
        'filename': 'PLS_betas_Excitement.nii.gz',
        'citation': 'Kragel, et al., 2019',
        'title': 'Emotion schemas are embedded in the human visual system',
        'doi': 'https://doi.org/10.1126/sciadv.aaw4358',
        'coverage': 'occipital',
    },
    'fear_wholebrain': {
        'name': 'Fear',
        'filename': 'VIFS.nii.gz',
        'citation': 'Zhou, et al., 2021',
        'title': 'A distributed fMRI-based signature for the subjective experience of fear',
        'doi': 'https://doi.org/10.1038/s41467-021-26977-3',
        'coverage': 'whole brain',
    },
    'fear_occipital': {
        'name': 'Fear',
        'filename': 'PLS_betas_Fear.nii.gz',
        'citation': 'Kragel, et al., 2019',
        'title': 'Emotion schemas are embedded in the human visual system',
        'doi': 'https://doi.org/10.1126/sciadv.aaw4358',
        'coverage': 'occipital',
    },
    'guilt_threshold': {
        'name': 'Guilt',
        'filename': 'Yu_guilt_SVM_sxpo_sxpx_EmotionForwardmask.nii.gz',
        'citation': 'Yu, et al., 2020',
        'title': 'Toward a brain-based biomarker of guilt',
        'doi': 'https://doi.org/10.1177/2633105520957638',
        'coverage': 'threshold',
    },
    'heatpain_threshold': {
        'name': 'Heat Pain',
        'filename': 'dpsp_hot_vs_others_weights_final.nii.gz',
        'citation': 'Woo, et al., 2016',
        'title': 'Quantifying cerebral contributions to pain beyond nociception',
        'doi': 'https://doi.org/10.1038/ncomms14211',
        'coverage': 'threshold',
    },
    'horror_occipital': {
        'name': 'Horror',
        'filename': 'PLS_betas_Horror.nii.gz',
        'citation': 'Kragel, et al., 2019',
        'title': 'Emotion schemas are embedded in the human visual system',
        'doi': 'https://doi.org/10.1126/sciadv.aaw4358',
        'coverage': 'occipital',
    },
    'interest_occipital': {
        'name': 'Interest',
        'filename': 'PLS_betas_Interest.nii.gz',
        'citation': 'Kragel, et al., 2019',
        'title': 'Emotion schemas are embedded in the human visual system',
        'doi': 'https://doi.org/10.1126/sciadv.aaw4358',
        'coverage': 'occipital',
    },
    'joy_occipital': {
        'name': 'Joy',
        'filename': 'PLS_betas_Joy.nii.gz',
        'citation': 'Kragel, et al., 2019',
        'title': 'Emotion schemas are embedded in the human visual system',
        'doi': 'https://doi.org/10.1126/sciadv.aaw4358',
        'coverage': 'occipital',
    },
    'negativeemotion_wholebrain': {
        'name': 'Negative Emotion',
        'filename': 'Rating_Weights_LOSO_2.nii.gz',
        'citation': 'Chang, et al., 2015',
        'title': 'A Sensitive and Specific Neural Signature for Picture-Induced Negative Affect',
        'doi': 'https://doi.org/10.1371/journal.pbio.1002180',
        'coverage': 'whole brain',
    },
    'rejection_threshold': {
        'name': 'Rejection',
        'filename': 'dpsp_rejection_vs_others_weights_final.nii.gz',
        'citation': 'Woo, et al., 2016',
        'title': 'Quantifying cerebral contributions to pain beyond nociception',
        'doi': 'https://doi.org/10.1038/ncomms14211',
        'coverage': 'threshold',
    },
    'reward_threshold': {
        'name': 'Reward',
        'filename': 'Reward_Signature_bootstrapped_0.5.nii.gz',
        'citation': 'Speer, et al., 2023',
        'title': 'A multivariate brain signature for reward',
        'doi': 'https://doi.org/10.1016/j.neuroimage.2023.119990',
        'coverage': 'threshold',
    },
    'romance_occipital': {
        'name': 'Romance',
        'filename': 'PLS_betas_Romance.nii.gz',
        'citation': 'Kragel, et al., 2019',
        'title': 'Emotion schemas are embedded in the human visual system',
        'doi': 'https://doi.org/10.1126/sciadv.aaw4358',
        'coverage': 'occipital',
    },
    'sadness_occipital': {
        'name': 'Sadness',
        'filename': 'PLS_betas_Sadness.nii.gz',
        'citation': 'Kragel, et al., 2019',
        'title': 'Emotion schemas are embedded in the human visual system',
        'doi': 'https://doi.org/10.1126/sciadv.aaw4358',
        'coverage': 'occipital',
    },
    'sexualdesire_occipital': {
        'name': 'Sexual Desire',
        'filename': 'PLS_betas_Sexual Desire.nii.gz',
        'citation': 'Kragel, et al., 2019',
        'title': 'Emotion schemas are embedded in the human visual system',
        'doi': 'https://doi.org/10.1126/sciadv.aaw4358',
        'coverage': 'occipital',
    },
    'surprise_occipital': {
        'name': 'Surprise',
        'filename': 'PLS_betas_Surprise.nii.gz',
        'citation': 'Kragel, et al., 2019',
        'title': 'Emotion schemas are embedded in the human visual system',
        'doi': 'https://doi.org/10.1126/sciadv.aaw4358',
        'coverage': 'occipital',
    },
    'threat_wholebrain': {
        'name': 'Threat',
        'filename': 'IE_ImEx_Acq_Threat_SVM_nothresh.nii.gz',
        'citation': 'Reddan, et al., 2018',
        'title': 'Attenuating neural threat expression with imagination',
        'doi': 'https://doi.org/10.1016/j.neuron.2018.10.047',
        'coverage': 'whole brain',
    },
    'emotionregulation_ventrofrontal': {
        'name': 'Emotion Regulation',
        'filename': 'schneck_emotion_regulation_vf.nii.gz',
        'citation': 'Schneck, et al., 2023',
        'title': 'The Temporal Dynamics of Emotion Regulation in Subjects With Major Depression and Healthy Control Subjects',
        'doi': 'https://doi.org/10.1016/j.biopsych.2022.09.002',
        'coverage': 'ventrofrontal',
    },
}


def get_dict_from_filename(filename):
    for decoder_name, decoder_dict in decoders.items():
        if decoder_dict['filename'] == filename:
            return decoder_dict
    return None


class App:

    def __init__(self):
        self.start_time = datetime.now()
        self.args = self.get_arguments()
        self.base_path = Path(self.args.data_base_path)
        self.orig_path = self.base_path / "original"


    @staticmethod
    def get_arguments():
        """ Parse command line arguments """

        parser = argparse.ArgumentParser(
            description="\n".join([
                "Go through decoder files and transform each decoder into template spaces.",
            ]),
        )
        parser.add_argument(
            "data_base_path",
            help="Path to subdirectories to contain transformed decoders",
        )
        parser.add_argument(
            "--verbose", action='store_true',
            help="set to True to trigger increasingly verbose output",
        )
        return parser.parse_args()

    def run(self):
        if self.args.verbose:
            print("Decoding everything in '{}'; starting at {}.".format(
                self.args.data_base_path, self.start_time
            ))

        for decoder_file in self.orig_path.glob("*.nii.gz"):
            decoder_dict = get_dict_from_filename(decoder_file.name)
            if decoder_dict is None:
                print(f"Could not find decoder file: {decoder_file.name}")
                continue
            print(f"Found decoder {decoder_file.name} '{decoder_dict['name']}'")
            orig_decoder_shape = nib.load(decoder_file).shape
            for space in [
                "MNI152FSL", "MNI152NLin6Asym", "MNI152NLin2009cAsym",
            ]:
                template_file = (
                    decoder_file.parent.parent /
                    f"template_space-{space}_t1w_brain.nii.gz"
                )
                out_path = decoder_file.parent.parent / f"space-{space}"
                out_filename = "_".join([
                    decoder_dict['name'].lower().replace(' ', ''),
                    decoder_dict['coverage'].lower().replace(' ', ''),
                    f"space-{space}",
                    "weights"
                ]) + ".nii.gz"
                p = subprocess.run([
                    "flirt",
                    "-in", str(decoder_file),
                    "-ref", str(template_file),
                    "-out", str(out_path / out_filename),
                    "-applyxfm", "-usesqform", "-interp", "trilinear"
                ])
                if p.returncode != 0:
                    print(f"  Error running FLIRT for {decoder_file.name}")
                else:
                    print(f"  FLIRT completed for {decoder_file.name}")
                    print(f"  {orig_decoder_shape} => "
                          f"{nib.load(out_path / out_filename).shape} "
                          f"({out_filename})")

def main():
    """ Entry point for the script """

    app = App()
    app.run()


if __name__ == "__main__":
    main()


## Step 1. Collect Decoders ##  

Numerous decoders have been downloaded
from the [Wager lab's github](https://github.com/canlab/Neuroimaging_Pattern_Masks)
to the local `original/` folder for use in this project. The supporting papers
are linked to their DOIs here.
We also included the PINES decoder and Noam Schneck's Emotion Regulation decoder since
we are familiar with them.

The first notebook in this project, `01_describe_decoders.ipynb`, builds the
glass brain representations of all the decoders listed below.

### Whole Brain Decoders ###   

- **Craving**
  `craving_wmapN99_boot10K_02-May-2022.nii.gz`
  from [Koban, et al., 2022. A neuromarker for drug and food craving distinguishes drug users from non-users](https://doi.org/10.1038/s41593-022-01228-w)
  - Paper in background
- **Empathic Care**
  `Ashar_2017_empathic_care_marker.nii.gz`
  from [Ashar, et al., 2017. Empathic care and distress: Predictive brain markers and dissociable brain systems](http://dx.doi.org/10.1016/j.neuron.2017.05.014)
  - Paper in background
- **Empathic Distress**
  `Ashar_2017_empathic_distress_marker.nii.gz`
  from [Ashar, et al., 2017. Empathic care and distress: Predictive brain markers and dissociable brain systems](http://dx.doi.org/10.1016/j.neuron.2017.05.014)
  - Paper in background
- **Fear** `VIFS.nii.gz`
  from [Zhou, et al., 2021. A distributed fMRI-based signature for the subjective experience of fear](https://doi.org/10.1038/s41467-021-26977-3)
  - In 67 participants, fear was elicited via images and rated on a 5-point scale.
- **Guilt** `Yu_guilt_SVM_sxpo_sxpx_EmotionForwardmask.nii.gz`
  from [Yu, et al., 2020. Toward a brain-based biomarker of guilt](https://doi.org/10.1177/2633105520957638)
  - Paper in background
- **Negative Emotion** `Rating_Weights_LOSO_2.nii.gz`
  from [Chang, et al., 2015. A Sensitive and Specific Neural Signature for Picture-Induced Negative Affect](https://doi.org/10.1371/journal.pbio.1002180)
  - Paper in background
- **Pain from heat** `dpsp_hot_vs_others_weights_final.nii.gz`
  from [Woo, et al., 2016. Quantifying cerebral contributions to pain beyond nociception](https://doi.org/10.1038/ncomms14211)
  - Paper in background
- **Rejection** `dpsp_rejection_vs_others_weights_final.nii.gz`
  from [Woo, et al., 2016. Quantifying cerebral contributions to pain beyond nociception](https://doi.org/10.1038/ncomms14211)
  - Paper in background
- **Reward** `Reward_Signature_bootstrapped_0.5.nii.gz`
  from [Speer, et al., 2023. A multivariate brain signature for reward](https://doi.org/10.1016/j.neuroimage.2023.119990)
  - Paper in background
- **Threat** `IE_ImEx_Acq_Threat_SVM_nothresh.nii.gz`
  from [Reddan, et al., 2018. Attenuating neural threat expression with imagination](https://doi.org/10.1016/j.neuron.2018.10.047)
  - Paper in background

![Whole Brain Decoder weights in glass brain representation](figures/glass_brain_whole_brain_decoders.png "Whole Brain Decoders")

### Schneck's Ventral Frontal Decoder ###   

- **Emotion Regulation** `schneck_emotion_regulation_vf.nii.gz`
  from [Schneck, et al., 2023. The Temporal Dynamics of Emotion Regulation in Subjects With Major Depression and Healthy Control Subjects](https://doi.org/10.1016/j.biopsych.2022.09.002)

![Ventral Frontal Decoder weights in glass brain representation](figures/glass_brain_ventral_frontal_decoders.png "Ventral Frontal Decoders")

### Kragel's Occipital Decoders ###   

- **Adoration** `PLS_betas_Adoration.nii.gz`
  from [Kragel, et al., 2019. Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358)
- **Aesthetic Appreciation** `PLS_betas_Aesthetic Appreciation.nii.gz`
  from [Kragel, et al., 2019. Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358)
- **Amusement** `PLS_betas_Amusement.nii.gz`
  from [Kragel, et al., 2019. Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358)
- **Anxiety** `PLS_betas_Anxiety.nii.gz`
  from [Kragel, et al., 2019. Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358)
- **Awe** `PLS_betas_Awe.nii.gz`
  from [Kragel, et al., 2019. Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358)
- **Boredom** `PLS_betas_Boredom.nii.gz`
  from [Kragel, et al., 2019. Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358)
- **Confusion** `PLS_betas_Confusion.nii.gz`
  from [Kragel, et al., 2019. Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358)
- **Craving** `PLS_betas_Craving.nii.gz`
  from [Kragel, et al., 2019. Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358)
- **Disgust** `PLS_betas_Disgust.nii.gz`
  from [Kragel, et al., 2019. Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358)
- **Empathic Pain** `PLS_betas_Empathic Pain.nii.gz`
  from [Kragel, et al., 2019. Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358)
- **Entrancement** `PLS_betas_Entrancement.nii.gz`
  from [Kragel, et al., 2019. Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358)
- **Excitement** `PLS_betas_Excitement.nii.gz`
  from [Kragel, et al., 2019. Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358)
- **Fear** `PLS_betas_Fear.nii.gz`
  from [Kragel, et al., 2019. Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358)
- **Horror** `PLS_betas_Horror.nii.gz`
  from [Kragel, et al., 2019. Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358)
- **Interest** `PLS_betas_Interest.nii.gz`
  from [Kragel, et al., 2019. Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358)
- **Joy** `PLS_betas_Joy.nii.gz`
  from [Kragel, et al., 2019. Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358)
- **Romance** `PLS_betas_Romance.nii.gz`
  from [Kragel, et al., 2019. Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358)
- **Sadness** `PLS_betas_Sadness.nii.gz`
  from [Kragel, et al., 2019. Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358)
- **Sexual Desire** `PLS_betas_Sexual Desire.nii.gz`
  from [Kragel, et al., 2019. Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358)
- **Surprise** `PLS_betas_Surprise.nii.gz`
  from [Kragel, et al., 2019. Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358)

![Occipital Decoder weights in glass brain representation](figures/glass_brain_occipital_decoders.png "Occipital Decoders")

## Step 2. Apply and Validate Decoders ##  

### Does preprocessing change results? ###   

We have some data preprocessed with FSL, some with fMRIPrep 20.2.0,
and some with fMRIPrep 23.2.0. Some of these were decoded with 6
motion confounds, and some with 24 motion confounds plus a white matter
and CSF confound. Before continuing, we spot-checked one subject to
see whether these approaches resulted in similar decoder scores.

![Pre-processing differences don't affect decoder output much](figures/sub-U03280_ses-1280_task-mem_decoder-Rating_Weights_LOSO_2_lineplot.png "Negative Emotion decoded via multiple pre-processing choices")

### Are decoder scores in the same ranges? ###   

It would be convenient to have all decoders normalized to the same
range of values. But to do that, we need to check that they each have
a mean near zero so we don't remove any real measured decoder-matching
brain activity by setting it to zero. I think we would ideally do this
at the decoding stage, so the sum of all decoder weights would add up
to the same value or something. Here are some histograms of decoder
scores, from decoder weights as provided from the Wager lab github,
and BOLD data whose residuals were z-scored after regressing out motion
confounds.

![Distribution of scores for all decoders and all studies](figures/decoder_score_histograms.png "Decoder Score Histograms")

![Distribution of scores for all decoders in Conte 2 data](figures/decoder_score_histograms_conte_2_raw.png "Conte 2 Decoder Score Histograms")

![Distribution of scores for all decoders in Conte 1 data](figures/decoder_score_histograms_conte_1_raw.png "Conte 1 Decoder Score Histograms")

![Distribution of scores for all decoders in BPD Orig data](figures/decoder_score_histograms_bpd_orig_raw.png "BPD Orig Decoder Score Histograms")

![Distribution of scores for all decoders in BPD MNI data](figures/decoder_score_histograms_bpd_mni_raw.png "BPD MNI Decoder Score Histograms")

### Decoder relationships with negative memories and emotion regulation ###   

To assess decoder performance without biasing our hypotheses in BPD
data, we will first apply decoders to a separate study, also using
the autobiographical memory "distancing" task. Decoders will also
be applied to all BPD fMRI after validation. 

Decoder scores in each task of interest (TOI) will be collected
from the time 6 seconds into the task to 6 seconds past the task,
an HRF-shifted block design. As a preliminary validation study,
we will assess whether decoders
assessing negative emotions like fear, horror, sadness are higher in
"memory" trials than in "arrows" trials, and higher in
"immerse" trials than in "distance" trials. (Note:
there are no controls in the BPD study, and we won't yet look
at BPD data. These validations will simply help to frame our hypotheses
before starting actual analyses.)

#### Whole Brain Decoders \

![Craving Decoder scores](figures/decoder_scores_per_trial_craving.png "Craving")  

![Empathic Care Decoder scores](figures/decoder_scores_per_trial_empathic_care.png "Empathic Care")  

![Empathic Distress Decoder scores](figures/decoder_scores_per_trial_empathic_distress.png "Empathic Distress")  

![Fear Decoder scores](figures/decoder_scores_per_trial_fear.png "Fear")  

![Guilt Decoder scores](figures/decoder_scores_per_trial_guilt.png "Guilt")  

![Heat Pain Decoder scores](figures/decoder_scores_per_trial_heat_pain.png "Heat Pain")  

![Negative Emotion Decoder scores](figures/decoder_scores_per_trial_negative_emotion.png "Negative Emotion")  

![Rejection Decoder scores](figures/decoder_scores_per_trial_rejection.png "Rejection")  

![Reward Decoder scores](figures/decoder_scores_per_trial_reward.png "Reward")  

![Threat Decoder scores](figures/decoder_scores_per_trial_threat.png "Threat")  

#### Schneck's Emotion Regulation Decoder \

![Emotion Regulation Decoder scores](figures/decoder_scores_per_trial_emotion_regulation.png "Emotion Regulation")

#### Kragel Occipital Decoders \

![Adoration Decoder scores](figures/decoder_scores_per_trial_adoration.png "Adoration")  

![Aesthetic Appreciation Decoder scores](figures/decoder_scores_per_trial_aesthetic_appreciation.png "Aesthetic Appreciation")  

![Amusement Decoder scores](figures/decoder_scores_per_trial_amusement.png "Amusement")  

![Anxiety Decoder scores](figures/decoder_scores_per_trial_anxiety.png "Anxiety")  

![Awe Decoder scores](figures/decoder_scores_per_trial_awe.png "Awe")  

![Boredom Decoder scores](figures/decoder_scores_per_trial_boredom.png "Boredom")  

![Confusion Decoder scores](figures/decoder_scores_per_trial_confusion.png "Confusion")  

![Craving (alt) Decoder scores](figures/decoder_scores_per_trial_craving_alt.png "Craving (alt)")  

![Disgust Decoder scores](figures/decoder_scores_per_trial_disgust.png "Disgust")  

![Empathic Pain Decoder scores](figures/decoder_scores_per_trial_empathic_pain.png "Empathic Pain")  

![Entrancement Decoder scores](figures/decoder_scores_per_trial_entrancement.png "Entrancement")  

![Excitement Decoder scores](figures/decoder_scores_per_trial_excitement.png "Excitement")  

![Fear (alt) Decoder scores](figures/decoder_scores_per_trial_fear_alt.png "Fear (alt)")  

![Horror Decoder scores](figures/decoder_scores_per_trial_horror.png "Horror")  

![Interest Decoder scores](figures/decoder_scores_per_trial_interest.png "Interest")  

![Joy Decoder scores](figures/decoder_scores_per_trial_joy.png "Joy")  

![Romance Decoder scores](figures/decoder_scores_per_trial_romance.png "Romance")  

![Sadness Decoder scores](figures/decoder_scores_per_trial_sadness.png "Sadness")  

![Sexual Desire Decoder scores](figures/decoder_scores_per_trial_sexual_desire.png "Sexual Desire")  

![Surprise Decoder scores](figures/decoder_scores_per_trial_surprise.png "Surprise")  

### Decoder relationships split by instruction ###   

Above, plots for "memory" and "arrows" trials contain data for all trials.
Below, they are split into "memory" trials preceding "immerse" or "distance"
trials. They shouldn't differ because the participant doesn't know what the
instruction will be. The same is done for "arrows", but there may be a
hangover effect if the prior memory persists through the "arrows" task.
This is potentially interesting if distancing just temporarily holds off
the affective valence of the memory, which then intrudes when working
memory is busy with detecting arrow directions.

#### Whole Brain Decoders, split by instruction \

![Craving Decoder scores, by instruct](figures/decoder_scores_per_trial_craving_by-instruct.png "Craving")

![Empathic Care Decoder scores, by instruct](figures/decoder_scores_per_trial_empathic_care_by-instruct.png "Empathic Care")

![Empathic Distress Decoder scores, by instruct](figures/decoder_scores_per_trial_empathic_distress_by-instruct.png "Empathic Distress")

![Fear Decoder scores, by instruct](figures/decoder_scores_per_trial_fear_by-instruct.png "Fear")

![Guilt Decoder scores, by instruct](figures/decoder_scores_per_trial_guilt_by-instruct.png "Guilt")

![Heat Pain Decoder scores, by instruct](figures/decoder_scores_per_trial_heat_pain_by-instruct.png "Heat Pain")

![Negative Emotion Decoder scores, by instruct](figures/decoder_scores_per_trial_negative_emotion_by-instruct.png "Negative Emotion")

![Rejection Decoder scores, by instruct](figures/decoder_scores_per_trial_rejection_by-instruct.png "Rejection")

![Reward Decoder scores, by instruct](figures/decoder_scores_per_trial_reward_by-instruct.png "Reward")

![Threat Decoder scores, by instruct](figures/decoder_scores_per_trial_threat_by-instruct.png "Threat")

#### Schneck's Emotion Regulation Decoder, split by instruction \

![Emotion Regulation Decoder scores, by instruct](figures/decoder_scores_per_trial_emotion_regulation_by-instruct.png "Emotion Regulation")

#### Kragel Occipital Decoders, split by intruction \

![Adoration Decoder scores, by instruct](figures/decoder_scores_per_trial_adoration_by-instruct.png "Adoration")

![Aesthetic Appreciation Decoder scores, by instruct](figures/decoder_scores_per_trial_aesthetic_appreciation_by-instruct.png "Aesthetic Appreciation")

![Amusement Decoder scores, by instruct](figures/decoder_scores_per_trial_amusement_by-instruct.png "Amusement")

![Anxiety Decoder scores, by instruct](figures/decoder_scores_per_trial_anxiety_by-instruct.png "Anxiety")

![Awe Decoder scores, by instruct](figures/decoder_scores_per_trial_awe_by-instruct.png "Awe")

![Boredom Decoder scores, by instruct](figures/decoder_scores_per_trial_boredom_by-instruct.png "Boredom")

![Confusion Decoder scores, by instruct](figures/decoder_scores_per_trial_confusion_by-instruct.png "Confusion")

![Craving (alt) Decoder scores, by instruct](figures/decoder_scores_per_trial_craving_alt_by-instruct.png "Craving (alt)")

![Disgust Decoder scores, by instruct](figures/decoder_scores_per_trial_disgust_by-instruct.png "Disgust")

![Empathic Pain Decoder scores, by instruct](figures/decoder_scores_per_trial_empathic_pain_by-instruct.png "Empathic Pain")

![Entrancement Decoder scores, by instruct](figures/decoder_scores_per_trial_entrancement_by-instruct.png "Entrancement")

![Excitement Decoder scores, by instruct](figures/decoder_scores_per_trial_excitement_by-instruct.png "Excitement")

![Fear (alt) Decoder scores, by instruct](figures/decoder_scores_per_trial_fear_alt_by-instruct.png "Fear (alt)")

![Horror Decoder scores, by instruct](figures/decoder_scores_per_trial_horror_by-instruct.png "Horror")

![Interest Decoder scores, by instruct](figures/decoder_scores_per_trial_interest_by-instruct.png "Interest")

![Joy Decoder scores, by instruct](figures/decoder_scores_per_trial_joy_by-instruct.png "Joy")

![Romance Decoder scores, by instruct](figures/decoder_scores_per_trial_romance_by-instruct.png "Romance")

![Sadness Decoder scores, by instruct](figures/decoder_scores_per_trial_sadness_by-instruct.png "Sadness")

![Sexual Desire Decoder scores, by instruct](figures/decoder_scores_per_trial_sexual_desire_by-instruct.png "Sexual Desire")

![Surprise Decoder scores, by instruct](figures/decoder_scores_per_trial_surprise_by-instruct.png "Surprise")

## Step 2 B. Validate in BPD ##

See bruno:/data/nyspi/bpd/derivatives/feat_for_rsa_2024/code/README.md
for details about transforming and decoding BPD's feat-based data.

## Step 2 C. Check whether decoder outputs are correlated ##

We checked whether the time course of decoder outputs, concatenated
along subjects and their runs, were correlated with the same time
course of another decoder output. We found that no whole-brain decoder 
outputs were strongly correlated with any other. But the occipital
decoders had clusters of similarity.

### Selected whole brain decoder correlations: ###

![Conte 1 Decoder Correlations, immerse](figures/decoder_correlations_conte_1_selected_immerse.png)

![Conte 1 Decoder Correlations, distance](figures/decoder_correlations_conte_1_selected_distance.png)

![Conte 2 Decoder Correlations, immerse](figures/decoder_correlations_conte_2_selected_immerse.png)

![Conte 2 Decoder Correlations, distance](figures/decoder_correlations_conte_2_selected_distance.png)

![BPD Decoder Correlations, immerse](figures/decoder_correlations_bpd_mni_selected_immerse.png)

![BPD Decoder Correlations, distance](figures/decoder_correlations_bpd_mni_selected_distance.png)

### All decoder correlations: ###

![Conte 1 Decoder Correlations, immerse](figures/decoder_correlations_conte_1_all_immerse.png)

![Conte 1 Decoder Correlations, distance](figures/decoder_correlations_conte_1_all_distance.png)

![Conte 2 Decoder Correlations, immerse](figures/decoder_correlations_conte_2_all_immerse.png)

![Conte 2 Decoder Correlations, distance](figures/decoder_correlations_conte_2_all_distance.png)

![BPD Decoder Correlations, immerse](figures/decoder_correlations_bpd_mni_all_immerse.png)

![BPD Decoder Correlations, distance](figures/decoder_correlations_bpd_mni_all_distance.png)


----

Notes:

To save this README.md as a pdf,

```bash
pandoc README.md \
-V colorlinks=true -V linkcolor=blue -V urlcolor=blue -V toccolor=gray -V geometry:margin=1in \
-f markdown-implicit_figures \
-o "figures/Decoder Notes 2025-09-10.pdf"
```

The decoders in `original` were mostly downloaded from the Wager lab's github
repository. Emotion Regulation was created internally. They are all in the
same World space as FSL's MNI152 template, but with differing coverage and
voxel sizes. To allow for ease of decoding, each was transformed into several
common MRI spaces with `resample_orig_to_templates.py`.  -Mike Schmidt 2026-02-16

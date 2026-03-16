The decoders in `original` were mostly downloaded from the Wager lab's github
repository. Emotion Regulation was created internally. They are all in the
same World space as FSL's MNI152 template, but with differing coverage and
voxel sizes. To allow for ease of decoding, each was transformed into several
common MRI spaces with `resample_orig_to_templates.py`.

-Mike Schmidt 2026-02-16


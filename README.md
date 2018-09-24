# What this is

Experiments with ABM golf data.

# Setup 

Data must be in ../data.  Most scripts use ../data/0261/0261/026111501.ebs.edf

## MNE

# Source code

Frequent Domain Plotting - hit "-" several times when the file comes up; eventually only signal on the time sync will be shown

mne_view.py - shows proper EEG signals

Time Domain Plotting - important -- remove last 6 channels; also data already appears to be filtered so applying the filter on top of the data doesn't give good results
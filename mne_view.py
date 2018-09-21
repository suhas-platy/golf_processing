# plot eeg data

# derived from https://mne-tools.github.io/dev/tutorials/philosophy.html
# more things at https://martinos.org/mne/dev/auto_tutorials/plot_visualize_raw.html#sphx-glr-auto-tutorials-plot-visualize-raw-py

import os.path as op
import numpy as np

import mne

data_path = '..\\data\\0261\\0261\\'
file = '026111501.ebs.edf'
#file = '026111502.ebs.edf'
raw = mne.io.read_raw_edf(op.join(data_path, file),
                          preload=True)
# don't use this; this is from an MEG example
#raw.set_eeg_reference('average', projection=True)  # set EEG average reference

raw.plot(show_options=False, block=True, lowpass=40)
# show_options shows help on keyboard input; leave this as False
################################################################################
# IMPORTANT: click off on show "Average EEG reference" if it shows up
################################################################################
# block means block the program from continuing or not
# lowpass - TSIA
# order = [range(0,4)] (e.g.)
# clipping doesn't help much (transparent is esp. bad)

# no workey
#raw.plot( butterfly=True, group_by='position')
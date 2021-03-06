# plot eeg data

# In Ananconda Prompt (not Cygwin):
# conda activate golf 

# derived from https://mne-tools.github.io/dev/tutorials/philosophy.html
# more things at https://martinos.org/mne/dev/auto_tutorials/plot_visualize_raw.html#sphx-glr-auto-tutorials-plot-visualize-raw-py

import os.path as op
import numpy as np

import mne

import matplotlib.pyplot as plt
from xdf import load_xdf

# golf
GOLF = 1
data_path = '..\\data\\0261\\0261\\'
eeg_filename = '026111501.ebs.edf'
#eeg_filename = '026111502.ebs.edf'
marker_filename = '026111501_Markers.mrk'

# Kangaroos
GOLF = 0
data_path = '..\\data\\0001_0\\0001_0\\'
eeg_filename = '000100000.221017.141511.Signals.Raw.edf'
marker_filename = '000100000.221017.143353.Markers.mrk'

# TPI Alpha
GOLF = 0
data_path = '..\\data\\TPI Alpha Test July 2018\\TestData2\\'
eeg_filename = 'TestData2_flanker_arrows_2018-07-05_11-34-23_1.xdf'

data_path = '..\\data\\Giorgio 072118\\Giorgio 072118\\EEG Data\\'
eeg_filename = 'giorgio_phase3.xdf'

if ( GOLF ):
  raw = mne.io.read_raw_edf(op.join(data_path, eeg_filename), preload=True)
else:
  streams, header = load_xdf(op.join(data_path, eeg_filename), synchronize_clocks=False)
  print( streams[0]["time_stamps"] )
  fig, ax = plt.subplots()
  ax.plot(streams[0]["time_stamps"], streams[0]["time_series"])
  print( streams[0]["time_stamps"] )
  #ax.plot(streams[1]["time_stamps"], streams[1]["time_series"])
  fig.show()
  input()
  
print(raw.info) # 26 channels + 1 stimulus channel
print(raw.info['chs'][0]['loc']) # no location info

# set locations
montage = mne.channels.read_montage('standard_1020')
print(montage)

# don't use this; this is from an MEG example
# raw.set_eeg_reference('average', projection=True)  # set EEG average reference

raw.plot(show_options=False, block=True, lowpass=40)
# show_options shows help on keyboard input; leave this as False
################################################################################
# IMPORTANT: click off on show "Average EEG reference" if it shows up
################################################################################
# block means block the program from continuing or not
# lowpass - TSIA
# order = [range(0,4)] (e.g.)
# clipping doesn't help much (transparent is esp. bad)

# no workey; no position info
# raw.plot( butterfly=True, group_by='position')

# no workey; file format wrong
# events = mne.read_events(op.join(data_path, marker_filename))
# print( events )
# raw.plot(butterfly=True, events=events)

# no workey; no position info
# raw.plot_sensors(block=True, kind='3d', ch_type='eeg', ch_groups='position')
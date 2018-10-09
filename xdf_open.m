% open Flanker or Kicker data; Matlab has issues with the files

% Flanker
DATA_PATH = '..\\data\\TPI Alpha Test July 2018\\TestData2\\'
EEG_FNAME = 'TestData2_flanker_arrows_2018-07-05_11-34-23_1.xdf'
EEG_FNAME = 'TestData2_threecvt_2018-07-05_11-47-07_1.xdf'

% Kicker
DATA_PATH = '..\\data\\Giorgio 072118\\Giorgio 072118\\EEG Data\\'
EEG_FNAME = 'giorgio_phase3.xdf'

HANDLE_CLOCK_SYNCHRONIZATION = 'false'
HANDLE_CLOCK_RESETS = 'false'

[streams,fileheader] = load_xdf2( [DATA_PATH EEG_FNAME], 'HandleClockSynchronization', HANDLE_CLOCK_SYNCHRONIZATION, 'HandleClockResets', HANDLE_CLOCK_RESETS )
markers_filename = 'C:\Users\suhas\Desktop\prjs\golf_processing\data\ABM - Old Golf Data\NUGA Golfers\0261\0261\026111501_Markers.mrk_Events_EEGLAB.csv'
% this is optional
merged_markers_filename = 'C:\Users\suhas\Desktop\prjs\golf_processing\data\ABM - Old Golf Data\merged_markers\merged_markers\0261_Markers_merged.xlsx'
out_filename = 'C:\Users\suhas\Desktop\prjs\golf_processing\data\ABM - Old Golf Data\NUGA Golfers\0261\0261\026111501_Markers.mrk_Events_EEGLAB_simple.csv'
[events, header, ignore_events] = convert_events( markers_filename, out_filename, 'merged_markers_filename', merged_markers_filename )


markers_filename = 'C:\Users\suhas\Desktop\prjs\golf_processing\data\ABM - Old Golf Data\NUGA Golfers\0261\0261\026111502_Markers.mrk_Events_EEGLAB.csv'
% this is optional
merged_markers_filename = 'C:\Users\suhas\Desktop\prjs\golf_processing\data\ABM - Old Golf Data\merged_markers\merged_markers\0261_Markers_merged.xlsx'
out_filename = 'C:\Users\suhas\Desktop\prjs\golf_processing\data\ABM - Old Golf Data\NUGA Golfers\0261\0261\026111502_Markers.mrk_Events_EEGLAB_simple.csv'
[events, header, ignore_events] = convert_events( markers_filename, out_filename, 'merged_markers_filename', merged_markers_filename, 'verbose', false )

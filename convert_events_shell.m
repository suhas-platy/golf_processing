SUBJ = '026111'
SUBJ_SHORT = '0261'
SESS_START = 501
SESS_END = 510
PATH = 'C:\Users\suhas\Desktop\prjs\golf_processing\data\ABM - Old Golf Data\'

merged_markers_filename = [PATH 'merged_markers' filesep 'merged_markers' filesep...
                           SUBJ_SHORT '_Markers_merged.xlsx'];
disp( merged_markers_filename );

for i = SESS_START:SESS_END
   markers_filename = [PATH 'NUGA Golfers' filesep SUBJ_SHORT filesep SUBJ_SHORT filesep...
                       SUBJ num2str(i) '_Markers.mrk_Events_EEGLAB.csv'];
   disp( sprintf( 'markers_filename = %s', markers_filename ) );

   out_filename = [PATH 'NUGA Golfers' filesep SUBJ_SHORT filesep SUBJ_SHORT filesep...
                   SUBJ num2str(i) '_Markers.mrk_Events_EEGLAB_simple.csv'];
   [events, header, ignore_events] = convert_events( markers_filename, out_filename, 'merged_markers_filename', merged_markers_filename, 'verbose', false );
end

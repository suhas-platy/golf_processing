% @brief convert all event files into a simple format EEGLab can read

SUBJ_Z = [261:262];
SESS_START = 501;
SESS_END = 510;
PATH = 'C:\Users\suhas\Desktop\prjs\golf_processing\data\ABM - Old Golf Data\';

% 261 502: i
% 261 505: i then u

% 262 502: u
% 262 503: a...
% 262 505: u
% 262 506: u
% 262 510: a...


for subj = 1:size(SUBJ_Z,2)
   SUBJ_SHORT = ['0' num2str( SUBJ_Z(subj) )];
   SUBJ_LONG = ['0' num2str( SUBJ_Z(subj) ) '11']; 

   disp( sprintf( 'Subject: %s', SUBJ_SHORT ) );
   merged_markers_filename = [PATH 'merged_markers' filesep 'merged_markers' filesep...
                       SUBJ_SHORT '_Markers_merged.xlsx'];
   disp( sprintf( 'Merged markers file: %s', merged_markers_filename ) );

   for sess = SESS_START:SESS_END
      markers_filename = [PATH 'NUGA Golfers' filesep SUBJ_SHORT filesep...
                          SUBJ_LONG num2str(sess) '_Markers.mrk_Events_EEGLAB.csv'];
      disp( sprintf( 'Markers filename: %s', markers_filename ) );

      out_filename = [PATH 'NUGA Golfers' filesep SUBJ_SHORT filesep...
                      SUBJ_LONG num2str(sess) '_Markers.mrk_Events_EEGLAB_simple.csv'];
                  
      %[events, header, ignore_events] = convert_events( markers_filename, out_filename, 'merged_markers_filename', merged_markers_filename, 'verbose', false );
      
      [events, header, ignore_events] = convert_events_simple( markers_filename, out_filename, 'merged_markers_filename', merged_markers_filename, 'verbose', false );

   end
end
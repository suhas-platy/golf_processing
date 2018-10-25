% @brief make script to convert events files into something EEGLab can almost read (use convert_events_shell.m after this)

SUBJ_Z = [261:265];
SESS_START = 501;
SESS_END = 510;
PATH = 'C:\Users\suhas\Desktop\prjs\golf_processing\data\ABM - Old Golf Data\';
PATH = [PATH 'NUGA Golfers\'];

for subj = 1:size(SUBJ_Z,2)
   SUBJ_SHORT = ['0' num2str( SUBJ_Z(subj) )];
   SUBJ_LONG = ['0' num2str( SUBJ_Z(subj) ) '11']; 

   OUT_FILENAME = 'labx2eeglab_tmp.blab';
   OUT_FILENAME = [PATH SUBJ_SHORT filesep OUT_FILENAME];
   disp( sprintf( 'out file: %s', OUT_FILENAME ) );
   
   fid = fopen( OUT_FILENAME, 'w' );
   if ( fid == -1 )
     error( sprintf( 'labx2eeglab_shell: cannot open out_filename (%s).  Returning without further processing.', OUT_FILENAME ) );
     return
   end

   for sess = SESS_START:SESS_END
      prefix = sprintf( '%s%s', SUBJ_LONG, num2str( sess ) );
      cmd = sprintf( 'ExportABMFormat( EEGLAB, %s.ebs.edf, %s_Markers.mrk )',...
                     prefix, prefix );
      fprintf( fid, cmd );
      fprintf( fid, '\n' );
   end

   fclose( fid );

end
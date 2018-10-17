OUT_FILENAME = 'labx_conversion2_tmp.blab'
SUBJ = '026111'
SESS_START = 501
SESS_END = 510

fid = fopen( OUT_FILENAME, 'w' );

for i = SESS_START:SESS_END
  prefix = sprintf( '%s%s', SUBJ, num2str( i ) );
  cmd = sprintf( 'ExportABMFormat( EEGLAB, %s.ebs.edf, %s_Markers.mrk )',...
    prefix, prefix );
  fprintf( fid, cmd );
  fprintf( fid, '\n' );
end

fclose( fid );

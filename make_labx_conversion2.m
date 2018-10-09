in_filename = 'labx_conversion2_tmp.blab'

subj = '026111'

sess_start = 501
sess_end = 510

fid = fopen( in_filename, 'w' );

for i = sess_start:sess_end
  prefix = sprintf( '%s%s', subj, num2str( i ) );
  cmd = sprintf( 'ExportABMFormat( EEGLAB, %s.ebs.edf, %s_Markers.mrk )',...
    prefix, prefix );
  fprintf( fid, cmd );
  fprintf( fid, '\n' );
end

fclose( fid );

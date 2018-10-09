function [events, header] = convert_events( in_filename, out_filename )
% @brief convert output of LabX into something EEGLab can read
%
% testing:
%   in_filename = 'C:\Users\suhas\Desktop\prjs\golf_processing\data\ABM - Old Golf Data\NUGA Golfers\0261\0261\026111501_Markers.mrk_Events_EEGLAB.csv'
%   out_filename = 'C:\Users\suhas\Desktop\prjs\golf_processing\data\ABM - Old Golf Data\NUGA Golfers\0261\0261\026111501_Markers.mrk_Events_EEGLAB_simple.csv'
%   [events, header] = convert_events( in_filename, out_filename )

  fid = fopen( in_filename );
  if ( fid == -1 )
    disp( sprintf( 'convert_events: in_filename (%s) not found.  Returning without further processing.', in_filename ) );
    return
  end

  fid_out = fopen( out_filename, 'w' );
  if ( fid_out == -1 )
    disp( sprintf( 'convert_events: cannot open out_filename (%s).  Returning without further processing.', out_filename ) );
    return
  end

  % read header, and write new one to output file
  line = fgetl( fid );
  header = 'latency\ttype';
  fprintf( fid_out, header );
  fprintf( fid_out, '\n' );

  % read data
  line = fgetl( fid );
  line_ctr = 1;

  while ( line ~= -1 )
    data = textscan(line, '%s', 'Delimiter', ',', 'EmptyValue', nan);
    events(line_ctr).latency = str2num( data{1}{1} );
    events(line_ctr).type = data{1}{2};

    % write out latency and type
    fprintf( fid_out, '%f\t%s\n', events(line_ctr).latency, events(line_ctr).type );

    line = fgetl( fid );
    line_ctr = line_ctr+1;
  end

  fclose(fid);
  fclose(fid_out);
  

  
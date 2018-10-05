% in_filename = 'C:\Users\suhas\Desktop\prjs\golf_processing\data\ABM - Old Golf Data\NUGA Golfers\0261\0261\026111501_Markers.mrk_Paired.csv'
% out_filename = 'C:\Users\suhas\Desktop\prjs\golf_processing\data\ABM - Old Golf Data\NUGA Golfers\0261\0261\026111501_Markers.mat'
% [events] = make_events( in_filename, out_filename )

% Epoch
% Datapoint
% ESUTime
% SystemTime
% JavaTime
% PacketLength
% PacketType
% EventData1
% EventData2
% EventData3
% EventData4
% EventData5
% EventData6
% EventData7
% EventData8
% EventData9
% EventData10
% EventData11
% EventData12
% EventData13
% EventData14
% EventData15
% EventData16
% EventData17
% EventData18
% Checksum_Status

%>> EEG.event(1)
%
%ans = 
%
%  struct with fields:
%
%        type: 'square'
%    position: 2
%     latency: 218.0000
%     urevent: 2
%       epoch: 1    

function [events] = make_events( in_filename, out_filename )
  fid = fopen( in_filename );
  if ( fid == -1 )
    disp( 'make_events: ''in_filename'' not found.  Returning without further processing.' );
    return
  end

  % read header
  line = fgetl( fid );

  % read data
  line = fgetl( fid )
  line_ctr = 1;
  while ( line ~= -1 )
    data = textscan(line, '%s', 'Delimiter', ',', 'EmptyValue', nan);

    events(line_ctr).epoch = str2num( data{1}{1} )

    events(line_ctr).datapoint = str2num( data{1}{2} )
    %events.ESUTIME_orig(line_ctr) = data{1}{3}
    %events = setfield( events, ESUTIME_orig, data{1}{3} )

    events(line_ctr).latency = convert_time_to_seconds( data{1}{3} )
    events(line_ctr).type = str2num( data{1}{8} )
                                             
    events(line_ctr).EventData1 = convert_str_to_num_or_fill( data{1}{8}, -1 )
    events(line_ctr).EventData2 = convert_str_to_num_or_fill( data{1}{9}, -1 )
    events(line_ctr).EventData3 = convert_str_to_num_or_fill( data{1}{10}, -1 )
    events(line_ctr).EventData4 = convert_str_to_num_or_fill( data{1}{11}, -1 )
    events(line_ctr).EventData5 = convert_str_to_num_or_fill( data{1}{12}, -1 )
    events(line_ctr).EventData6 = convert_str_to_num_or_fill( data{1}{13}, -1 )
    events(line_ctr).EventData7 = convert_str_to_num_or_fill( data{1}{14}, -1 )
    events(line_ctr).EventData8 = convert_str_to_num_or_fill( data{1}{15}, -1 )
    events(line_ctr).EventData9 = convert_str_to_num_or_fill( data{1}{16}, -1 )
    events(line_ctr).EventData10 = convert_str_to_num_or_fill( data{1}{17}, -1 )
    events(line_ctr).EventData11 = convert_str_to_num_or_fill( data{1}{18}, -1 )
    events(line_ctr).EventData12 = convert_str_to_num_or_fill( data{1}{19}, -1 )
    events(line_ctr).EventData13 = convert_str_to_num_or_fill( data{1}{20}, -1 )
    events(line_ctr).EventData14 = convert_str_to_num_or_fill( data{1}{21}, -1 )
    events(line_ctr).EventData15 = convert_str_to_num_or_fill( data{1}{22}, -1 )
    events(line_ctr).EventData16 = convert_str_to_num_or_fill( data{1}{23}, -1 )
    events(line_ctr).EventData17 = convert_str_to_num_or_fill( data{1}{24}, -1 )
    events(line_ctr).EventData18 = convert_str_to_num_or_fill( data{1}{25}, -1 )

    line = fgetl( fid );
    line_ctr = line_ctr+1;
  end
  fclose(fid)

  save(out_filename,'events')

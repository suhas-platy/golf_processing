function [events, header, ignored_events] = convert_events( in_filename, out_filename, varargin )
% @brief convert output of LabX into something EEGLab can read
%
% testing:
%   in_filename = 'C:\Users\suhas\Desktop\prjs\golf_processing\data\ABM - Old Golf Data\NUGA Golfers\0261\0261\026111501_Markers.mrk_Events_EEGLAB.csv'
%   out_filename = 'C:\Users\suhas\Desktop\prjs\golf_processing\data\ABM - Old Golf Data\NUGA Golfers\0261\0261\026111501_Markers.mrk_Events_EEGLAB_simple.csv'
%   % this is optional
%   merged_markers_filename = 'C:\Users\suhas\Desktop\prjs\golf_processing\data\ABM - Old Golf Data\merged_markers\merged_markers\0261_Markers_merged.xlsx'
%   [events, header] = convert_events( in_filename, out_filename, 'merged_markers_filename', merged_markers_filename )

  % global param's
  DNE_SUCCESS_IN_OUTPUT = -1; % if we don't have merged markers, use this dummy value to put in the output file
   
  % handle arguments
  HAVE_MERGED_MARKERS = 0;
  VERBOSE = 1;
  opts = cell2struct(varargin(2:2:end),varargin(1:2:end),2);
  if ( isfield(opts, 'merged_markers_filename' ) )
     HAVE_MERGED_MARKERS = 1;
  end
  if ( isfield(opts, 'verbose' ) )
     VERBOSE = opts.verbose;
  end
  
  % check if in_filename exists and figure out session number for it
  fid = fopen( in_filename );
  if ( fid == -1 )
    disp( sprintf( 'convert_events: in_filename (%s) not found.  Returning without further processing.', in_filename ) );
    return
  end
  % figure out session from filename
  [filepath,name,ext] = fileparts(in_filename);
  in_filename_session = str2num( name(7:9) ); % @warn hardcode
  disp( sprintf( 'convert_events: session = %d', in_filename_session ) );

  % check if out_filename exists
  fid_out = fopen( out_filename, 'w' );
  if ( fid_out == -1 )
    disp( sprintf( 'convert_events: cannot open out_filename (%s).  Returning without further processing.', out_filename ) );
    return
  end
  
  % parse the merged markers file if available
  if ( HAVE_MERGED_MARKERS )
     START_DATA_ROW_IDX = 2; % skip the header
     END_DATA_ROW_IDX = -1; % set below
     SESSION_IDX = 2;
     PUTT_IDX = 3;
     START_EPOCH_IDX = 4;
     END_EPOCH_IDX = 5;
     START_END_IDX = 6;
     MARKER_IDX = 7;
     MARKER_FILE_COMMENT_IDX = 8;
     EVENT_IDX = 9;
     PUTT_PERFORMANCE_IDX = 10;
     SESSION_START_DATA_ROW_IDX = -1; % set below
     SESSION_END_DATA_ROW_IDX = -1; % set below

     TOLERANCE = 1.005; % .004 off in 501, 1.004 off in 502
     SUCCESS_IN_MERGED_MARKERS = 5;
     NOT_SUCCESS_IN_OUTPUT = 0;

     % read and parse
     [~,~,merged_markers_raw] = xlsread( opts.merged_markers_filename );
     % @todo catch file not found
     END_DATA_ROW_IDX = size( merged_markers_raw, 1 );

     ctr = 1;
     for i = START_DATA_ROW_IDX:END_DATA_ROW_IDX
       % session
       merged_markers_session(ctr) = merged_markers_raw{i, SESSION_IDX};
       
       % start epoch
       merged_markers_start_epoch(ctr) = merged_markers_raw{i, START_EPOCH_IDX};
       
       % end epoch
       merged_markers_end_epoch(ctr) = merged_markers_raw{i, END_EPOCH_IDX};
       
       % type
       tmp = merged_markers_raw{i, EVENT_IDX}; % handle Video Start and Video End
       if ( isnan(tmp) )
           tmp = merged_markers_raw{i, MARKER_FILE_COMMENT_IDX};
       end
       merged_markers_type{ctr} = tmp;
       
       % success
       tmp = merged_markers_raw{i, PUTT_PERFORMANCE_IDX};
       if ( isnan( tmp ) ) % handle Video Start and Video End, etc.
          tmp = NOT_SUCCESS_IN_OUTPUT;
       end
       merged_markers_success(ctr) = tmp;
       
       ctr = ctr+1;
     end

     % figure out first & last row in session
     session_idx = find( merged_markers_session == in_filename_session );
     SESSION_START_DATA_ROW_IDX = session_idx(1);
     SESSION_END_DATA_ROW_IDX = session_idx(end);
  end

  % read header in in_filename, and write a new one to out_filename
  line = fgetl( fid );
  header = 'latency\ttype\tsuccess';
  fprintf( fid_out, header );
  fprintf( fid_out, '\n' );

  % read data in in_filename and write along the way
  line = fgetl( fid );
  line_ctr = 1;
  do_not_increment_line_ctr_for_merged_markers = false;
  skip_lines = 0;
  ignored_events = [];
  while ( line ~= -1 )
    data = textscan(line, '%s', 'Delimiter', ',', 'EmptyValue', nan);
    
    % latency
    latency_str =  data{1}{1};
    latency_num = str2num( latency_str );
    
    % type
    type_str = data{1}{2};
    
    % pack away
    events(line_ctr).latency = latency_num;
    events(line_ctr).type = type_str; % always target; can be overridden below
    
    if ( HAVE_MERGED_MARKERS )
       merged_markers_row_idx = line_ctr + SESSION_START_DATA_ROW_IDX - 1 - skip_lines;
       %if ( do_not_increment_line_ctr_for_merged_markers )
       %   merged_markers_row_idx = merged_markers_row_idx - 1; % same as (line_ctr-1)
       %   do_not_increment_line_ctr_for_merged_markers = false;
       %end
       
       % latency
       time = merged_markers_start_epoch( merged_markers_row_idx );
       time_diff = events(line_ctr).latency - time;
       if ( abs( time_diff ) > TOLERANCE )
         % check events before and after
         time_pre = merged_markers_start_epoch( merged_markers_row_idx - 1 );
         time_diff_pre = events(line_ctr-1).latency - time_pre;
         
         time_post = merged_markers_start_epoch( merged_markers_row_idx +1 1 );
         time_diff_post = events(line_ctr).latency - time_post;         
           
           
         warning( sprintf( 'convert_events: line %d (%f seconds) off by %f seconds from merged markers file; ignoring entry',...
                           line_ctr, latency_num, time_diff ) );
         ignored_events = [ignored_events line_ctr];
         line = fgetl( fid );
         line_ctr = line_ctr+1;
         do_not_increment_line_ctr_for_merged_markers = true;
         skip_lines = skip_lines+1;
         continue;
       end
       
       % type
       type_str = merged_markers_type{ merged_markers_row_idx };
       if ( strfind( lower(type_str), lower('Video Start') ) )
	      type_str = 'VideoStart';
       end
       if ( strfind( lower(type_str), lower('Video End') ) )
	      type_str = 'VideoEnd';
       end          
       if ( strfind( lower(type_str), lower('End Play') ) )
          type_str = 'EndPlay';
       end
       if ( strfind( lower(type_str), lower('Error Marker') ) )
          type_str = 'ErrorMarker';
       end

       % pack away
       events(line_ctr).latency = time;
       events(line_ctr).type = type_str;

       % success; pack away
       if ( merged_markers_success( merged_markers_row_idx ) == SUCCESS_IN_MERGED_MARKERS )
         events(line_ctr).success = 1;
       else
         events(line_ctr).success = 0;
       end
    else
      events(line_ctr).success = DNE_SUCCESS_IN_OUTPUT; % put a value in to write out below	 
    end
    
    % write out latency, type, etc.
    fprintf( fid_out, '%f\t%s\t%d\n', events(line_ctr).latency, events(line_ctr).type, events(line_ctr).success );

    if ( VERBOSE )
       if (mod(line_ctr,20)==0)
          disp( sprintf( 'convert_events: on line %d', line_ctr ) );
       end
    end

    line = fgetl( fid );
    line_ctr = line_ctr+1;
  end

  fclose(fid);
  fclose(fid_out);
function sec = convert_time_to_seconds( str )
  % 00:55:17:730
  nums = sscanf( str, '%d:%d:%d:%d' );
  sec = 0;
  sec = sec*nums(1)*60*60;
  sec = sec + nums(2)*60;
  sec = sec + nums(3);
  sec = sec + nums(4)/1000.
  

function ret = convert_str_to_num_or_fill( str, fill )
  if ( isequal(str,'') )
    ret = fill;
  else
    ret = str2num( str );
  end

% @brief make script to convert events files into something EEGLab can almost read (use convert_events_shell.m after this)

SUBJ_Z = [261:265];
%SUBJ_Z = [261 263:265];
SESS_START = 501;
SESS_END = 502;
PATH = 'C:\Users\suhas\Desktop\prjs\golf_processing\data\ABM - Old Golf Data\';
PATH = [PATH 'NUGA Golfers\'];

for subj = 1:size(SUBJ_Z,2)
   curr_subj = SUBJ_Z( subj );
   SUBJ_SHORT = ['0' num2str( curr_subj )];
   SUBJ_LONG = ['0' num2str( curr_subj ) '11']; 

   for sess = SESS_START:SESS_END
     eeglabhist_one_subj( curr_subj, sess );
   end
   
end
% @brief preprocess one subject

% test
% SUBJ = 261; SESS = 501;
% eeglabhist_one_subj( SUBJ, SESS )

function eeglabhist_one_subj( SUBJ, SESS )
C4_IDX = 10; C4_TXT = 'C4';
P3_IDX = 12; P3_TXT = 'P3';

DO_ARTIFACT_REMOVAL = 0;

clear ALLEEG EEG CURRENTSET ALLCOM;
[ALLEEG EEG CURRENTSET ALLCOM] = eeglab;

% load and drop ECG
filename = sprintf( 'C:\\Users\\suhas\\Desktop\\prjs\\golf_processing\\data\\ABM - Old Golf Data\\NUGA Golfers\\%s\\%s11%s.ebs.edf.EEGLAB.edf',...
                    ['0' num2str( SUBJ )], ['0' num2str( SUBJ )], num2str( SESS ) );
disp( sprintf( 'infilename = %s', filename ) );
EEG = pop_biosig(filename, 'channels',[1:20] );
EEG = eeg_checkset( EEG );
figure(1); pop_eegplot( EEG, 1, 1, 1);

% bandpass b/t .1 and 60 Hz
EEG = pop_eegfiltnew(EEG, 0.1,60,8448,0,[],0);
figure(2); pop_eegplot( EEG, 1, 1, 1);

% import events
EEG = eeg_checkset( EEG );
events_filename = sprintf( 'C:\\Users\\suhas\\Desktop\\prjs\\golf_processing\\data\\ABM - Old Golf Data\\NUGA Golfers\\%s\\%s11%s_Markers.mrk_Events_EEGLAB_simple.csv',...
    ['0' num2str( SUBJ )], ['0' num2str( SUBJ )], num2str( SESS ) );
EEG = pop_importevent( EEG, 'event',events_filename,'fields',{'latency' 'type' 'success'},'skipline',1,'timeunit',1);
%[ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET);
%EEG = pop_importevent( EEG, 'event','no','event',events_filename,'fields',{'latency' 'type' 'success'},'skipline',1,'timeunit',1,'align',0);
%EEG = pop_importevent( EEG, 'append','no','event','fields',{'latency' 'type' 'success'},'skipline',1,'timeunit',1,'align',0);
[ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET);

% crop to -5 to 1 from Putt
EEG = eeg_checkset( EEG );
EEG = pop_epoch( EEG, {  'Putt'  }, [-5  1], 'newname', 'EDF file epochs', 'epochinfo', 'yes');

% remove baseline from -4 to 0
EEG = eeg_checkset( EEG );
EEG = pop_rmbase( EEG, [-4000     0]);
[ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, 1,'overwrite','on','gui','off'); 
EEG = eeg_checkset( EEG );
figure(3);pop_eegplot( EEG, 1, 1, 1);

% artifact removal; these param's are too conservative
if ( DO_ARTIFACT_REMOVAL )
EEG = eeg_checkset( EEG );
EEG = pop_eegthresh(EEG,1,[1:20] ,-25,25,-5,0.996,2,0);
EEG = pop_rejtrend(EEG,1,[1:20] ,1536,50,0.3,2,0);
EEG = pop_jointprob(EEG,1,[1:20] ,5,5,0,0,0,[],0);
EEG = pop_jointprob(EEG,1,[1:20] ,5,5,0,0,'set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''mantrial''), ''string'', num2str(sum(EEG.reject.rejmanual)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''threshtrial''), ''string'', num2str(sum(EEG.reject.rejthresh)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''freqtrial''), ''string'', num2str(sum(EEG.reject.rejfreq)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''consttrial''), ''string'', num2str(sum(EEG.reject.rejconst)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''enttrial''), ''string'', num2str(sum(EEG.reject.rejjp)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''kurttrial''), ''string'', num2str(sum(EEG.reject.rejkurt)));',[],0);
EEG = pop_rejkurt(EEG,1,[1:20] ,5,5,0,0,0,[],0);
EEG = pop_rejkurt(EEG,1,[1:20] ,5,5,0,0,'set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''mantrial''), ''string'', num2str(sum(EEG.reject.rejmanual)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''threshtrial''), ''string'', num2str(sum(EEG.reject.rejthresh)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''freqtrial''), ''string'', num2str(sum(EEG.reject.rejfreq)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''consttrial''), ''string'', num2str(sum(EEG.reject.rejconst)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''enttrial''), ''string'', num2str(sum(EEG.reject.rejjp)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''kurttrial''), ''string'', num2str(sum(EEG.reject.rejkurt)));',[],0);
EEG = pop_rejspec( EEG, 1,'elecrange',[1:20] ,'method','multitaper','threshold',[-25 25] ,'freqlimits',[0 50] ,'eegplotcom','set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''mantrial''), ''string'', num2str(sum(EEG.reject.rejmanual)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''threshtrial''), ''string'', num2str(sum(EEG.reject.rejthresh)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''freqtrial''), ''string'', num2str(sum(EEG.reject.rejfreq)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''consttrial''), ''string'', num2str(sum(EEG.reject.rejconst)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''enttrial''), ''string'', num2str(sum(EEG.reject.rejjp)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''kurttrial''), ''string'', num2str(sum(EEG.reject.rejkurt)));','eegplotplotallrej',2,'eegplotreject',0);
end

% plot ERP image for C4 and P3
EEG = eeg_checkset( EEG );
figure; pop_erpimage(EEG,1, [C4_IDX],[[]],C4_TXT,5,1,{},[],'' ,'yerplabel','\muV','erp','on','cbar','on','topo', { [C4_IDX] EEG.chanlocs EEG.chaninfo } );
figure; pop_erpimage(EEG,1, [P3_IDX],[[]],P3_TXT,5,1,{},[],'' ,'yerplabel','\muV','erp','on','cbar','on','topo', { [P3_IDX] EEG.chanlocs EEG.chaninfo } );

% plot ERSP
EEG = eeg_checkset( EEG );
figure; pop_newtimef( EEG, 1, C4_IDX, [-5000   996], [3         0.5] , 'baseline',[0], 'alpha',.01,'padratio', 16, 'plotphase', 'off', 'padratio', 1, 'winsize', 1280);

% save
filename = sprintf( 'C:\\Users\\suhas\\Desktop\\prjs\\golf_processing\\data\\ABM - Old Golf Data\\NUGA Golfers\\%s\\',...
    ['0' num2str( SUBJ )] );
disp( sprintf( 'outfilename = %s', filename ) );
EEG = pop_saveset( EEG, 'filename','eeglab_export_5sBeforePutts1sAfter_proc.set','filepath',filename);
[ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% always end w/ redraw
eeglab redraw
#-- GAUDI jobOptions generated on Mon Feb 15 16:56:20 2016
#-- Contains event types : 
#--   24142001 - 5 files - 97087 events - 15.76 GBytes


#--  Extra information about the data processing phases:


#--  Processing Pass Step-128049 

#--  StepId : 128049 
#--  StepName : Reco15em for MC 2015, DST 
#--  ApplicationName : Brunel 
#--  ApplicationVersion : v47r9 
#--  OptionFiles : $APPCONFIGOPTS/Brunel/DataType-2015.py;$APPCONFIGOPTS/Brunel/saveFittedVeloTracks.py;$APPCONFIGOPTS/Brunel/MC-WithTruth.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : fromPreviousStep 
#--  CONDDB : fromPreviousStep 
#--  ExtraPackages : AppConfig.v3r224 
#--  Visible : Y 


#--  Processing Pass Step-128074 

#--  StepId : 128074 
#--  StepName : Turbo stream for MC 2015 Early Measurments, to process v23r7p6 Moore with DaVinci v36r7p7 (DST in, DST out) 
#--  ApplicationName : DaVinci 
#--  ApplicationVersion : v36r7p7 
#--  OptionFiles : $APPCONFIGOPTS/Turbo/Tesla_EM_AllHlt2Lines_v9r9b.py;$APPCONFIGOPTS/Turbo/Tesla_Simulation_2015_PVHLT2.py 
#--  DDDB : fromPreviousStep 
#--  CONDDB : fromPreviousStep 
#--  ExtraPackages : AppConfig.v3r224;TurboStreamProd.v1r4 
#--  Visible : Y 

from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles(['LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000001_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000002_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000003_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000004_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000005_2.dst'
], clear=True)
FileCatalog().Catalogs += [ 'xmlcatalog_file:MC15_reco_test.xml' ]

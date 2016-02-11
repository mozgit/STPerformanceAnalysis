#-- GAUDI jobOptions generated on Thu Feb  4 11:19:19 2016
#-- Contains event types : 
#--   90000000 - 4 files - 418 events - 0.02 GBytes


#--  Extra information about the data processing phases:


#--  Processing Pass Step-127012 

#--  StepId : 127012 
#--  StepName : Stripping21-Merging-DV-v36r1 
#--  ApplicationName : DaVinci 
#--  ApplicationVersion : v36r1 
#--  OptionFiles : $APPCONFIGOPTS/Merging/DV-Stripping-Merging.py 
#--  DDDB : dddb-20130929-1 
#--  CONDDB : cond-20141107 
#--  ExtraPackages : AppConfig.v3r203;SQLDDDB.v7r10 
#--  Visible : N 

from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles(['LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00000007_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00000021_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00000035_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision12/DIMUON.DST/00041836/0000/00041836_00000049_1.dimuon.dst'
], clear=True)
FileCatalog().Catalogs += [ 'xmlcatalog_file:2012_data_test.xml' ]

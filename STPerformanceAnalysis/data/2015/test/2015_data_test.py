#-- GAUDI jobOptions generated on Mon Jan 25 11:00:28 2016
#-- Contains event types : 
#--   90000000 - 6 files - 199801 events - 23.62 GBytes


#--  Extra information about the data processing phases:


#--  Processing Pass Step-128576 

#--  StepId : 128576 
#--  StepName : Stripping23r1-Merging-DV-v37r2p4-AppConfig-v3r241 
#--  ApplicationName : DaVinci 
#--  ApplicationVersion : v37r2p4 
#--  OptionFiles : $APPCONFIGOPTS/Merging/DV-Stripping-Merging.py 
#--  DDDB : dddb-20150724 
#--  CONDDB : cond-20150828 
#--  ExtraPackages : AppConfig.v3r241;SQLDDDB.v7r10 
#--  Visible : N 

from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles(['LFN:/lhcb/LHCb/Collision15/DIMUON.DST/00048460/0000/00048460_00000027_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision15/DIMUON.DST/00048460/0000/00048460_00000057_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision15/DIMUON.DST/00048460/0000/00048460_00000092_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision15/DIMUON.DST/00048460/0000/00048460_00000122_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision15/DIMUON.DST/00048460/0000/00048460_00000131_1.dimuon.dst',
'LFN:/lhcb/LHCb/Collision15/DIMUON.DST/00048460/0000/00048460_00000188_1.dimuon.dst'
], clear=True)
FileCatalog().Catalogs += [ 'xmlcatalog_file:2015_data_test.xml' ]

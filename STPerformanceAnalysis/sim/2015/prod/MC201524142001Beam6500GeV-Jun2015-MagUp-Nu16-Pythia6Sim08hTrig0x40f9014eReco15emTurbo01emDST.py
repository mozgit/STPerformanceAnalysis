#-- GAUDI jobOptions generated on Mon Feb 15 16:55:25 2016
#-- Contains event types : 
#--   24142001 - 342 files - 6663935 events - 1081.00 GBytes


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
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000005_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000006_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000007_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000008_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000009_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000010_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000011_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000012_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000013_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000015_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000016_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000017_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000018_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000019_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000020_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000021_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000022_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000023_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000024_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000025_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000026_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000027_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000028_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000029_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000030_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000031_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000032_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000033_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000034_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000035_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000036_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000037_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000038_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000039_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000040_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000041_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000042_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000043_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000044_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000045_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000046_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000047_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000048_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000049_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000050_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000051_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000052_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000053_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000054_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000055_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000056_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000057_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000058_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000059_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000060_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000061_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000062_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000063_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000064_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000065_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000066_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000067_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000068_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000069_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000070_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000071_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000072_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000073_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000074_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000075_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000076_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000077_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000078_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000079_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000080_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000081_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000082_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000083_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000084_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000085_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000086_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000087_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000089_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000090_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000091_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000092_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000093_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000094_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000095_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000096_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000097_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000098_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000099_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000100_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000101_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000102_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000103_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000104_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000106_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000107_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000108_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000109_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000110_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000111_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000112_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000113_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000114_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000115_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000116_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000117_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000118_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000119_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000120_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000121_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000122_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000123_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000124_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000125_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000126_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000127_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000128_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000129_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000130_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000131_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000132_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000133_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000134_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000135_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000136_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000137_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000138_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000139_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000140_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000141_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000142_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000143_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000144_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000145_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000146_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000147_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000148_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000149_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000151_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000152_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000153_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000154_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000155_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000156_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000157_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000158_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000159_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000160_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000161_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000162_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000163_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000164_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000165_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000166_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000167_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000168_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000169_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000171_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000172_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000173_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000174_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000175_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000176_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000177_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000178_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000179_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000180_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000181_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000182_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000183_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000184_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000185_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000186_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000187_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000188_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000190_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000191_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000192_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000193_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000194_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000195_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000196_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000197_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000198_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000199_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000200_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000201_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000202_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000203_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000204_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000205_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000206_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000207_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000208_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000209_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000211_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000212_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000213_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000214_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000215_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000216_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000217_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000218_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000219_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000220_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000221_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000222_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000223_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000224_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000225_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000226_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000227_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000228_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000230_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000231_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000233_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000234_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000235_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000236_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000237_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000238_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000239_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000240_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000241_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000242_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000244_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000245_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000246_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000247_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000248_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000249_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000250_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000251_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000252_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000253_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000254_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000255_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000256_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000257_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000258_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000259_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000261_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000262_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000263_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000264_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000265_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000266_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000267_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000268_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000269_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000270_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000271_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000272_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000273_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000274_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000275_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000276_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000277_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000278_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000279_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000280_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000281_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000282_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000283_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000284_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000285_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000287_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000288_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000289_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000290_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000291_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000293_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000294_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000295_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000296_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000297_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000298_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000299_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000300_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000301_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000302_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000303_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000304_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000305_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000306_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000307_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000309_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000310_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000311_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000312_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000313_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000314_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000315_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000316_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000317_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000318_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000319_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000320_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000321_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000322_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000323_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000324_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000325_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000326_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000327_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000328_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000329_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000330_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000331_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000332_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000333_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000334_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000335_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000337_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000338_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000339_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000340_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000341_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000342_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000343_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000344_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000345_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000346_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000347_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000348_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000349_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000350_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000351_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000352_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000353_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000354_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000356_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000357_2.dst',
'LFN:/lhcb/MC/2015/DST/00046261/0000/00046261_00000358_2.dst'
], clear=True)
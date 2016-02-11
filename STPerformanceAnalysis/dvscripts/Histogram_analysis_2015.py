itwindow = 0.4
itcollectorwindow = 0.4
itxTol = 1.
ityTol = 0.

ttwindow = 0.4
ttcollectorwindow = 0.4
ttxTol = 1.
ttyTol = 0.

particlesAndCuts = { "/Event/Dimuon/Phys/FullDSTDiMuonJpsi2MuMuDetachedLine/Particles" : "ALL" }


from Configurables import GaudiSequencer

mainSeq = GaudiSequencer( 'MainSeq' )
mainSeq.MeasureTime = True
mainSeq.IgnoreFilterPassed = False

from Configurables import DecodeVeloRawBuffer, RawBankToSTClusterAlg, UnpackTrack

from Configurables import STOfflinePosition

itClusterPosition = STOfflinePosition('ToolSvc.ITClusterPosition')
itClusterPosition.DetType  = 'IT'

ttClusterPosition = STOfflinePosition('ToolSvc.STOfflinePosition')

from Configurables import HltRoutingBitsFilter
physFilter = HltRoutingBitsFilter( "PhysFilter", RequireMask = [ 0x0, 0x4, 0x0 ] )

veloDecoder = DecodeVeloRawBuffer('VeloDecoder')
veloDecoder.DecodeToVeloLiteClusters = False
veloDecoder.DecodeToVeloClusters = True

itDecoder = RawBankToSTClusterAlg('ITDecoder') 
itDecoder.DetType = 'IT'

ttDecoder = RawBankToSTClusterAlg('TTDecoder')

from PhysSelPython.Wrappers import Selection, SelectionSequence, AutomaticData
from Configurables import FilterDesktop

myInputParticlesList = []
myParticlesFilterList = []
myParticlesList = []
myParticlesSeqList = []
myParticlesLocationList = []

filterSeq = GaudiSequencer( 'FilterSeq' )
filterSeq.ModeOR = True

codeIN = ""

for particles, cuts in particlesAndCuts.iteritems():
    codeIN = codeIN.replace("||","|")
    codeIN += "(CONTAINS( '"+str(particles)+"' )>0) || "
    
    myParticlesName = particles.split("/")[-2]

    myInputParticlesList += [ AutomaticData( Location = particles ) ]
    
    myParticlesFilterList += [ FilterDesktop( myParticlesName+"Filter",
                                              Code = cuts ) ]
    myParticlesList += [ Selection( myParticlesName,
                                    Algorithm = myParticlesFilterList[-1],
                                    RequiredSelections = [ myInputParticlesList[-1] ] ) ]
    
    myParticlesSeqList += [ SelectionSequence( myParticlesName+"Seq",
                                               TopSelection = myParticlesList[-1] ) ]

    myParticlesLocationList += [ myParticlesList[-1].outputLocation() ]
    
    filterSeq.Members += [ myParticlesSeqList[-1].sequence() ]

codeIN = codeIN.replace(" || ","")

from Configurables import LoKi__VoidFilter as EventFilter

inputFilter = EventFilter( name = 'InputFilter',
                           Code = codeIN )

from Configurables import ChargedParticlesToTracks

tracks = ChargedParticlesToTracks("ChargedParticlesToTracks")
tracks.ParticlesLocations = myParticlesLocationList
tracks.TracksOutputLocation = "/Event/Rec/Track/MyBest"
tracks.RefitTracks = True
tracks.FullDetail = True
tracks.MassWindow = 40.
tracks.MassOffset = 3.
                               
from Configurables import TrackContainerCleaner, TrackSelector

cleaner = TrackContainerCleaner( 'GoodTracks' )
cleaner.inputLocation = "/Event/Rec/Track/MyBest"
cleaner.addTool( TrackSelector, name = 'Selector' )
cleaner.Selector.MinPCut    = 10000.
cleaner.Selector.MaxChi2Cut = 3.
cleaner.Selector.TrackTypes = [ "Long" ]

cleaner2 = TrackContainerCleaner( 'ExcellentTracks' )
cleaner2.inputLocation = "/Event/Rec/Track/MyBest"
cleaner2.addTool( TrackSelector, name = 'Selector' )
cleaner2.Selector.MaxChi2Cut = 2.
cleaner2.Selector.MaxChi2PerDoFMatch = 2.
cleaner2.Selector.MaxChi2PerDoFDownstream = 2.
cleaner2.Selector.MaxChi2PerDoFVelo = 2.
cleaner2.Selector.TrackTypes = [ "Long" ]

from Configurables import STEfficiency, STClusterCollector, STSelectChannelIDByElement

ttEff = STEfficiency( "TTHitEfficiency" )
ttEff.TracksInContainer  = "/Event/Rec/Track/MyBest"
ttEff.DetType            = "TT"
ttEff.Cuts               = [ 2.e-3, 5.e-3, 1.e-2, 2.e-2, 3.e-2, 4.e-2, 6.e-2, 8.e-2, 1.e-1, 1.5e-1, 2.e-1, 3.e-1, 4.e-1]
ttEff.XLayerCut          = 0.4 #0.4
ttEff.StereoLayerCut     = 0.4 #0.4
# Minimum number of expected sectors required
ttEff.MinExpectedSectors = 2 #2
# Maximum number of found - expected hits
ttEff.MaxNbResSectors    = 10
# Minimum number of stations where hits are on the track
ttEff.MinStationPassed   = 1
# Edge size excluded of the computation
ttEff.MinDistToEdgeX     = 2 #0.4
ttEff.MinDistToEdgeY     = 2 #0.4
# Not dump the efficiency plot, because of the merging afterwards
ttEff.EfficiencyPlot     = True
# Dump all the biased residual histograms
ttEff.ResidualsPlot      = True
# Dump all the control histograms (for experts)
ttEff.FullDetail         = True
# Dump all the control histograms (for experts)
ttEff.SingleHitPerSector = True
# Take hits found by STClusterCollector
ttEff.TakeEveryHit       = True
ttEff.OutputLevel        = 3
ttEff.TH2DSummaryHist    = True



itEff = STEfficiency( "ITHitEfficiency" )
itEff.TracksInContainer  = "/Event/Rec/Track/MyBest"
itEff.DetType            = "IT"
# Steps for hit efficiency measurements as a function of search window
itEff.Cuts               = [ 2.e-3, 5.e-3, 1.e-2, 2.e-2, 3.e-2, 4.e-2, 6.e-2, 8.e-2, 1.e-1, 1.5e-1, 2.e-1, 3.e-1, 4.e-1]
# Search window (must be at least larger than the last value of Cuts property)
itEff.XLayerCut          = 0.4 #0.4
itEff.StereoLayerCut     = 0.4 #0.4
# Minimum number of expected sectors required
itEff.MinExpectedSectors =  6 #6
# Maximum number of found - expected hits
itEff.MaxNbResSectors    = 10
# Minimum number of stations where hits are on the track
itEff.MinStationPassed   =  3 #3
# Edge size excluded of the computation
itEff.MinDistToEdgeX     = 2 #0.4
itEff.MinDistToEdgeY     = 2 #0.4
# Not dump the efficiency plot, because of the merging afterwards
itEff.EfficiencyPlot     = True
# Dump all the biased residual histograms
itEff.ResidualsPlot      = True
# Dump all the control histograms (for experts)
itEff.FullDetail         = True
# No more than one found hit per sector
itEff.SingleHitPerSector = True
# Take hits found by STClusterCollector
itEff.TakeEveryHit       = True
itEff.OutputLevel        = 3
itEff.TH2DSummaryHist    = True

# Collecting the ST clusters
itClusterCollector = STClusterCollector( "ToolSvc.ITClusterCollector" )
itClusterCollector.DetType           = "IT"
itClusterCollector.ignoreHitsOnTrack = False
itClusterCollector.xTol              = itxTol
itClusterCollector.yTol              = ityTol
itClusterCollector.window            = itcollectorwindow
itClusterCollector.MagFieldOn        = True
itClusterCollector.dataLocation      = "/Event/Raw/IT/Clusters"

ttClusterCollector = STClusterCollector( "ToolSvc.TTClusterCollector" )
ttClusterCollector.DetType           = "TT"
ttClusterCollector.ignoreHitsOnTrack = False
ttClusterCollector.xTol              = ttxTol
ttClusterCollector.yTol              = ttyTol
ttClusterCollector.window            = ttcollectorwindow
ttClusterCollector.MagFieldOn        = True
ttClusterCollector.dataLocation      = "/Event/Raw/TT/Clusters"

#########################################################################################
### Calculating hit resolution and signal-to-noise ratio                               ##
#########################################################################################

from Configurables import ITTrackMonitor, TTTrackMonitor, TrackMonitor

trackMon = TrackMonitor('TrackMonitor')
trackMon.TracksInContainer = "/Event/Rec/Track/MyBest"

itMon = ITTrackMonitor('ITTrackMonitor')
itMon.TracksInContainer = "/Event/Rec/Track/MyBest"
# Dump all the plots
itMon.FullDetail = True
# Dump all the plots per layers
itMon.plotsByLayer = True
itMon.plotsBySector = True
# Minimum number of found hits on track
itMon.minNumITHits = 6

ttMon = TTTrackMonitor('TTTrackMonitor')
ttMon.TracksInContainer = "/Event/Rec/Track/MyBest"
# Dump all the plots
ttMon.FullDetail = True
ttMon.plotsBySector = True
ttMon.TH2DSummaryHist = True
# Minimum number of found hits on track
ttMon.minNumTTHits = 2


from TrackFitter.ConfiguredFitters import ConfiguredFit

from Configurables import CondDB, CondDBAccessSvc


mainSeq.Members += [ inputFilter, filterSeq,
                     UnpackTrack(), 
                     veloDecoder, ttDecoder, itDecoder,
                     tracks, cleaner, cleaner2,
                     trackMon, itMon, ttMon, 
                     itEff, ttEff
                     ]

from Configurables import DaVinci
DaVinci().EvtMax   = 1000
#DaVinci().SkipEvents = 10000
DaVinci().PrintFreq = 100
DaVinci().DataType = "2015"
DaVinci().Simulation = False
from Configurables import CondDB
CondDB().UseLatestTags = ["2015"]

DaVinci().HistogramFile = "STTrackMonitor-HitEfficiency.root"
DaVinci().UserAlgorithms = [ mainSeq ]

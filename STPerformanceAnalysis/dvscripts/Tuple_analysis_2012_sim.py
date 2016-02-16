itwindow = 0.4
itcollectorwindow = 0.4
itxTol = 1.
ityTol = 0.

ttwindow = 0.4
ttcollectorwindow = 0.4
ttxTol = 1.
ttyTol = 0.

particlesAndCuts = { "/Event/AllStreams/Phys/FullDSTDiMuonJpsi2MuMuDetachedLine/Particles" : "ALL" }

#Initialization of Gaudi sequence
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


#Finding location input of particles
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

#Creating tracks from obtained particles
from Configurables import ChargedParticlesToTracks

tracks = ChargedParticlesToTracks("ChargedParticlesToTracks")
tracks.ParticlesLocations = myParticlesLocationList
tracks.TracksOutputLocation = "/Event/Rec/Track/MyBest"
tracks.RefitTracks = True
tracks.FullDetail = True
tracks.MassWindow = 40.
tracks.MassOffset = 3.
                               
#Selection of tracks
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

#Initializing track tuple algorithms
from Configurables import STEfficiency, STClusterCollector, STSelectChannelIDByElement, STTrackTuple
itTupleMon = STTrackTuple( "ITHitMonitor" )
itTupleMon.TracksInContainer  = "/Event/Rec/Track/MyBest"
itTupleMon.DetType            = "IT"
# Search window (must be at least larger than the last value of Cuts property)
itTupleMon.XLayerCut          = itwindow
itTupleMon.StereoLayerCut     = itwindow
# Minimum number of expected sectors required
itTupleMon.MinExpectedSectors = 6
# Maximum number of found - expected hits
itTupleMon.MaxNbResSectors    = 10
# Minimum number of stations where hits are on the track
itTupleMon.MinStationPassed   = 3
# Edge size excluded of the computation
itTupleMon.MinDistToEdgeX     = 2.
itTupleMon.MinDistToEdgeY     = 2.
# Not dump the efficiency plot, because of the merging afterwards
itTupleMon.EfficiencyPlot     = False
# Dump all the biased residual histograms
itTupleMon.ResidualsPlot      = False
# Dump all the control histograms (for experts)
itTupleMon.FullDetail         = False
# No more than one found hit per sector
itTupleMon.SingleHitPerSector = True
# Take hits found by STClusterCollector
itTupleMon.HitsOnTrack       = True
#itTupleMon.TestProperty       = True
itTupleMon.OutputLevel        = 3
itTupleMon.EfficiencyMode     = False
itTupleMon.SaveSectorPositions = False

itTupleEff = STTrackTuple( "ITHitEfficiency" )
itTupleEff.TracksInContainer  = "/Event/Rec/Track/MyBest"
itTupleEff.DetType            = "IT"
# Search window (must be at least larger than the last value of Cuts property)
itTupleEff.XLayerCut          = itwindow
itTupleEff.StereoLayerCut     = itwindow
# Minimum number of expected sectors required
itTupleEff.MinExpectedSectors = 6
# Maximum number of found - expected hits
itTupleEff.MaxNbResSectors    = 10
# Minimum number of stations where hits are on the track
itTupleEff.MinStationPassed   = 3
# Edge size excluded of the computation
itTupleEff.MinDistToEdgeX     = 2.
itTupleEff.MinDistToEdgeY     = 2.
# Not dump the efficiency plot, because of the merging afterwards
itTupleEff.EfficiencyPlot     = False
# Dump all the biased residual histograms
itTupleEff.ResidualsPlot      = False
# Dump all the control histograms (for experts)
itTupleEff.FullDetail         = False
# No more than one found hit per sector
itTupleEff.SingleHitPerSector = True
# Take hits found by STClusterCollector
itTupleEff.HitsOnTrack       = False
#itTupleEff.TestProperty       = True
itTupleEff.OutputLevel        = 3
itTupleEff.EfficiencyMode     = True
itTupleEff.SaveSectorPositions = False

ttTupleMon = STTrackTuple( "TTHitMonitor" )
ttTupleMon.TracksInContainer  = "/Event/Rec/Track/MyBest"
ttTupleMon.DetType            = "TT"
# Search window (must be at least larger than the last value of Cuts property)
ttTupleMon.XLayerCut          = itwindow
ttTupleMon.StereoLayerCut     = itwindow
# Minimum number of expected sectors required
ttTupleMon.MinExpectedSectors = 2
# Maximum number of found - expected hits
ttTupleMon.MaxNbResSectors    = 10
# Minimum number of stations where hits are on the track
ttTupleMon.MinStationPassed   = 1
# Edge size excluded of the computation
ttTupleMon.MinDistToEdgeX     = 2.
ttTupleMon.MinDistToEdgeY     = 2.
# Not dump the efficiency plot, because of the merging afterwards
ttTupleMon.EfficiencyPlot     = False
# Dump all the biased residual histograms
ttTupleMon.ResidualsPlot      = False
# Dump all the control histograms (for experts)
ttTupleMon.FullDetail         = False
# No more than one found hit per sector
ttTupleMon.SingleHitPerSector = True
# Take hits found by STClusterCollector
ttTupleMon.HitsOnTrack       = True
#ttTupleMon.TestProperty       = True
ttTupleMon.OutputLevel        = 3
ttTupleMon.EfficiencyMode     = False
ttTupleMon.SaveSectorPositions = False

ttTupleEff = STTrackTuple( "TTHitEfficiency" )
ttTupleEff.TracksInContainer  = "/Event/Rec/Track/MyBest"
ttTupleEff.DetType            = "TT"
# Search window (must be at least larger than the last value of Cuts property)
ttTupleEff.XLayerCut          = itwindow
ttTupleEff.StereoLayerCut     = itwindow
# Minimum number of expected sectors required
ttTupleEff.MinExpectedSectors = 2
# Maximum number of found - expected hits
ttTupleEff.MaxNbResSectors    = 10
# Minimum number of stations where hits are on the track
ttTupleEff.MinStationPassed   = 1
# Edge size excluded of the computation
ttTupleEff.MinDistToEdgeX     = 2.
ttTupleEff.MinDistToEdgeY     = 2.
# Not dump the efficiency plot, because of the merging afterwards
ttTupleEff.EfficiencyPlot     = False
# Dump all the biased residual histograms
ttTupleEff.ResidualsPlot      = False
# Dump all the control histograms (for experts)
ttTupleEff.FullDetail         = False
# No more than one found hit per sector
ttTupleEff.SingleHitPerSector = True
# Take hits found by STClusterCollector
ttTupleEff.HitsOnTrack       = False
#ttTupleEff.TestProperty       = True
ttTupleEff.OutputLevel        = 3
ttTupleEff.EfficiencyMode     = True
ttTupleEff.SaveSectorPositions = False


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


from TrackFitter.ConfiguredFitters import ConfiguredFit

from Configurables import CondDB, CondDBAccessSvc

mainSeq.Members += [ inputFilter, filterSeq,
                     UnpackTrack(), 
                     veloDecoder, ttDecoder, itDecoder,
                     tracks, cleaner, cleaner2,
                     #trackMon, itMon, ttMon, 
                     itTupleMon, itTupleEff, ttTupleEff, ttTupleMon]

from Configurables import DaVinci
DaVinci().EvtMax   = -1
DaVinci().PrintFreq = 1000000
DaVinci().DataType = "2012"
DaVinci().Simulation = True
from Configurables import CondDB
CondDB().UseLatestTags = ["2012"]

DaVinci().TupleFile = "Tuple.root"
DaVinci().UserAlgorithms = [ mainSeq ]

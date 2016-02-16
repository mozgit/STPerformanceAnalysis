itwindow = 0.4
itcollectorwindow = 0.4
itxTol = 1.
ityTol = 0.

ttwindow = 0.4
ttcollectorwindow = 0.4
ttxTol = 1.
ttyTol = 0.

#Currently we don't have strippted JPsi2MuMu 2015 samples.
#Thus, we have to simulate selection criteria of FullDSTDiMuonJpsi2MuMuDetachedLine on turbostream output
#If you will find  proper MC sample, code will be silimar to one for 2012
#particlesAndCuts = { "/Event/Dimuon/Phys/FullDSTDiMuonJpsi2MuMuDetachedLine/Particles" : "ALL" }

#Description of FullDSTDiMuonJpsi2MuMuDetachedLine line
#      "FullDSTDiMuonJpsi2MuMuDetachedLine" : {
#        "Prescale"  : 1.0,
#        "Inherit"   : "VirtualBase",
#        "checkPV"   : True,
#        "RequiredRawEvents" : ["Trigger", "Muon", "Calo", "Rich", "Velo", "Tracker"],
#        "InputDiMuon"   : "StdLooseJpsi2MuMu",
#        "Cuts"          : {
#          "MuonPt"        : "MINTREE('mu+'==ABSID,PT) > 500.0 *MeV",# replace!
#          "Mass"          : "(MM > 2996.916) & (MM < 3196.916)",
#          "Detachement"   : "((BPVDLS>3) | (BPVDLS<-3))",
#          "MuonPIDmu"     : "MINTREE('mu+'==ABSID,PIDmu) > 0.0"
#          }
#      },

# StdLooseJpsi2MuMu = CombineParticles ("StdLooseJpsi2MuMu")
# StdLooseJpsi2MuMu.Inputs = ["Phys/StdAllLooseMuons/Particles"]
# StdLooseJpsi2MuMu.DecayDescriptor = "J/psi(1S) -> mu+ mu-"
# StdLooseJpsi2MuMu.CombinationCut = "(ADAMASS('J/psi(1S)') < 100.*MeV) & (ADOCACHI2CUT(30,''))"
# StdLooseJpsi2MuMu.MotherCut = "(VFASPF(VCHI2) < 25.)"

cuts =  {
          "MuonPt"        : "(MINTREE('mu+'==ABSID,PT) > 500.0 *MeV)",
          "Mass"          : "(MM > 2996.916) & (MM < 3196.916)",
          #"Detachement"   : "((BPVDLS>3) | (BPVDLS<-3))", #Impossible to get this for Turbostream.
          "MuonPIDmu"     : "(MINTREE('mu+'==ABSID,PIDmu) > 0.0)",
          "JPsiVertex"    : "(VFASPF(VCHI2) < 25.)" #From StdLooseJpsi2MuMu
        }


cuts_line = ""
for i in cuts.values():
    cuts_line += i+"&"
cuts_line = cuts_line[:-1]

print cuts_line

tesla_line = "Hlt2JPsiReFitPVsTurbo"
tesla_particle_location = "/Event/Turbo/"+tesla_line+"/Particles"
tesla_vertex_location = "/Event/Turbo/"+tesla_line+"/Primary"
particlesAndCuts = { tesla_particle_location : cuts_line }


from Configurables import CombineParticles
StdLooseJpsi2MuMu = CombineParticles ("StdLooseJpsi2MuMu")
StdLooseJpsi2MuMu.Inputs = [tesla_particle_location]
StdLooseJpsi2MuMu.DecayDescriptor = "J/psi(1S) -> mu+ mu-"
StdLooseJpsi2MuMu.CombinationCut = "(ADAMASS('J/psi(1S)') < 100.*MeV) & (ADOCACHI2CUT(30,''))"
StdLooseJpsi2MuMu.MotherCut = cuts_line

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
from PhysSelPython.Wrappers import Selection, SelectionSequence
from PhysSelPython.Wrappers import AutomaticData
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
                                    Algorithm = StdLooseJpsi2MuMu,
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
DaVinci().DataType = "2015"
DaVinci().Simulation = True
from Configurables import CondDB
CondDB().UseLatestTags = ["2015"]

DaVinci().TupleFile = "Tuple.root"
DaVinci().UserAlgorithms = [ mainSeq ]

from GaudiConf import IOHelper
IOHelper().inputFiles(['/tmp/ikomarov/00046261_00000001_2.dst'])


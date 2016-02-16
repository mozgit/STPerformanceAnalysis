"""
This script submit DaVinci jobs to get information on ST performance in tuples
These scripts use pre-compiled version of DaVinci v38r1p1
"""

from Ganga.GPI import *
import sys
import inspect
import os


local_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
home_dir = "/afs/cern.ch/user/i/ikomarov/"

j = Job(application=DaVinci(version = 'v38r1p1', optsfile=local_dir + "/../dvscripts/Tuple_analysis_2012_sim.py", user_release_area=home_dir+'cmtuser/'))
j.application.platform = "x86_64-slc6-gcc49-opt"

j.name = "12_T_MC"
j.comment = "2012 simulation, Tuples"
j.inputdata = DaVinci().readInputData(local_dir + '/../sim/2012/prod/MC2012Beam4000GeV-2012-MagUp-Nu25-Pythia6Sim08aDigi13Trig0x409f0045Reco14aStripping20NoPrescalingFlagged24142001STREAMSDST.py')


j.do_auto_resubmit = True
j.outputfiles = [DiracFile("Tuple.root")]
j.backend = Dirac()

j.splitter = SplitByFiles(filesPerJob=90, ignoremissing = True)


j.submit()

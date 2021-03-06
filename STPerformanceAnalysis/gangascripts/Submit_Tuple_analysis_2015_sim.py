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

j = Job(application=DaVinci(version = 'v38r1p1', optsfile=local_dir + "/../dvscripts/Tuple_analysis_2015_sim.py", user_release_area=home_dir+'cmtuser/'))
j.application.platform = "x86_64-slc6-gcc49-opt"

j.name = "15_T_MC"
j.comment = "2015 MC, Tuples"
j.inputdata = DaVinci().readInputData(local_dir + '/../sim/2015/prod/MC201524142001Beam6500GeV-Jun2015-MagUp-Nu16-Pythia6Sim08hTrig0x40f9014eReco15emTurbo01emDST.py')


j.do_auto_resubmit = True
j.outputfiles = [DiracFile("Tuple.root")]
j.backend = Dirac()

j.splitter = SplitByFiles(filesPerJob=90, ignoremissing = True)


j.submit()

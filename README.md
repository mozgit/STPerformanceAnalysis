# ST Performance Analysis scripts
Here are collected scritps used for ST performance analysis in 2012/2015

These scripts were tested with DaVinci v38r1p1 compiled with head of Tr/TrackMonitors package (04 Feb 2016)

To run tests:

```
SetupProject DaVinci v38r1p1
cd data/<year>/test
gaudirun.py {Histogram, Tuple}_analysis_<year>.py <year>_data_test.py

```

To submit jobs to production, fix number of events in scripts and run:

```
cd gangascripts
source SetupEnvironment.sh
ganga Submit_{Histogram, Tuple}_analysis_<year>.py
```

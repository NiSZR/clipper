# clipper
Clipper estimates the RMS background noise and creates a sigma-clipping mask that preserves extended, low-surface brightness features. It is tested on ALMA interferometric cubes but should work on a variety of noisy observational data.
Just provide a positon-positon-velocity data cube and a continuum image. Then adapt the input parameters, defined in the headers of each script and run the scripts 1, 2, 3,4 with MIRIAD (https://www.atnf.csiro.au/computing/software/miriad/).
Script #4 is optional, but a useful template to remove bright sources that are blended with extended emission features.
The main output are moment maps of the emission.

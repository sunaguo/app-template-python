# Copyright (c) 2020 brainlife.io at University of Texas at Austin and Indiana University

# This file is a template for a python-based brainlife.io App
# brainlife stages this git repo, writes `config.json` and execute this script.
# this script reads the `config.json` and execute pynets container through singularity
#
# you can run this script(main) without any parameter to test how this App will run outside brainlife
# you will need to copy config.json.brainlife-sample to config.json before running `main` as `main`
# will read all parameters from config.json

# set up environment
from dipy.workflows.reconst import ReconstMAPMRIFlow
import json
import os.path

# load inputs from config.json
with open('config.json') as config_json:
	config = json.load(config_json)

	# Load into variables predefined code inputs
	data_file = str(config['dwi'])
	data_bval = str(config['bvals'])
	data_bvec = str(config['bvecs'])
	lap = bool(config['lap'])
	pos = bool(config['pos'])
	lap_weighting = float(config['laplacian_weighting'])
  
  # Defined final output metrics to save into file 
	save_metrics = ['rtop', 'msd', 'qiv', 'rtap', 'rtpp', 'ng', 'perng', 'parng']
	
  # get the command to run (in this case this is a python workflow)
  path = os.getcwd()
	mmri_flow = ReconstMAPMRIFlow()

  # run the actual python code (in this case part of the DIPY library)
  mmri_flow.run(data_file=data_file, data_bval=data_bval, data_bvec=data_bvec,
		  out_dir=path, laplacian=lap, positivity=pos, save_metrics=save_metrics,
		  lap_weighting=lap_weighting)

"""
imports.py - Helper script for main.py, models.py, training.py, output.py, plots.py, quasars.py
This script handles all module and data set imports for the core files.
"""
# Modules needed: astroML (has dependencies), itertools, termcolor, time
import numpy as np
from matplotlib import pyplot as plt
import itertools
from termcolor import colored
import time

from sklearn import model_selection, preprocessing
from sklearn import neighbors, linear_model, ensemble, neural_network, tree, svm
from sklearn import metrics

# Pull data from SDSS' DR7 quasar catalog
from astroML.datasets import fetch_dr7_quasar
raw_data = fetch_dr7_quasar()
count = len(raw_data)
print(colored(f"Imported {count} quasars", 'green'))
# Set each filter as a parameter
useJHK = True # Whether JHK wavebands are used
print(colored(f"JHK wavebands: {useJHK}", 'magenta'))
filters = ['mag_' + f for f in list('ugriz' + ('JHK' if useJHK else ''))]
nf = len(filters)
# The regular features array only has the raw magnitudes
features = np.zeros((count, nf))
for i in range(nf):
	features[:, i] = raw_data[filters[i]]

# The preprocessed array uses manually created filter combinations and normalizes values
# Magnitudes are normalized by comparing them to empirically determined values
offsets = [
	# mean , std
	[19.867, 1.456], # u
	[19.371, 0.959], # g
	[19.140, 0.832], # r
	[18.994, 0.805], # i
	[18.903, 0.812]  # z
]
if useJHK:
	offsets += [
		[17.062, 0.523], # J
		[16.203, 0.508], # H
		[15.554, 0.568]  # K
	]
ofs_data = {}
for i in range(nf):
	f = filters[i]
	ofs_data[f] = []
	for j in range(len(raw_data[f])):
		if raw_data[f][j] != 0:
			ofs_data[f].append((raw_data[f][j] - offsets[i][0]) / offsets[i][1])
		else:
			ofs_data[f].append(0)
	ofs_data[f] = np.array(ofs_data[f])
# Use one sum and one difference for each pair of filters
combs = list(itertools.combinations(filters, 2))
nCombs = len(combs)
featuresPre = np.zeros((count, nCombs * 2))
for i in range(nCombs):
	c = combs[i]
	featuresPre[:, i * 2] = (ofs_data[c[0]] + ofs_data[c[1]]) / 2
	featuresPre[:, i * 2 + 1] = ofs_data[c[0]] - ofs_data[c[1]]
# Take square root of magnitude
for f in featuresPre:
	for i in range(nCombs):
		n = f[i]
		sign = 1 if n >= 0 else -1
		n = ((n * sign) ** 1/2) * sign
targets = raw_data['redshift']
print(colored("Finished preprocessing", 'green'))
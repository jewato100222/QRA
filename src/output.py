"""
output.py - Helper script for main.py
This script handles outputting data files.
"""
from imports import *

# Attaches error statistics to results
def calcStats (results):
	# (Root) Mean Squared error
	results['ms'] = np.mean((results['pred'] - results['actual']) ** 2)
	print(f"MS error: {results['ms']}")
	results['rms'] = np.sqrt(results['ms'])
	print(f"RMS error: {results['rms']}")
	# R^2 value
	results['R2'] = metrics.r2_score(results['actual'], results['pred'])
	print(f"R^2: {results['R2']}")

data = {
	'N': []
}
# Adds a datum to the data frame
def saveResults (results):
	if results['name'] not in data:
		data[results['name']] = []
	if results['N'] not in data['N']:
		data['N'].append(results['N'])
	data[results['name']] += [
		round(results['ms'], 4),
		round(results['time'], 3)
	]

# Writes the output file for one run of the program
outPath = "../output/"
def writeOutput ():
	for i in [0, 1]:
		outputting = ['errors', 'runtimes'][i]
		outputStr = outputting + ', JHK = ' + str(useJHK)
		# Data points are spaced with tabs to allow pasting into a spreadsheet
		outputStr += '\n' + '\t'.join(['N'] + [str(N) for N in data['N']])
		for model in data:
			if model != 'N':
				outputStr += '\n' + '\t'.join([model] + [str(n) for n in data[model][i::2]])
		filePath = outPath + time.ctime() + ' ' + outputting + '.txt'
		stream = open(filePath, 'w')
		stream.write(outputStr)
		stream.close()
		print(colored(f"Saved {outputting} to {filePath}", 'cyan'))
"""
plots.py - Helper script for main.py, quasars.py
This script generates graphs for data produced.
"""
from imports import *

plotPath = "../plots/"
dispPlt = True # Whether to open all generated plots in a viewing window
print(colored(f"Display plots: {dispPlt}", 'magenta'))

def savePlot (fileName):
	savePath = plotPath + fileName
	plt.savefig(savePath, dpi = 200)
	print(colored("Saved plot to " + savePath, 'yellow'))
	if dispPlt:
		plt.show()

# Shows the results of training an estimator
def plotEstimator (name, N, results):
	# Set sizes
	plt.figure(figsize = (5, 5))
	ax = plt.axes()
	axis_lim = np.array([0, results['actual'].max()])

	# Set axes
	processed = 'preprocessed' if results['preprocess'] else 'unprocessed'
	title = f"{name} ($N$ = {N}, {processed})"
	plt.title(title)
	plt.xlim(axis_lim)
	plt.ylim(axis_lim)
	plt.xlabel(r"$z_\mathrm{actual}$", fontsize = 14)
	plt.ylabel(r"$z_\mathrm{pred}$", fontsize = 14)

	# Draw data
	# Color the dot according to magnitudes:
	# a = (r, g, b) ~ (mag_g - mag_r, mag_u - mag_g, mag_i - mag_u)
	# Some transformations are done for normalization.
	colors = []
	for r in results['orig']:
		colors.append((r[1] - r[2], r[0] - r[1] - 0.25, r[3] - r[0] + 0.5))
	colors = np.array(colors)
	# Draw scatter plot
	plt.scatter(
		results['actual'],
		results['pred'],
		c = np.clip(colors, 0, 1),
		alpha = min(5000 / N, 1),
		s = 2
	)
	
	# Statistics
	plt.plot(axis_lim, axis_lim, 'g') # Optimal value line
	plt.plot(axis_lim, axis_lim + results['rms'], ':r') # Positive error
	plt.plot(axis_lim, axis_lim - results['rms'], ':r') # Negative error
	plt.text(
		0.98,
		0.02,
		f"RMS error: {results['rms']:.3f}\n$R^2$: {results['R2']:.3f}\nRuntime: {results['time']:.3f} s",
		ha = 'right',
		va = 'bottom',
		transform = ax.transAxes,
		bbox = dict(ec = 'w', fc = 'w'),
		fontsize = 12
	)

	# Titles and display
	savePlot("estimators/" + title)
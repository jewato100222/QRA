"""
quasars.py
This script generates plots to represent the quasar data.
"""
from imports import *
from plots import *

# Shows distribution of parameters
def plotDistr (title, data, labels, colors, disp0 = False):
	plt.figure(figsize = (len(labels) * 0.75, 5))
	plt.margins(0.1)
	plt.title(title)
	plt.xticks(range(len(labels)), labels)

	for i in range(len(labels)):
		# Draw points
		l = labels[i]
		labelData = data[l]
		plt.scatter(
			[i] * len(data[labels[0]]),
			labelData,
			c = colors[i],
			alpha = min(250 / count, 1),
			s = 8
		)
		# Draw means
		nz = labelData[np.nonzero(labelData)]
		m = np.mean(nz)
		s = np.std(nz)
		for j in [m - s, m, m + s]:
			plt.plot([i - 0.1, i + 0.1], [j, j], colors[i])
		plt.text(i + 0.15, m - 0.1, f"$μ$={m:.2f}\n$σ$={s:.2f}", va = "center", fontsize = 5)
		# Display number of points at 0
		if disp0:
			num0 = len(labelData) - len(nz)
			plt.text(i + 0.15, 0, num0, va = "center", fontsize = 5)
	
	#plt.tight_layout()
	savePlot("quasars/" + title)

# Plots the raw quasar data
def plotRaw (quasars):
	title = f"Quasar attribute scatter ($N$ = {len(quasars)}, with{'' if useJHK else 'out'} JHK)"
	labels = ['mag_u', 'mag_g', 'mag_r', 'mag_i', 'mag_z', 'redshift']
	colors = ['b', 'g', 'r', 'm', 'k', 'y']
	if useJHK:
		labels = ['mag_u', 'mag_g', 'mag_r', 'mag_i', 'mag_z', 'mag_J', 'mag_H', 'mag_K', 'redshift']
		colors = ['b', 'g', 'r', 'm', 'k', '0.5', '0.5', '0.5', 'y']
	plotDistr(title, quasars, labels, colors, True)
plotRaw(raw_data)

# Plots the processed quasar data
def plotProcessed (prcQuasars):
	title = f"Processed quasar attributes ($N$ = {len(prcQuasars)}, with{'' if useJHK else 'out'} JHK)"
	labels = range(len(combs))
	dataDict = []
	for i in labels:
		dataDict.append(prcQuasars[:, i])
	colors = ['0.5'] * len(combs)
	plotDistr(title, dataDict, labels, colors)
plotProcessed(featuresPre)
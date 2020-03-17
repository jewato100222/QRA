"""
training.py - Helper script for main.py
This script provides a function to train and test models.
"""
from imports import *

def train (estimator, N, preprocess = False):
	start = time.time()
	
	# Splits the training and testing sections of the data in an 80:20 ratio
	split = model_selection.train_test_split
	featuresArr = features if not preprocess else featuresPre
	featuresCp = np.copy(featuresArr)
	targetsCp = np.copy(targets)
	Xtrain, Xtest, ytrain, ytest = split(featuresCp[:N], targetsCp[:N], test_size = 0.2)

	# If preprocessing, scale data to accomodate feature scaling sensitivity
	if preprocess:
		scaler = preprocessing.StandardScaler()
		scaler.fit(Xtrain) # Make sure to not leak data from test set
		Xtrain = scaler.transform(Xtrain)
		Xtest = scaler.transform(Xtest)

	# Shuffles the data
	np.random.seed()
	newIndices = np.arange(len(Xtrain))
	np.random.shuffle(newIndices)
	Xtrain, ytrain = Xtrain[newIndices], ytrain[newIndices]
	
	# Computes fit and predictions
	estimator.fit(Xtrain, ytrain)
	return {
		'name': estimator.title.split(' (')[0],
		'N': N,
		'preprocess': preprocess,
		'time': time.time() - start,

		'orig': features[len(Xtrain) : N], # The original features recorded for the quasar
		'pred': estimator.predict(Xtest),
		'actual': ytest
	}
"""
models.py - Helper script for main.py
This script holds all the models and parameters that will be used for training.
"""
from imports import *

# All the models that should be trained
models = [
		{
		'name': "k-Neighbors Regressor",
		'class': neighbors.KNeighborsRegressor,
		'preprocess': False,
		'params': {
			'n_neighbors': 10,
			'weights': "distance"
		}
	},
	{
		'name': "SGD Regressor",
		'class': linear_model.SGDRegressor,
		'preprocess': True,
		'params': {
			'loss': "squared_epsilon_insensitive",
			'shuffle': True
		}
	},
	{
		'name': "Ridge Regressor",
		'class': linear_model.Ridge,
		'preprocess': False,
		'params': {}
	},
	{
		'name': "Elastic Net CV",
		'class': linear_model.ElasticNetCV,
		'preprocess': True,
		'params': {
			'normalize': False,
			'cv': 50,
			'max_iter': 10000
		}
	},
	{
		'name': "Random Forest Regressor",
		'class': ensemble.RandomForestRegressor,
		'preprocess': False,
		'params': {}
	},
	# Takes ~1 minute for large N
	{
		'name': "MLP Regressor",
		'class': neural_network.MLPRegressor,
		'preprocess': False,
		'params': {}
	},
	{
		'name': "Gradient Boosting Regressor",
		'class': ensemble.GradientBoostingRegressor,
		'preprocess': False,
		'params': {}
	},
	{
		'name': "Decision Tree Regressor",
		'class': tree.DecisionTreeRegressor,
		'preprocess': True,
		'params': {}
	},
	{
		'name': "Linear SVR",
		'class': svm.LinearSVR,
		'preprocess': True,
		'params': {}
	},
	# Takes ~5 minutes for large N
	{
		'name': "Nu SVR",
		'class': svm.NuSVR,
		'preprocess': True,
		'params': {
			'max_iter': 10000
		}
	}
]
for i in range(len(models)):
	if 'numPoints' not in models[i]:
		# Use these default sample counts for a good range
		models[i]['numPoints'] = [100, 500, 1000, 5000, 20000, 100000]
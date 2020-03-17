"""
main.py
This script pulls together all the other scripts to actually train the models.
The main program is run starting from here.
"""
from imports import *
from models import *
from training import *
from output import *
from plots import *

for model in models:
	for N in model['numPoints']:
		title = f"{model['name']} ($N$ = {N}, preprocess = {model['preprocess']})"
		print(colored("Training " + title, 'blue'))
		# Create the estimator object
		estimator = model['class'](**model['params'])
		estimator.title = title
		results = train(estimator, N, model['preprocess'])
		print(f"Completed in {results['time']:.3f} s")
		# Save and display results
		calcStats(results)
		saveResults(results)
		plotEstimator(model['name'], N, results)
writeOutput()
print(colored("Program completed", 'cyan'))
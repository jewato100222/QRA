"""
clean.py
This script clears all output files created during runtime.
"""
import os
dirs = ["../output", "../plots/estimators", "../plots/quasars"]
for d in dirs:
	for file in os.listdir(d):
		path = os.path.join(d, file)
		os.unlink(path)
print("Cleaned output directories")
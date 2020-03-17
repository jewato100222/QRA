# QRA

## About
![](https://i.imgur.com/BLBRc9w.png)
The QRA Project, which stands for **Quasar Redshift Analysis**, aims to use a variety of machine learning techniques to approach the well-established [phometric redshift](https://en.wikipedia.org/wiki/Photometric_redshift) problem. The project's authors are [Jeffrey Tong](https://github.com/csytrn) and [Matthew Casertano](https://github.com/mcasertano). It was started as a school project and was later submitted to the 2020 ScienceMONTGOMERY Fair under the title "Modeling Quasar Redshift from UGRIZ Light Wavebands with Supervised ML". This repository is an open-source collection of all the code written for the project.

## Installation
The project runs in Python 3.8.2. It uses the following modules (some of them include dependencies), which may need to be manually installed:
- astroML
- itertools
- termcolor
- time

## Usage
All scripts are contained in the `/src` directory. Within the directory, there are 3 scripts that can be run directly:
- main.py: This is the program's main script. It conducts the actual machine learning and produces most of the plots and data files used in the poster.
- quasars.py: This script plots the distributions of the quasar data attributes.
- clean.py: This script clears the output of other scripts.
# NRAO_Interview
[![codecov](https://codecov.io/gh/cvalenzu/NRAO_Interview/branch/master/graph/badge.svg?token=3DE7SQE4Z8)](https://codecov.io/gh/cvalenzu/NRAO_Interview)  [![Build Status](https://travis-ci.com/cvalenzu/NRAO_Interview.svg?token=o75gTmbE8jQjf4RpsqHV&branch=master)](https://travis-ci.com/cvalenzu/NRAO_Interview)

Camilo Valenzuela's NRAO Interview exercise.

A simple script that takes a Spectrogram in CSV, generate plots and estimate the SNR.

## Installation

To install the required packages run:
```
pip install -r requirements.txt
```

Then installing the script is simple

```
pip install .
```

## Using the script

The script is called `nrao_script` it is installed on the python path and can be run in a terminal.

For more information run
```
nrao_script --help
```

## Running test & coverage

The `nrao_script` has a associated package called `nrao_interview`, this package has a `test` module.

To run tests:
```
pip install pytest
pip install coverage
coverage run -m pytest
```

This will generate a `.coverage` file and can be analyzed with
```
coverage report -m
```
showing the test code coverage.


## Some Assumptions

- The code is written for python 3, it will not work on python 2 (Just for some string formatting, is easy to made it compatible).

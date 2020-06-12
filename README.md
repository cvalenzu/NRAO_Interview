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

## Signal to Noise Ratio (SNR) estimation

Using the mean of the frecuencies over time as the
<img src="https://render.githubusercontent.com/render/math?math=P_{signal}"> .

We calculate the mean for each frequency:

<img src="https://render.githubusercontent.com/render/math?math=P_{signal}^k = \frac{1}{T} \displaystyle\sum_{t=0}^T x^k_t ">

Then we calculate the deviation from the mean

<img src="https://render.githubusercontent.com/render/math?math={dev}_t^k = \left|x_t^k  - P_{signal}^k \right|, \forall t \in T">

The deviation will show the noise. Then we calculate the mean of the deviation and we'll get the <img src="https://render.githubusercontent.com/render/math?math=P_{noise}"> .

<img src="https://render.githubusercontent.com/render/math?math=P_{noise}^k = \frac{1}{T} \displaystyle\sum_{t=0}^T dev^k_t ">

We calculate the SNR for each frequency

<img src="https://render.githubusercontent.com/render/math?math=SNR^k = \frac{P_{noise}^k}{P_{noise}^k}, \forall k \in K">

And get the max SNR as the estimate.

<img src="https://render.githubusercontent.com/render/math?math=SNR=\max(SNR^k)">

Example:

The data and signal:

<img src="doc/data.png"><img src="doc/signal.png">

Then we estimate the noise get the mean at each frequency:

<img src="doc/noise.png"> <img src="doc/pnoise.png">

And later the SNR for each frequency:

<img src="doc/snr_all.png">

And a SNR = 27.349


## Other notes

- The code is written for python 3, it will not work on python 2 (Just for some string formatting, is easy to made it compatible).

- In the SNR estimation function if the noise (deviation from the mean) is zero, then it will show a warning an get a `nan` result.

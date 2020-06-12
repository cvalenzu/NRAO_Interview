import os
import unittest
import numpy as np
import glob
from unittest.mock import patch
from nrao_interview.functions import prepare_directory, plot_data, estimate_snr


class TestPlotFunctions(unittest.TestCase):
    """Simple unittest for plotting functions."""

    test_dir = 'test_dir'
    data = np.random.rand(100, 128)

    def setUp(self):
        if os.path.exists(self.test_dir):
            os.rmdir(self.test_dir)
        [os.remove(f) for f in glob.glob("*.pdf")]

    # Checking if the directory is created
    def test_prepare_directory(self):
        not_exists = os.path.exists(self.test_dir)
        assert(not_exists is False)
        prepare_directory(self.test_dir)
        exists = os.path.exists(self.test_dir)
        assert(exists is True)

    # Checking if the plots are created
    @patch("nrao_interview.functions.plt.show")
    def test_plot_frequency_domain(self, mock_show):
        plot_data(self.data, save=False, format='pdf')
        no_save_pdf = len(glob.glob("*.pdf"))
        assert(no_save_pdf == 0)
        plot_data(self.data, save=True, format='pdf')
        save_pdf = len(glob.glob("*.pdf"))
        assert(save_pdf > 0)

    def tearDown(self):
        if os.path.exists(self.test_dir):
            os.rmdir(self.test_dir)
        [os.remove(f) for f in glob.glob("*.pdf")]


class TestSNRFunctions(unittest.TestCase):
    """Test SNR estimation function."""
    dummy = None

    # Creating a dummy signal with a power = 100
    # adding uniform random noise
    def setUp(self):
        np.random.seed(42)
        self.dummy = np.zeros((100, 128))
        self.dummy[:, 44] = 100
        self.dummy = self.dummy + np.random.rand(100, 128)

    # The SNR will be greater than 100
    def testSNREstimation(self):
        snr = estimate_snr(self.dummy)
        assert(snr > 100)

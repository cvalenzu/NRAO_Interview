import os
import unittest
import numpy as np
import glob
from unittest.mock import patch
from nrao_interview.functions import prepare_directory, plot_frequency_domain#, plot_time_domain


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
    def test_plot_time_domain(self, mock_show):
        pass

    # Checking if the plots are created
    @patch("nrao_interview.functions.plt.show")
    def test_plot_frequency_domain(self, mock_show):
        plot_frequency_domain(self.data, save=False, format='pdf')
        no_save_pdf = len(glob.glob("*.pdf"))
        assert(no_save_pdf == 0)
        plot_frequency_domain(self.data, save=True, format='pdf')
        save_pdf = len(glob.glob("*.pdf"))
        assert(save_pdf > 0)

    def tearDown(self):
        if os.path.exists(self.test_dir):
            os.rmdir(self.test_dir)
        [os.remove(f) for f in glob.glob("*.pdf")]

import click
import sys
import os
import numpy as np
import matplotlib.pyplot as plt


def prepare_directory(save_path):
    """Create directory if doesn't exists.

    Parameters
    ----------
    save_path : String
        Path to save plots
    """
    abs_path = os.path.abspath(save_path)
    if not os.path.exists(abs_path):
        os.makedirs(abs_path)


def plot_frequency_domain(data, save=True, save_path='.', format='jpg'):
    """Generate frequency Domain plots.

    Parameters
    ----------
    data : pandas.DataFrame
        Spectra over time (Rows Time, Columns Frequency).
    save : Boolean
        Store the plots in a directory.
    """
    mean = data.mean(axis=0)
    min = data.min(axis=0)
    max = data.max(axis=0)
    frequencies = np.arange(data.shape[1])
    plt.plot(frequencies, mean, label="Mean Power")
    plt.fill_between(frequencies, min, max, alpha=0.2, label="Power Range (Min/Max)")
    plt.title("Mean Spectrogram.")
    plt.xlabel("Frequency [units]")
    plt.ylabel("Power [units]")
    plt.legend()
    if save:
        save_path = os.path.abspath(save_path)
        out_path = os.path.join(save_path, f'freq_plot.{format}')
        plt.savefig(out_path, format=format)
    plt.show()


# def plot_time_domain(data, save=True, save_path='.', format='jpg'):
#     """Generate Time Domain plots.
#
#     Parameters
#     ----------
#     data : pandas.DataFrame
#         Spectra over time (Rows Time, Columns Frequency).
#     save : Boolean
#         Store the plots in a directory.
#     """
#     pass


# def estimate_snr(data):
#     """Estimate the SNR from a spectra over time.
#
#     Parameters
#     ----------
#     data : pandas.DataFrame
#         Spectra over time (Rows Time, Columns Frequency).
#
#     Returns
#     -------
#     float
#         SNR estimate from the data.
#
#     """
#
#     data = data.values
#     mean = data.mean()
#     std = data.std()
#
#     return None

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


def plot_basic(data, snr=None, freq_snr=None):
    """Plot basic information.

    - Raw Data
    - Mean of frequency over time
    - SNR for each frequency

    Parameters
    ----------
    data : pandas.DataFrame
    snr : float
        SNR estimate.
    freq_snr : array
        SNR for each frequency
    Returns
    -------
    matplotlib.figure.Figure
        Figure with plots.
    """

    mean = data.mean(axis=0)
    min = data.min(axis=0)
    max = data.max(axis=0)
    frequencies = np.arange(data.shape[1])
    n_plots = 3 if freq_snr is not None else 2
    fig, axes = plt.subplots(n_plots, 1, sharex=True)
    # Plotting data
    axes[0].matshow(data)
    axes[0].set_aspect('auto')
    axes[0].set_title("Raw Data")
    axes[0].set_ylabel("Time [units]")
    axes[0].set_xlim((0, len(frequencies)))
    # Plotting signal (mean)
    axes[1].plot(frequencies, mean, label="Mean Power")
    axes[1].fill_between(frequencies, min, max, alpha=0.2, label="Power Range (Min/Max)")
    axes[1].set_title("Mean Spectrogram.")
    axes[1].set_ylabel("Power [units]")
    axes[1].legend()
    # Plotting SNR
    if freq_snr is not None:
        title = None if snr is None else f"Max: {snr:.3f}"
        axes[2].plot(frequencies, freq_snr)
        axes[2].set_title(title)
        axes[2].set_ylabel("SNR")

    fig.tight_layout()
    return fig


def plot_data(data, snr=None, freq_snr=None, save=True, save_path='.', format='jpg'):
    """Generate Time and Frequency Domain plots.

    Parameters
    ----------
    data : pandas.DataFrame
        Spectra over time (Rows Time, Columns Frequency).
    snr : float
        SNR estimate.
    freq_snr : array
        SNR for each frequency.
    save : boolean
        Store the plots in a directory.
    save_path : string
        Path to store the plots.
    format : string
        Format given to savefig.
    """

    click.secho("Plotting basic information.", fg='blue')
    fig_basic = plot_basic(data, snr=snr, freq_snr=freq_snr)
    if save:
        save_path = os.path.abspath(save_path)
        click.echo(f"Saving plots into: {save_path}")
        out_path = os.path.join(save_path, f'basic_plots.{format}')
        fig_basic.savefig(out_path, format=format)
    plt.show()


def estimate_snr(data):
    """Estimate the SNR from a spectra over time.

    We assume that the mean over time is the Signal. Then we calculate the
    deviation's mean to get an estimate of the "noise".

    For each frequency we calculate a SNR and then we get the max for the
    whole spectrogram.

    Parameters
    ----------
    data : pandas.DataFrame
        Spectra over time (Rows Time, Columns Frequency).

    Returns
    -------
    tuple (float, array)
        SNR estimate from the data and SNR for each frequency.

    """

    signal = data.mean(0)
    deviation = np.abs(data - signal)
    noise = deviation.mean(axis=0)
    freq_SNR = signal/noise
    SNR = freq_SNR.max()

    return SNR, freq_SNR

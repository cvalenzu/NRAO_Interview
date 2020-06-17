import click
import os
import numpy as np
import matplotlib.pyplot as plt


def prepare_directory(save_path):
    """
    Create directory if doesn't exists.

    Parameters
    ----------
    save_path : String
        Path to save plots.
    """
    abs_path = os.path.abspath(save_path)
    if not os.path.exists(abs_path):
        os.makedirs(abs_path)


def plot_basic(data, snr=None, freq_snr=None):
    """
    Plot basic inplot_formation.

    - Raw Data
    - Mean of frequency over time
    - SNR for each frequency

    Parameters
    ----------
    data : pandas.DataFrame
        DataFrame containing the power
    snr : float
        SNR estimate.
    freq_snr : array
        SNR for each frequency
    Returns
    -------
    matplotlib.figure.Figure
        Figure with plots.
    """
    # Calculating stats
    mean = data.mean(axis=0)
    min_val = data.min(axis=0)
    max_val = data.max(axis=0)

    # Some utils
    frequencies = np.arange(data.shape[1])
    n_plots = 3 if freq_snr is not None else 2

    # Creting plots
    fig, axes = plt.subplots(n_plots, 1, sharex=True)
    # Plotting data
    axes[0].matshow(data)
    axes[0].set_aspect('auto')
    axes[0].set_title("Raw Data")
    axes[0].set_ylabel("Time [units]")
    axes[0].set_xlim((0, len(frequencies)))
    # Plotting signal (mean)
    axes[1].plot(frequencies, mean, label="Mean Power")
    axes[1].fill_between(frequencies, min_val, max_val, alpha=0.2, label="Power Range (Min/Max)")
    axes[1].set_title("Mean Spectrogram.")
    axes[1].set_ylabel("Power [units]")
    axes[1].legend()
    # Plotting SNR
    if freq_snr is not None:
        title = None if snr is None else f"Max: {snr:.3f}"
        axes[2].plot(frequencies, freq_snr)
        axes[2].set_title(title)
        axes[2].set_ylabel("SNR")
    last_ax = n_plots-1
    axes[last_ax].set_xlabel("Frequency [units]")
    fig.suptitle("Basic Inplot_formation")
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    return fig


def plot_over_time(data):
    """
    Generate a plot with the mean power over time.

    Parameters
    ----------
    data : pandas.DataFrame
        DataFrame containing the power

    Returns
    -------
    matplotlib.figure.Figure
        Figure with plots.
    """
    # Getting stats
    mean = data.mean(axis=1)
    min_val = data.min(axis=1)
    max_val = data.max(axis=1)
    frequencies = np.arange(data.shape[0])
    data = np.asarray(data)

    # Plotting
    fig, axes = plt.subplots(2, 1, sharex=True)
    # Plotting data
    axes[0].matshow(data.T)
    axes[0].set_aspect('auto')
    axes[0].set_title("Raw Data")
    axes[0].set_ylabel("Frequency [units]")
    axes[0].set_xlim((0, len(frequencies)))
    # Plotting power over time (mean)
    axes[1].plot(frequencies, mean, label="Mean Power")
    axes[1].fill_between(frequencies, min_val, max_val, alpha=0.2, label="Power Range (Min/Max)")
    axes[1].axhline(data.mean(), ls="--", color="red", label=f"Power Mean {data.mean():.3f}")
    axes[1].set_title("Power over time.")
    axes[1].set_ylabel("Power [units]")
    axes[1].set_xlabel("Time [units]")
    axes[1].legend()
    fig.suptitle("Analysis over time")
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    return fig


def plot_data(data, snr=None, freq_snr=None, show=True, save=True, save_path='.', plot_format='jpg'):
    """
    Generate Time and Frequency Domain plots.

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
    plot_format : string
        plot_format given to savefig.
    """
    click.secho("Plotting basic inplot_formation.", fg='blue')
    fig_basic = plot_basic(data, snr=snr, freq_snr=freq_snr)
    click.secho("Plotting data over time", fg='blue')
    fig_time = plot_over_time(data)

    if save:
        save_path = os.path.abspath(save_path)
        click.echo(f"Saving plots into: {save_path}")
        out_basic_path = os.path.join(save_path, f'basic_plot.{plot_format}')
        fig_basic.savefig(out_basic_path, plot_format=plot_format)

        out_time_path = os.path.join(save_path, f'over_time_plot.{plot_format}')
        fig_time.savefig(out_time_path, plot_format=plot_format)
    if show:
        plt.show()


def estimate_snr(data):
    """
    Estimate the SNR from a spectra over time.

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
    freq_snr = signal/noise
    snr = freq_snr.max()

    return snr, freq_snr

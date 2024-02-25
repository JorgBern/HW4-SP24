import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


def define_distribution(mean, std_dev):
    """
    Define a normal distribution given a mean and standard deviation.

    Parameters:
    mean (float): The mean of the distribution.
    std_dev (float): The standard deviation of the distribution.

    Returns:
    The defined normal distribution.
    """
    dist = stats.norm(loc=mean, scale=std_dev)
    return dist


def calculate_probability(dist, x_value):
    """
    Calculate the cumulative distribution function at a given x_value for a given distribution.

    Parameters:
    dist : The distribution to calculate the probability for.
    x_value (float): The x-value to calculate the cumulative distribution function at.

    Returns:
    float: The calculated probability.
    """
    prob = dist.cdf(x_value)
    return prob


def generate_data(start, end):
    """
    Generate an array of 100 evenly spaced values between a start and end value.

    Parameters:
    start (float): The start of the range.
    end (float): The end of the range.

    Returns:
    numpy.ndarray: The generated array of values.
    """
    x = np.linspace(start, end, 100)
    return x


def create_normal_dist_plot(ax, x, dist, x_value):
    """
    Create a plot of the probability density function of a given distribution.

    Parameters:
    ax (matplotlib.axes.Axes): The axes to plot on.
    x (numpy.ndarray): The x-values to plot.
    dist : The distribution to plot.
    x_value (float): The x-value to fill the area under the curve up to.
    """
    ax.plot(x, dist.pdf(x), 'b-', lw=1, alpha=0.6, label='norm pdf')
    if x_value == 1:
        ax.fill_between(x, dist.pdf(x), where=(x <= x_value), color='0.5', alpha=0.3)
        ax.set_xlim(left=-6)
        ax.set_xlim(right=6)
    else:
        ax.fill_between(x, dist.pdf(x), where=(x >= x_value), color='0.5', alpha=0.3)
        ax.set_xlim(left=160)
        ax.set_xlim(right=190)
    ax.set_ylabel('f(x)')
    ax.xaxis.tick_top()
    ax.yaxis.tick_right()
    ax.tick_params(axis='x', direction='in', which='both', top=True, bottom=True, labelbottom=False, labeltop=False)
    ax.tick_params(axis='y', direction='in', which='both', left=True, right=True, labelleft=True, labelright=False)
    ax.set_ylim(bottom=0)


def create_standardized_dist_plot(ax, x, dist, x_value):
    """
    Create a plot of the cumulative distribution function of a given distribution.

    Parameters:
    ax (matplotlib.axes.Axes): The axes to plot on.
    x (numpy.ndarray): The x-values to plot.
    dist : The distribution to plot.
    x_value (float): The x-value to draw a vertical line at.
    """
    ax.plot(x, dist.cdf(x), 'b-', lw=1, alpha=0.6, label='norm cdf')
    ax.axvline(x=x_value, color='k', linestyle='-')
    ax.axhline(y=dist.cdf(x_value), color='k', linestyle='-')
    ax.scatter(x_value, dist.cdf(x_value), color='r')
    ax.set_ylabel('£(x)')
    ax.set_xlabel('x')
    ax.xaxis.tick_top()
    ax.yaxis.tick_right()
    ax.tick_params(axis='x', direction='in', which='both', top=True, bottom=True, labelbottom=True, labeltop=False)
    ax.tick_params(axis='y', direction='in', which='both', left=True, right=True, labelleft=True, labelright=False)
    ax.set_ylim(top=1)
    ax.set_ylim(bottom=0)
    if x_value == 1:
        ax.set_xlim(left=-6)
        ax.set_xlim(right=6)
    else:
        ax.set_xlim(left=160)
        ax.set_xlim(right=190)


def main():
    """
    Main function to define distributions, calculate probabilities, generate data, and create plots.
    """
    # Define means and standard deviations
    mean1, std_dev1 = 0, 1
    mean2, std_dev2 = 175, 3
    x1 = 1
    x2 = mean2 + std_dev2*2

    # Define distributions
    dist1 = define_distribution(mean1, std_dev1)
    dist2 = define_distribution(mean2, std_dev2)

    # Calculate probabilities
    prob1 = calculate_probability(dist1, x1)
    prob2 = 1-calculate_probability(dist2, x2)

    # Print probabilities
    print(f'Probability for distribution N({mean1},{std_dev1}): {prob1}')
    print(f'Probability for distribution N({mean2},{std_dev2}): {prob2}')

    # Generate data
    xscale = generate_data(-6, 6)
    xscale2 = generate_data(160, 190)

    # Create subplots
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))

    # Create plots
    create_normal_dist_plot(axs[0, 0], xscale, dist1, x1)
    create_normal_dist_plot(axs[0, 1], xscale2, dist2, x2)
    create_standardized_dist_plot(axs[1, 0], xscale, dist1, x1)
    create_standardized_dist_plot(axs[1, 1], xscale2, dist2, x2)

    # Show plots
    plt.show()


if __name__ == "__main__":
    main()







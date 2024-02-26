#ChatGPT was used to help write this code
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


def define_distribution(mean, std_dev):
    '''
    This function creates a normal distribution using the stat.norm function from scipy, it takes in the mean
    the standard deviation for each problem and uses them to create the distribution for each.

    Parameters:
    Mean(float): The mean of the distribution.
    std_dev(float): The standard deviation of the distributions.

    Returns:
    The defined normal distribution.
    '''
    dist = stats.norm(loc=mean, scale=std_dev)
    return dist


def calculate_probability(dist, x_value):
    '''
    Calculate the probability that a random variable is less than
    or equal to a given value. This works perfectly for the first problem since it requires for the probability of
    values less than 1, but for the second one, it requires values greater than 181, to account for this
    later we do 1-prob for the second problem to get the correct value.

    This function uses the cumulative distribution function (CDF) of the distribution
    to calculate the probability.
    :param dist: A continuous random variable represent the distribution.
    :param x_value (float):The value for which to calculate the probability.
    :return: The probability that the random value is less than or equal to the x value.
    '''
    prob = dist.cdf(x_value)
    return prob


def generate_data(start, end):
    '''
    Generates an array of evenly spaced numbers over a specified range.

    This function uses the numpy linspace function to generate an array of 100 evenly spaced
    numbers between a start and end value . I chose 100 because changing it to a higher value, did not affect
    the look of the plots.
    :param start: The start of the interval range.
    :param end: The end of the interval range.
    :return: The array of 100 evenly spaced numbers over the interval.
    '''
    x = np.linspace(start, end, 100)
    return x


def create_normal_dist_plot(ax, x, dist, x_value, mean, std_dev, xytext, xy):
    '''
    This function plots a normal distribution curve using the pdf function from scipy and shades the
    area under the curve based on the x value. There is an if statement is there since both problems
    are being sent to this function, it detects if the x value is 1, if it is, it shades the area before it, if is not 1
    it shades the area after it.

    A lot of this code is just dedicated to the formatting of the graph
    :param ax: The axes to draw the plot on the plot.
    :param x: The x-coordinates for the points on the plot
    :param dist: The normal distribution of the plot.
    :param x_value: The x value at which to shade the area under the curve
    :param mean: The mean of the normal distribution
    :param std_dev: The standard deviation of the normal distribution
    :param xytext: The position to place the text annotation on the plot.
    :param xy: The position to point the arrow annotation to on the plot
    :return: none
    '''
    # Plot the normal distribution
    ax.plot(x, dist.pdf(x), 'b-', lw=1, alpha=0.6, label='norm pdf')
    # Check if the value is 1, for the first problem
    if x_value == 1:
        # Annotate the plot with the probability and an arrow that points at the x-value
        ax.annotate(f'P(x<{x_value}|N({mean},{std_dev}))={dist.cdf(x_value):.2f}', xy=xy, xytext=xytext, arrowprops=dict(facecolor='black', shrink=0.05),fontsize=8)
        ax.fill_between(x, dist.pdf(x), where=(x <= x_value), color='0.5', alpha=0.3)
        # Shade the area under tje curve to the left of the x_value
        ax.set_xlim(left=-6) #These are the x limits of the chart, these were chosen to match the example from the example.
        ax.set_xlim(right=6)
    else:
        # Shade the area under the curve to the right of the x_value
        ax.fill_between(x, dist.pdf(x), where=(x >= x_value), color='0.5', alpha=0.3)
        # Shows the probability along with an arrow pointing at the x value, 1-CDF to get the correct probability.
        ax.annotate(f'P(x>{x_value}|N({mean},{std_dev}))={1 - dist.cdf(x_value):.2f}', xy=xy, xytext=xytext, arrowprops=dict(facecolor='black', shrink=0.05),fontsize=8)
        ax.set_xlim(left=160) # Sets the limits to this to match the example
        ax.set_xlim(right=190)
    # Annotate the plot with the formula for the normal distribution, uses LaTex to show accurately
    ax.annotate(r'$f(x)={\frac {1}{\sigma {\sqrt {2\pi }}}}e^{-{\frac {1}{2}}\left({\frac {x-\mu }{\sigma }}\right)^{2}}$',xy=(0.04, 0.8), xycoords='axes fraction', fontsize=8)
    # Set the y-axis label
    ax.set_ylabel('f(x)')
    # Add ticks to the top of the plot
    ax.xaxis.tick_top()
    # Add ticks to the right of the plot
    ax.yaxis.tick_right()
    # Set the tick parameters for the x-axis and y-axis
    ax.tick_params(axis='x', direction='in', which='both', top=True, bottom=True, labelbottom=False, labeltop=False)
    ax.tick_params(axis='y', direction='in', which='both', left=True, right=True, labelleft=True, labelright=False)
    ax.set_ylim(bottom=0)


def create_standardized_dist_plot(ax, x, dist, x_value):
    '''
    This function plots the standardized normal distribution S-curve using the cumulative distribution function
    of the normal distribution and marks the specified x_value on the plot.
    :param ax: The axes to be drawn the plot on.
    :param x: The x-coordinates for the points on the plot.
    :param dist: The normal distribution to plot
    :param x_value: The x-value to mark on the plot
    :return: none
    '''
    # Plot the CDF
    ax.plot(x, dist.cdf(x), 'b-', lw=1, alpha=0.6, label='norm cdf')
    # Draw a vertical line at the x_value
    ax.axvline(x=x_value, color='k', linestyle='-')
    # Draw a horizontal line at the CDF of the x_value
    ax.axhline(y=dist.cdf(x_value), color='k', linestyle='-')
    # Place a red dot at the intersection of the vertical and horizontal line
    ax.scatter(x_value, dist.cdf(x_value), color='r')
    # Set the y-axis, uses Latex to successfully write the cdf equation
    ax.set_ylabel('$\Phi(x)=\int_{-\infty}^{x} f(x)dx$')
    # Sets the x-axis
    ax.set_xlabel('x')
    # Adds ticks to the top
    ax.xaxis.tick_top()
    # Adds ticks to the bttom
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
    '''
    This program calculates probabilities of chosen x values for two normal distributions and creates 4 plots.
    It does not take user input, if values are changed they have to be changed in the code, but they are tied in so it
    is an easy process. The mean1, std_dev1, and x1 correspond to the first problem and mean2, std_Dev2,and x2 correspond
    to the second problem.
    - The two top plots are the normal distributions of each problem with the areas under the curve shaded based on the
    x-values
    - Two plots at the bottom are based on the standardized normal distribution using the CDF function with the x-value
    marked
    :return:None
    '''
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
    # It does 1-prob to correctly get the correct probability of part 2

    # Print probabilities
    print(f'Probability for distribution N({mean1},{std_dev1}) being less than 1: {prob1}')
    print(f'Probability for distribution N({mean2},{std_dev2}) being more than 181: {prob2}')

    # Generate data
    xscale = generate_data(-6, 6)
    xscale2 = generate_data(160, 190)

    # Create subplots
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))

    # Create plots
    create_normal_dist_plot(axs[0, 0], xscale, dist1, x1, mean1, std_dev1, (x1-6.5, 0.1), (x1, 0))
    create_normal_dist_plot(axs[0, 1], xscale2, dist2, x2, mean2, std_dev2, (x2-2.5, 0.07), (x2+0.3, 0.01))

    create_standardized_dist_plot(axs[1, 0], xscale, dist1, x1)
    create_standardized_dist_plot(axs[1, 1], xscale2, dist2, x2)

    # Show plots
    plt.show()


if __name__ == "__main__":
    main()







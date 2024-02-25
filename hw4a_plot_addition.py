import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def define_distribution(mean, std_dev):
    dist = stats.norm(loc=mean, scale=std_dev)
    return dist

def calculate_probability(dist, x_value):
    prob = dist.cdf(x_value)
    return prob

def generate_data(start, end):
    x = np.linspace(start, end, 100)
    return x

def create_normal_dist_plot(ax, x, dist, x_value, mean, std_dev, xytext, xy):
    ax.plot(x, dist.pdf(x), 'b-', lw=1, alpha=0.3)
    if x_value == 1:
        ax.annotate(f'P(x<{x_value}|N({mean},{std_dev}))={dist.cdf(x_value):.2f}', xy=xy, xytext=xytext, arrowprops=dict(facecolor='black', shrink=0.05))
        ax.fill_between(x, dist.pdf(x), where=(x <= x_value), color='0.5', alpha=0.3)
        ax.set_xlim(left=-6)
        ax.set_xlim(right=6)
    else:
        ax.annotate(f'P(x>{x_value}|N({mean},{std_dev}))={1 - dist.cdf(x_value):.2f}', xy=xy, xytext=xytext, arrowprops=dict(facecolor='black', shrink=0.05))
        ax.fill_between(x, dist.pdf(x), where=(x >= x_value), color='0.5', alpha=0.3)
        ax.set_xlim(left=160)
        ax.set_xlim(right=190)
    ax.set_ylabel('f(x)')
    ax.xaxis.tick_top()
    ax.yaxis.tick_right()
    ax.tick_params(axis='x', direction='in', which='both', top=True, bottom=True, labelbottom=False, labeltop=False)
    ax.tick_params(axis='y', direction='in', which='both', left=True, right=True, labelleft=True, labelright=False)
    ax.set_ylim(bottom=0)




def create_standardized_dist_plot(ax, x, dist, x_value, mean, std_dev):
    ax.plot(x, dist.cdf(x), 'b-', lw=1, alpha=0.6)
    ax.axvline(x=x_value, color='k', linestyle='-')
    ax.axhline(y=dist.cdf(x_value), color='k', linestyle='-')
    ax.scatter(x_value, dist.cdf(x_value), color='r')
    ax.set_ylabel('$\Phi(x)=\int_{-\infty}^{x} f(u)du$')
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
    # Define means and standard deviations
    mean1, std_dev1 = 0, 1
    mean2, std_dev2 = 175, 3
    x1 = -0.5
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
    xscale = generate_data(-10, 10)
    xscale2 = generate_data(160, 190)
    # Create subplots
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))

    # Create plots
    # xytext is the location of the equation
    # xy is the location of the tip of the arrow.
    create_normal_dist_plot(axs[0, 0], xscale, dist1, x1, mean1, std_dev1, (x1-3, 0.1), (x1, 0))
    create_normal_dist_plot(axs[0, 1], xscale2, dist2, x2, mean2, std_dev2, (x2+0.5, 0.03), (x2+0.8, 0.01))


    create_standardized_dist_plot(axs[1, 0], xscale, dist1, x1, mean1, std_dev1)
    create_standardized_dist_plot(axs[1, 1], xscale2, dist2, x2, mean2, std_dev2)
    # Show plots
    plt.show()

if __name__ == "__main__":
    main()

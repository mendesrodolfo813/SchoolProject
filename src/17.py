import numpy as np
from scipy.stats import norm

def calculate_pdf(x):
    # This function calculates the probability density function of the normal distribution.
    if x <= 0 or x >= 10:
        return 0
    else:
        return norm.pdf(x, loc=0.0, scale=np.sqrt(1.0 / 5.0))

def main():
    # Main code to execute random number generation and probability density calculation
    n = 1000
    x = np.random.normal(loc=0.0, scale=1.0, size=n)
    pdf = calculate_pdf(x)
    
    print("Random sample from normal distribution:", x)
    print("Probability Density Function of the Normal Distribution:", pdf)

if __name__ == "__main__":
    main()

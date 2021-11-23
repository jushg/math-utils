from distributions.binomial import binomial
from distributions.chi_square import chi_sq
from distributions.exponential import exponential
from distributions.f import f
from distributions.negative_binomial import neg_binomial
from distributions.normal import normal
from distributions.poisson import poisson
from distributions.t import t
import statistics

def sample_params(sample_points):
    print(f"Sample points: " + str(sample_points))
    print(f"Number of sample points n = {len(sample_points)}")
    print(f"Sample mean mu = {statistics.mean(sample_points)}")
    print(f"Sample standard deviation s = {statistics.stdev(sample_points)}")
    print(f"Sample variance s^2 = {statistics.variance(sample_points)}")


# test code
b = exponential(1)
b.left_cdf(1)

samples = [3.2,-1.5,0.7,5.9,-3.7,8.9,17,8]
sample_params(samples)

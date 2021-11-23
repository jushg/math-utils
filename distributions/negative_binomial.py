from scipy import stats


class neg_binomial:

    def __init__(self, k, p):
        self.k = k
        self.p = p

    def left_cdf(self, target):
        print(f"Pr(X <= {target}) = {stats.nbinom.cdf(target - self.k, self.k, self.p)}")

    def pmf(self, target):
        print(f"Pr(X = {target}) = {stats.nbinom.pmf(target - self.k, self.k, self.p)}")

    def right_cdf(self, target):
        print(f"Pr(X > {target}) = {1 - stats.nbinom.cdf(target - self.k, self.k, self.p)}")

    def ppf(self, target):
        print(f"Pr(X <= {stats.nbinom.ppf(target, self.k, self.p) + self.k}) >= {target}")

    def __str__(self):
        return f"Negative Binomial Distribution\nX: number of trials, with k = {self.k} success required and prob of success p = {self.p}" \
               + f"\nE(X) = k/p =  {self.k / self.p}; V(X) = k(1-p)/p^2 = {self.k * (1 - self.p)/(self.p**2)}"

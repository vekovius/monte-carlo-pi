# Monte Carlo Estimation of Pi

Estimating pi using Monte Carlo simulation and verifying the Central Limit Theorem on the sampling distribution of the estimator.

## How It Works

Random points (x, y) are sampled uniformly in the unit square [0, 1] x [0, 1]. Points satisfying x^2 + y^2 <= 1 fall inside the quarter-circle of radius 1. Since the quarter-circle has area pi/4:

```
pi = 4 * (points inside circle) / n
```

## What the Script Does

1. **Basic estimation** -- estimates pi at n = 100, 1000, 10000, 100000
2. **Convergence study** -- sweeps n from 100 to 1,000,000 on a log scale and plots how the estimate converges (error ~ 1/sqrt(n))
3. **CLT verification** -- runs 500 independent experiments at n = 1000, 10000, 100000; plots histograms against the theoretical normal distribution and Q-Q plots; runs Shapiro-Wilk normality tests

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
python monte_carlo_pi.py
```

Outputs printed to the console and two plots saved to the working directory:
- `pi_convergence.png` -- estimate vs. sample size
- `sampling_distributions.png` -- histograms + Q-Q plots for CLT verification

## Sample Output

```
n =    100: pi ~ 3.120000, error = 0.021593
n =   1000: pi ~ 3.164000, error = 0.022407
n =  10000: pi ~ 3.153200, error = 0.011607
n = 100000: pi ~ 3.139280, error = 0.002313
```

## Key Results

- Error decreases proportionally to 1/sqrt(n)
- The sampling distribution is approximately normal even at n = 1,000
- Normality strengthens as n increases, confirming the CLT
- Theoretical std = sqrt(pi(4 - pi) / n) matches empirical observations

## Dependencies

- numpy, matplotlib, scipy

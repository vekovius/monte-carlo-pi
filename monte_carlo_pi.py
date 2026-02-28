import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def estimate_pi(n):

    # Generate random points in unit square
    x = np.random.uniform(0, 1, n)
    y = np.random.uniform(0, 1, n)
    
    # Count points inside quarter-circle
    inside_circle = (x**2 + y**2) <= 1
    points_inside = np.sum(inside_circle)
    
    # Estimate π using the ratio
    pi_estimate = 4 * points_inside / n
    
    return pi_estimate


def convergence_study():

    # Create logarithmic range of n values to test
    n_values = np.logspace(2, 6, 50).astype(int)
    pi_estimates = []
    
    np.random.seed(42)  # Set seed for reproducibility
    
    print("Testing convergence with different sample sizes...")
    for n in n_values:
        pi_est = estimate_pi(n)
        pi_estimates.append(pi_est)
        # Print key milestones (AI assisted with formatted output)
        if n in [100, 1000, 10000, 100000, 1000000]:
            error = abs(pi_est - np.pi)
            print(f"n = {n:7d}: π ≈ {pi_est:.6f}, error = {error:.6f}")
    
    # Create convergence plot
    plt.figure(figsize=(10, 6))
    plt.semilogx(n_values, pi_estimates, 'b-', alpha=0.7, label='π estimates')
    plt.axhline(y=np.pi, color='r', linestyle='--', linewidth=2, label=f'True π = {np.pi:.6f}')
    plt.xlabel('Number of samples (n)', fontsize=12)
    plt.ylabel('Estimated π', fontsize=12)
    plt.title('Convergence: π Estimates vs Sample Size', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=10)
    plt.ylim(2.8, 3.5)
    plt.tight_layout()
    plt.savefig('pi_convergence.png', dpi=300, bbox_inches='tight')
    print("Saved: pi_convergence.png")
    plt.show()


def sampling_distribution_study():
 
    # Parameters
    n_values = [1000, 10000, 100000]
    R = 500  # Number of repetitions for each n
    
    # Set up figure with 2 rows and 3 columns
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Sampling Distribution of π Estimator (Central Limit Theorem)', fontsize=16)
    
    for i, n in enumerate(n_values):
        print(f"\nAnalyzing n = {n}:")
        
        # Run R independent experiments
        np.random.seed(123)
        pi_estimates = np.array([estimate_pi(n) for _ in range(R)])
        
        # Calculate sample statistics
        sample_mean = np.mean(pi_estimates)
        sample_std = np.std(pi_estimates, ddof=1)
        
        # Calculate theoretical values from CLT
        theoretical_mean = np.pi
        theoretical_std = np.sqrt(np.pi * (4 - np.pi) / n)
        
        print(f"  Sample mean: {sample_mean:.6f} (theoretical: {theoretical_mean:.6f})")
        print(f"  Sample std:  {sample_std:.6f} (theoretical: {theoretical_std:.6f})")
        
        # Create histogram (AI assisted with styling)
        ax_hist = axes[0, i]
        ax_hist.hist(pi_estimates, bins=30, density=True, alpha=0.7, 
                    color='skyblue', edgecolor='black')
        
        # Overlay theoretical normal distribution curve
        x_range = np.linspace(pi_estimates.min(), pi_estimates.max(), 100)
        normal_curve = stats.norm.pdf(x_range, theoretical_mean, theoretical_std)
        ax_hist.plot(x_range, normal_curve, 'r-', linewidth=2, 
                    label=f'N({theoretical_mean:.3f}, {theoretical_std:.4f}²)')
        
        # Add reference lines
        ax_hist.axvline(np.pi, color='red', linestyle='--', alpha=0.8, label='True π')
        ax_hist.set_xlabel('π estimate')
        ax_hist.set_ylabel('Density')
        ax_hist.set_title(f'n = {n}')
        ax_hist.legend(fontsize=8)
        ax_hist.grid(True, alpha=0.3)
        
        # Create Q-Q plot to assess normality
        ax_qq = axes[1, i]
        stats.probplot(pi_estimates, dist="norm", plot=ax_qq)
        ax_qq.set_title(f'Q-Q Plot (n = {n})')
        ax_qq.grid(True, alpha=0.3)
        
        # Perform Shapiro-Wilk normality test (AI assisted)
        shapiro_stat, shapiro_p = stats.shapiro(pi_estimates)
        print(f"  Shapiro-Wilk: statistic = {shapiro_stat:.4f}, p-value = {shapiro_p:.4f}")
        if shapiro_p > 0.05:
            print(f"  → Fail to reject normality (p > 0.05)")
        else:
            print(f"  → Reject normality (p ≤ 0.05)")
    
    plt.tight_layout()
    plt.savefig('sampling_distributions.png', dpi=300, bbox_inches='tight')
    print("\nSaved: sampling_distributions.png")
    plt.show()


def main():
    # Main function - runs all three parts of the analysis.
    print("=" * 50)
    print("Monte Carlo π Estimation Project")
    print("=" * 50)
    print(f"True value of π = {np.pi:.10f}\n")
    
    # Part 1: Basic Monte Carlo estimation
    print("Part 1: Monte Carlo π Estimator")
    print("-" * 50)
    np.random.seed(42)
    for n in [100, 1000, 10000, 100000]:
        pi_est = estimate_pi(n)
        error = abs(pi_est - np.pi)
        print(f"n = {n:6d}: π ≈ {pi_est:.6f}, |error| = {error:.6f}")
    
    # Part 2: Convergence study
    print("\n" + "=" * 50)
    print("Part 2: Convergence with Sample Size")
    print("-" * 50)
    convergence_study()
    
    # Part 3: Sampling distribution (CLT verification)
    print("\n" + "=" * 50)
    print("Part 3: Sampling Distribution and Central Limit Theorem")
    print("-" * 50)
    sampling_distribution_study()
    
    print("\n" + "=" * 50)
    print("Analysis complete!")
    print("Generated files:")
    print("  - pi_convergence.png")
    print("  - sampling_distributions.png")
    print("=" * 50)


if __name__ == "__main__":
    main()

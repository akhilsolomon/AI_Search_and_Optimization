import matplotlib.pyplot as plt
import csv
import os

def load_csv(filepath):
    runs, costs, times = [], [], []
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            runs.append(int(row['run']))
            costs.append(float(row['cost']))
            times.append(float(row['time_seconds']))
    return runs, costs, times

def plot_results():
    # Load results
    hc_runs, hc_costs, hc_times = load_csv("results/hc_results.csv")
    sa_runs, sa_costs, sa_times = load_csv("results/sa_results.csv")

    # Create output directory if not exists
    os.makedirs("results/plots", exist_ok=True)

    # Plot: Cost vs Time
    plt.figure(figsize=(10, 5))
    plt.plot(hc_times, hc_costs, 'o-', label='Hill Climbing', color='blue')
    plt.plot(sa_times, sa_costs, 'o-', label='Simulated Annealing', color='orange')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Tour Cost')
    plt.title('Cost vs Time for TSP Solvers')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("results/plots/cost_vs_time.png")
    plt.close()
    print("✅ Saved plot: results/plots/cost_vs_time.png")

if __name__ == "__main__":
    plot_results()

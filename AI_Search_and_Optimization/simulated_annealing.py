import argparse
import time
import math
import random
from tsp_env import TSPEnv
from utils import run_experiment, save_results


def simulated_annealing(env, timeout, initial_temp, alpha):
    """
    SA with exponential cooling: T <- T * alpha each step.
    Accept worse moves with probability exp(-Δ/T).
    """
    current = env.random_solution()
    best = current.copy()
    current_cost = env.cost(current)
    best_cost = current_cost
    T = initial_temp
    start = time.time()

    while (time.time() - start) < timeout and T > 1e-3:
        # pick a random 2-swap neighbor
        i, j = random.sample(range(env.n), 2)
        neighbor = current.copy()
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
        c = env.cost(neighbor)
        delta = c - current_cost
        if delta < 0 or random.random() < math.exp(-delta / T):
            current, current_cost = neighbor, c
            if c < best_cost:
                best, best_cost = neighbor.copy(), c
        T *= alpha

    return best, best_cost


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--problem', required=True,
                        help='Path to .tsp file')
    parser.add_argument('--runs', type=int, default=5)
    parser.add_argument('--timeout', type=int, default=600,
                        help='Timeout per run (seconds)')
    parser.add_argument('--temp', type=float, default=1000,
                        help='Initial temperature')
    parser.add_argument('--alpha', type=float, default=0.995,
                        help='Cooling rate')
    parser.add_argument('--output', default='results/sa_results.csv',
                        help='CSV output path')
    args = parser.parse_args()

    env = TSPEnv(args.problem)
    # wrap SA to match run_experiment signature
    def run_sa(e, timeout):
        return simulated_annealing(e, timeout, args.temp, args.alpha)

    results = run_experiment(run_sa, env, args.runs, args.timeout)
    save_results(results, args.output)
    print(f"Simulated Annealing: saved results to {args.output}")


if __name__ == '__main__':
    main()
import argparse
import time
from tsp_env import TSPEnv
from utils import run_experiment, save_results


def hill_climbing(env, timeout):
    """
    Greedy hill climbing: swap two cities if it improves cost.
    Stop when no improvement or timeout.
    """
    current = env.random_solution()
    best_cost = env.cost(current)
    start = time.time()
    improved = True
    while improved and (time.time() - start) < timeout:
        improved = False
        for neighbor in env.neighbors(current):
            c = env.cost(neighbor)
            if c < best_cost:
                current, best_cost = neighbor, c
                improved = True
                break
    return current, best_cost


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--problem', required=True,
                        help='Path to .tsp file')
    parser.add_argument('--runs', type=int, default=5)
    parser.add_argument('--timeout', type=int, default=600,
                        help='Timeout per run (seconds)')
    parser.add_argument('--output', default='results/hc_results.csv',
                        help='CSV output path')
    args = parser.parse_args()

    env = TSPEnv(args.problem)
    results = run_experiment(hill_climbing, env, args.runs, args.timeout)
    save_results(results, args.output)
    print(f"Hill Climbing: saved results to {args.output}")


if __name__ == '__main__':
    main()
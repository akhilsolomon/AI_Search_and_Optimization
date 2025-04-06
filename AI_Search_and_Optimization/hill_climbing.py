import argparse
from tsp_env import TSPEnv
from utils import run_experiment, save_results
import os

def hill_climbing(env, timeout, capture=None):
    import time
    start_time = time.time()
    current = env.random_solution()
    best_cost = env.cost(current)

    if capture: capture(current, best_cost)

    while time.time() - start_time < timeout:
        improved = False
        for neighbor in env.neighbors(current):
            cost = env.cost(neighbor)
            if cost < best_cost:
                current, best_cost = neighbor, cost
                improved = True
                if capture: capture(current, best_cost)
                break
        if not improved:
            break
    return current, best_cost

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--problem", type=str, required=True)
    parser.add_argument("--runs", type=int, default=5)
    parser.add_argument("--timeout", type=int, default=30)
    args = parser.parse_args()

    env = TSPEnv(args.problem)
    gif_dir = "gifs/hc"
    os.makedirs(gif_dir, exist_ok=True)

    results = run_experiment(
        hill_climbing, env, runs=args.runs, timeout=args.timeout, gif_dir=gif_dir
    )
    save_results(results, "results/hc_results.csv")

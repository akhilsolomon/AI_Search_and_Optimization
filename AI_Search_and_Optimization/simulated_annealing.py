import argparse
from tsp_env import TSPEnv
from utils import run_experiment, save_results
import os
import math
import random
import time

def simulated_annealing(env, timeout, capture=None):
    start_time = time.time()
    current = env.random_solution()
    current_cost = env.cost(current)

    T = 100.0
    T_min = 1e-3
    alpha = 0.995

    if capture:
        capture(current, current_cost)

    while T > T_min and time.time() - start_time < timeout:
        neighbor = random.choice(list(env.neighbors(current)))
        neighbor_cost = env.cost(neighbor)
        delta = neighbor_cost - current_cost

        if delta < 0 or random.random() < math.exp(-delta / T):
            current = neighbor
            current_cost = neighbor_cost
            if capture:
                capture(current, current_cost)

        T *= alpha

    return current, current_cost

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--problem", type=str, required=True)
    parser.add_argument("--runs", type=int, default=5)
    parser.add_argument("--timeout", type=int, default=30)
    args = parser.parse_args()

    env = TSPEnv(args.problem)
    gif_dir = "gifs/sa"
    os.makedirs(gif_dir, exist_ok=True)

    results = run_experiment(
        simulated_annealing, env, runs=args.runs, timeout=args.timeout, gif_dir=gif_dir
    )
    save_results(results, "results/sa_results.csv")

import time
import csv
import os
import matplotlib.pyplot as plt
import numpy as np
import imageio

def run_experiment(func, env, runs, timeout, gif_dir=None):
    results = []

    for run in range(1, runs + 1):
        frames = []

        def capture(path, cost):
            fig, ax = plt.subplots()
            coords = env.coords
            x = [coords[i][0] for i in path + [path[0]]]
            y = [coords[i][1] for i in path + [path[0]]]
            ax.plot(x, y, 'o-', label=f"Cost: {cost:.2f}")
            ax.set_title(f'Run {run}')
            ax.legend()
            fig.canvas.draw()
            img = np.frombuffer(fig.canvas.buffer_rgba(), dtype=np.uint8)
            img = img.reshape(fig.canvas.get_width_height()[::-1] + (4,))
            frames.append(img)
            plt.close(fig)

        sol, cost = func(env, timeout, capture=capture if gif_dir else None)
        if gif_dir:
            gif_path = os.path.join(gif_dir, f"run{run}.gif")
            imageio.mimsave(gif_path, frames, fps=2)
            print(f"Saved GIF: {gif_path}")
        elapsed = timeout  # approx, since we use time.time() inside the func
        results.append((run, cost, elapsed))

    return results

def save_results(results, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['run', 'cost', 'time_seconds'])
        for row in results:
            writer.writerow(row)


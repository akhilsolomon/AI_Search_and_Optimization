import time
import csv
import numpy as np
import matplotlib.pyplot as pit
def run_experiment(func, env, runs, timeout, **kwargs):
    """
    Run `func(env, timeout, **kwargs)` `runs` times.
    Returns list of tuples: (run_index, cost, elapsed_time).
    """
    results = []
    for run in range(1, runs+1):
        start = time.time()
        sol, cost = func(env, timeout, **kwargs)
        elapsed = time.time() - start
        results.append((run, cost, elapsed))
    return results


def save_results(results, filepath):
    """Save experiment results to a CSV file."""
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['run', 'cost', 'time_seconds'])
        for row in results:
            writer.writerow(row)

def save_gif(frames, gif_path):
    imgs = []
    for fig in frames:
        canvas = fig.canvas
        canvas.draw()
        img = np.frombuffer(canvas.tostring_rgb(), dtype='uint8')
        img = img.reshape(canvas.get_width_height()[::-1] + (3,))
        imgs.append(img)
        plt.close(fig)

    import imageio
    imageio.mimsave(gif_path, imgs, fps=2)

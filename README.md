# 🧠 AI Search and Optimization – Assignment 2

This project implements two metaheuristic algorithms to solve the **Traveling Salesman Problem (TSP)**:

- 🧗 Hill Climbing
- ❄️ Simulated Annealing

It visualizes each optimization run as GIFs, records performance results in CSV files, and plots a comparison graph of **Cost vs Time**.

---

## Project Structure

```
assignment2/
├── berlin52.tsp                # Input TSP file
├── hill_climbing.py            # Hill Climbing implementation
├── simulated_annealing.py      # Simulated Annealing implementation
├── tsp_env.py                  # TSP environment and utility functions
├── utils.py                    # Core utilities: experiment runner, saving, GIF generator
├── plot_results.py             # Generates comparison plot
│
├── results/
│   ├── hc_results.csv          # Hill Climbing results
│   ├── sa_results.csv          # Simulated Annealing results
│   └── plots/
│       └── cost_vs_time.png    # Cost vs Time graph
│
└── gifs/
    ├── hc/
    │   ├── run_1.gif
    │   └── ...
    └── sa/
        ├── run_1.gif
        └── ...
```

---

## Requirements

Make sure you have Python 3.10+ installed, then install the required libraries:

```bash
pip install numpy matplotlib imageio
```

---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/akhilsolomon/AI_Search_and_Optimization.git
cd AI_Search_and_Optimization/assignment2
```

### 2. Run Hill Climbing
```bash
python3 hill_climbing.py --problem berlin52.tsp --runs 5 --timeout 60
```
-  Generates `gifs/hc/` with visualizations
-  Results saved to `results/hc_results.csv`

### 3. Run Simulated Annealing
```bash
python3 simulated_annealing.py --problem berlin52.tsp --runs 5 --timeout 60
```
-  Generates `gifs/sa/` with visualizations
-  Results saved to `results/sa_results.csv`

### 4. Plot Comparison Graph
```bash
python plot_results.py
```
-  Saves plot to `results/plots/cost_vs_time.png`

---

##  Output Summary

- **GIFs**: Visualizes how the tour evolves for each algorithm.
- **CSV Files**: Record of costs and times for each run.
- **PNG Plot**: Visual comparison of HC vs SA performance.

---

##  Notes

- You can adjust number of runs and timeout using `--runs` and `--timeout` arguments.
- Make sure `berlin52.tsp` (or your own `.tsp` file) is placed in the working directory.
- You can increase timeout to observe longer optimization paths and better results.

---

## 👨‍💻 Author

- **Akhil Solomon**
- GitHub: [akhilsolomon](https://github.com/akhilsolomon)

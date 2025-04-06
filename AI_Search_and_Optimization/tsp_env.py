import math

class TSPEnv:
    """
    Wraps a TSPLIB-style .tsp file with EUC_2D coords.
    Parses NODE_COORD_SECTION and builds a distance matrix.
    """
    def __init__(self, filepath):
        self.coords = []
        with open(filepath) as f:
            lines = f.readlines()
        reading = False
        for line in lines:
            if line.strip() == "NODE_COORD_SECTION":
                reading = True
                continue
            if reading:
                if line.strip() == "EOF":
                    break
                parts = line.strip().split()
                if len(parts) >= 3:
                    _, x, y = parts
                    self.coords.append((float(x), float(y)))
        self.n = len(self.coords)
        # build distance matrix
        self.distance_matrix = [[0]*self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                xi, yi = self.coords[i]
                xj, yj = self.coords[j]
                self.distance_matrix[i][j] = math.hypot(xi-xj, yi-yj)

    def cost(self, path):
        """Total tour length (closed loop)."""
        total = 0
        for i in range(len(path)):
            j = (i + 1) % len(path)
            total += self.distance_matrix[path[i]][path[j]]
        return total

    def random_solution(self):
        import random
        path = list(range(self.n))
        random.shuffle(path)
        return path

    def neighbors(self, path):
        """Generate all 2-swap neighbors of the current path."""
        for i in range(self.n):
            for j in range(i+1, self.n):
                neigh = path.copy()
                neigh[i], neigh[j] = neigh[j], neigh[i]
                yield neigh
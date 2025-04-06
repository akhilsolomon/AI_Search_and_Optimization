import math
import random

class TSPEnv:
    def __init__(self, filepath):
        self.coords = []
        with open(filepath, 'r') as f:
            lines = f.readlines()
            start = False
            for line in lines:
                if line.strip() == "NODE_COORD_SECTION":
                    start = True
                    continue
                if line.strip() == "EOF":
                    break
                if start:
                    parts = line.strip().split()
                    self.coords.append((float(parts[1]), float(parts[2])))

        self.n = len(self.coords)

    def cost(self, path):
        return sum(self.distance(path[i], path[(i + 1) % self.n]) for i in range(self.n))

    def distance(self, i, j):
        x1, y1 = self.coords[i]
        x2, y2 = self.coords[j]
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def random_solution(self):
        path = list(range(self.n))
        random.shuffle(path)
        return path

    def neighbors(self, path):
        for i in range(self.n):
            for j in range(i + 1, self.n):
                neighbor = path[:]
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                yield neighbor

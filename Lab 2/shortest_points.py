import matplotlib.pyplot as plt
import random
import math

class closest_pair():
    def __init__(self, num: int):
        self.num_points = num
        self.points = []
        self.min_dist_points = None

    def generate_points(self) -> None:
        num = self.num_points
        while len(self.points) < num:
            x = random.randint(0, 500)
            y = random.randint(0, 500)
            if (x, y) not in self.points:
                self.points.append((x, y))

    def run(self) -> None:
        self.generate_points()
        self.points.sort()  # Sort by x-coordinate
        self.min_dist_points = self.closest_pair_recursive(self.points)
        self.plot()

    def distance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def closest_pair_recursive(self, points):
        if len(points) <= 3:
            return self.brute_force(points)

        mid = len(points) // 2
        mid_point = points[mid]

        dl = self.closest_pair_recursive(points[:mid])
        dr = self.closest_pair_recursive(points[mid:])

        min_pair = dl if self.distance(*dl) < self.distance(*dr) else dr
        d = min(self.distance(*dl), self.distance(*dr))

        strip = [p for p in points if abs(p[0] - mid_point[0]) < d]

        strip_min = self.strip_closest(strip, d, min_pair)

        return strip_min

    def brute_force(self, points):
        min_dist = float('inf')
        min_pair = None
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if self.distance(points[i], points[j]) < min_dist:
                    min_dist = self.distance(points[i], points[j])
                    min_pair = (points[i], points[j])
        return min_pair

    def strip_closest(self, strip, d, min_pair):
        strip.sort(key=lambda p: p[1])
        min_dist = d

        for i in range(len(strip)):
            for j in range(i + 1, len(strip)):
                if strip[j][1] - strip[i][1] >= min_dist:
                    break
                if self.distance(strip[i], strip[j]) < min_dist:
                    min_dist = self.distance(strip[i], strip[j])
                    min_pair = (strip[i], strip[j])
        return min_pair

    def plot(self) -> None:
        plt.figure(figsize=(10, 10))
        x, y = zip(*self.points)
        plt.scatter(x, y, label="Points")

        if self.min_dist_points:
            p1, p2 = self.min_dist_points
            plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'r-', label="Closest Pair")

        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Closest Pair of Points")
        plt.legend()
        plt.grid(True)
        plt.show()

inp = input("Enter the number of points: ")
cp = closest_pair(int(inp))
cp.run()

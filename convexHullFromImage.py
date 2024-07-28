from PIL import Image
from tkinter import filedialog
import tkinter as tk
import random
import matplotlib.pyplot as plt


root = tk.Tk()
root.withdraw()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

def get_points_from_image():
    points = []
    baseImageAdd = filedialog.askopenfilename(
        title="Select images", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")]
    )
    bg = (255, 255, 255, 255)

    baseImage = Image.open(baseImageAdd)

    width, height = baseImage.size

    print(width, height)

    for x in range(width):
        for y in range(height):
            p = baseImage.getpixel((x,y))
            percentageDiff = [
                abs(p[i] - bg[i]) / 255.0 for i in range(len(p))
            ]
            absoluteDiff = sum(percentageDiff)
            if absoluteDiff > 0 :
                points.append(Point(x, y))
    return points

def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val > 0:
        return 1
    elif val < 0:
        return -1
    else:
        return 0


def leftmost_index(points):
    min_idx = 0
    for i in range(1, len(points)):
        if points[i].x < points[min_idx].x:
            min_idx = i
        elif points[i].x == points[min_idx].x:
            if points[i].y < points[min_idx].y:
                min_idx = i
    return min_idx

# Convex - hull gift wrapper 
def convex_hull(points):
    n = len(points)
    if n < 3:
        return []
    l = leftmost_index(points)
    hull = []
    p = l
    while True:
        hull.append(points[p])
        q = (p + 1) % n
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == -1:
                q = i
        p = q
        if p == l:
            break
    return hull

random_points = get_points_from_image()

hull = convex_hull(random_points)



# Plotting the points and the convex hull
def plot_points_and_hull(points, hull):
    x_points = [p.x for p in points]
    y_points = [p.y for p in points]

    hull_points = hull + [
        hull[0]
    ]  # Close the hull by adding the first point at the end
    x_hull = [p.x for p in hull_points]
    y_hull = [p.y for p in hull_points]

    plt.scatter(x_points, y_points, label="Random Points")
    plt.plot(x_hull, y_hull, color="red", label="Convex Hull")

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.title("Convex Hull of Random Points")
    plt.show()


plot_points_and_hull(random_points, hull)
from math import cos, sin

R, x_1, y_1 = 1, 0.75, 0
coordinates = [(R * (cos(t / 10000)) ** 3, R * (sin(t / 10000)) ** 3) for t in range(0, 2 * 31415, 1)]
distances = [((x_1 - coord[0]) ** 2 + (y_1 - coord[1]) ** 2) ** 0.5 for coord in coordinates]
for i in range(len(coordinates)):
    print(coordinates[i], distances[i])
print(round(min(distances), 4))

# где проверить? непонятно, может быть непривально...
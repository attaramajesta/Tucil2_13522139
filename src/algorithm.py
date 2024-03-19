import numpy as np

def brute_force(control_points, iterations):
    points = []
    for i in range(1, iterations + 1):
        step = 1 / (2 ** i)
        for t in np.arange(0, 1 + step, step):
            x, y = 0, 0
            n = len(control_points)
            for j, point in enumerate(control_points):
                c = np.math.comb(n - 1, j) * (1 - t) ** (n - 1 - j) * t ** j
                x += c * point[0]
                y += c * point[1]
            if i == iterations:
                points.append((x, y))
    return points

def divide_conquer(control_points, iterations, bezier=[], midpoints=[], current_iteration=0):
    if iterations == 0:
        return control_points, bezier, midpoints
    else:
        midpoint_1 = calculate_midpoint(control_points[0], control_points[1])
        midpoint_2 = calculate_midpoint(control_points[1], control_points[2])
        midpoint_3 = calculate_midpoint(midpoint_1, midpoint_2)
        
        bezier.append(midpoint_3)
        midpoints.append([midpoint_1, midpoint_2, midpoint_3])

        # left branch
        divide_conquer([control_points[0], midpoint_1, midpoint_3], iterations - 1, bezier, midpoints, current_iteration + 1)
        # right branch
        divide_conquer([midpoint_3, midpoint_2, control_points[2]], iterations - 1, bezier, midpoints, current_iteration + 1)

        return bezier, midpoints

def calculate_midpoint(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

#testing
def data():
    control_points = [(1, 3), (2, 5), (7, 6)]
    iterations = 3
    algorithm = 'dac'
    return control_points, iterations, algorithm

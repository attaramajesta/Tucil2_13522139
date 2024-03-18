import matplotlib.pyplot as plt
import numpy as np
import time

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

def linear_bezier(p0, p1, t):
    return ((1 - t) * p0[0] + t * p1[0], (1 - t) * p0[1] + t * p1[1])

def divide_conquer(control_points, iterations, midpoints=None, current_iteration=0, t=0.5):

    print("DEBUG: --------------------\nControl points:", control_points)
    print("Iteration:", iterations)
    print("Current iteration:", current_iteration)

    if current_iteration > iterations:
        return control_points, midpoints
    else:
        new_control_points = []
        midpoints = []

        if len(control_points) == 2:
            new_control_points.append(linear_bezier(control_points[0], control_points[1], t))
            print("DEBUG: new control points:", new_control_points)
        elif len(control_points) > 2:
            for idx in range(1, len(control_points)):
                print("DEBUG: idx-1:", control_points[idx-1])
                print("DEBUG: idx:", control_points[idx])
                point = linear_bezier(control_points[idx-1], control_points[idx], t)
                print("DEBUG: point:", point)
                print("\n")
                new_control_points.append(point)
                midpoints.append(point)

            print("midpoints:", midpoints)
            if len(midpoints) > 1:
                for i in range(len(midpoints) - 1):
                    plt.plot([midpoints[i][0], midpoints[i + 1][0]], [midpoints[i][1], midpoints[i + 1][1]], 'ko-', alpha=0.25, markersize=5)
                    plt.text(midpoints[i][0] + 0.1, midpoints[i][1], f'  ({midpoints[i][0]:.2f}, {midpoints[i][1]:.2f})', fontsize=8, ha='left', va='center')

            return divide_conquer(new_control_points, iterations, midpoints, current_iteration + 1, t)

    print("Midpoints:", midpoints)
    print("New control points:", new_control_points)
    return new_control_points

def calculate_midpoint(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

def get_user_input():
    num_points = int(input("Enter the number of control points: "))
    control_points = []
    for i in range(num_points):
        x, y = map(float, input(f"Enter the x and y coordinates of control point {i + 1}, separated by a space: ").split())
        control_points.append((x, y))
    iterations = int(input("Enter the number of iterations: "))
    algorithm = input("Enter 'bf' for brute force or 'dac' for divide and conquer: ")
    return control_points, iterations, algorithm

def data():
    control_points = [(1, 3), (2, 5), (7, 6), (9, 3)]
    iterations = 2
    algorithm = 'dac'
    return control_points, iterations, algorithm

def main():
    control_points, iterations, algorithm = data()
    
    plt.figure(figsize=(7, 5))
    plt.title('Bézier Curve')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    control_x = [point[0] for point in control_points]
    control_y = [point[1] for point in control_points]
    plt.plot(control_x, control_y, color='#FC8EAC', linestyle='-', label='Control Points')

    start_time = time.time() 

    if algorithm == 'bf':
        bezier = brute_force(control_points, iterations + 1)
        end_time = time.time()

        for points in bezier:
            plt.plot(points[0], points[1], 'ko')

        bezier.extend([control_points[0], control_points[-1]])
        sorted_bezier = sorted(bezier, key=lambda point: point[0])

        plt.plot(*zip(*sorted_bezier), color='g', label='Brute Force')
    elif algorithm == 'dac':
        bezier = divide_conquer(control_points, iterations + 1)
        print("bezier:" , bezier)

        bezier.append(control_points[0])
        bezier.append(control_points[-1])
        sorted_bezier = sorted(bezier, key=lambda point: point[0])
        print(sorted_bezier)

        plt.plot(*zip(*sorted_bezier), color='g', label='Divide And Conquer')
    else:
        print("Invalid algorithm choice. Please enter 'bf' or 'dac'.")

    plt.legend()
    plt.grid(True)
    plt.show()

main()

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

def divide_conquer(control_points, iterations, bezier=[], midpoints=[], current_iteration=0):
    if iterations == 0:
        return control_points, bezier, midpoints
    else:
        midpoint_1 = calculate_midpoint(control_points[0], control_points[1])
        midpoint_2 = calculate_midpoint(control_points[1], control_points[2])
        midpoint_3 = calculate_midpoint(midpoint_1, midpoint_2)
        
        bezier.append(midpoint_3)
        midpoints.append([midpoint_1, midpoint_2, midpoint_3])
        print(midpoints)
        
        # left branch
        divide_conquer([control_points[0], midpoint_1, midpoint_3], iterations - 1, bezier, midpoints, current_iteration + 1)
        # right branch
        divide_conquer([midpoint_3, midpoint_2, control_points[2]], iterations - 1, bezier, midpoints, current_iteration + 1)

        return bezier, midpoints

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
    control_points = [(1, 3), (2, 5), (7, 6)]
    iterations = 3
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
        bezier = brute_force(control_points, iterations)
        end_time = time.time()
        # print("LEN MID: ", len(bezier))
        # print("B:", bezier)

        plt.pause
        for points in bezier:
            plt.pause(0.2)
            plt.plot(points[0], points[1], 'ko')

        bezier.extend([control_points[0], control_points[-1]])
        sorted_bezier = sorted(bezier, key=lambda point: point[0])

        plt.pause(1)
        plt.plot(*zip(*sorted_bezier), color='g', label='Brute Force')
    elif algorithm == 'dac':
        bezier, midpoints = divide_conquer(control_points, iterations)
        # print("MIDPOINTS", midpoints)
        # print("BEZIER", bezier)

        end_time = time.time()

        plt.pause(1)
        for pair in midpoints: 
            plt.pause(0.2)
            plt.plot(pair[0][0], pair[0][1], 'ko', alpha=0.25, markersize=5) 
            plt.pause(0.5)
            plt.plot([pair[0][0], pair[1][0]], [pair[0][1], pair[1][1]], color='b', alpha=0.25)  
            plt.plot(pair[1][0], pair[1][1], 'ko', alpha=0.25, markersize=5) 
            plt.pause(0.5)
            plt.plot(pair[2][0], pair[2][1], 'ko', alpha=1, markersize=5) 
            plt.text(pair[2][0] + 0.1, pair[2][1], f'  ({pair[2][0]:.2f}, {pair[2][1]:.2f})', fontsize=8, ha='left', va='center')
            plt.pause(0.5)

        bezier.extend([control_points[0], control_points[-1]])
        sorted_bezier = sorted(bezier, key=lambda point: point[0])

        plt.pause(1)
        plt.plot(*zip(*sorted_bezier), color='g', label='Divide And Conquer')
    else:
        print("Invalid algorithm choice. Please enter 'bf' or 'dac'.")

    execution_time = (end_time - start_time) * 1000
    print("Execution Time:", execution_time, "ms")

    plt.legend()
    plt.grid(True)
    plt.show()

main()
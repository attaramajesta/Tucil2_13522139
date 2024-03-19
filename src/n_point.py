import matplotlib.pyplot as plt
import numpy as np
import time

# not finished

def linear_bezier(p0, p1, t):
    return ((1 - t) * p0[0] + t * p1[0], (1 - t) * p0[1] + t * p1[1])

def divide_conquer(p0, p1, control_points, iterations, current_iteration=0, t=0.5):
    print("DEBUG: --------------------\nControl points:", control_points)
    print("Iteration:", iterations)
    print("Current iteration:", current_iteration)

    if iterations == 0:
        return control_points
    else:
        new_control_points = []
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
        elif len(control_points) == 1:
            control_points = [control_points[0], p0, p1]  
            new_control_points = control_points 
        control_points[:] = new_control_points 
        print("DEBUG: new control points:", control_points)
        return divide_conquer(p0, p1, control_points, iterations - 1, current_iteration + 1, t)

def data():
    control_points = [(1, 3), (2, 5), (7, 6), (9, 3)]
    iterations = 1
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

        for points in bezier:
            plt.plot(points[0], points[1], 'ko')

        bezier.extend([control_points[0], control_points[-1]])
        sorted_bezier = sorted(bezier, key=lambda point: point[0])

        plt.plot(*zip(*sorted_bezier), color='g', label='Brute Force')
    elif algorithm == 'dac':
        bezier = divide_conquer(control_points[0], control_points[-1], control_points, iterations + 1)
        print("bezier:" , bezier)
        sorted_bezier = sorted(bezier, key=lambda point: point[0])
        print(sorted_bezier)

        plt.plot(*zip(*sorted_bezier), color='g', label='Divide And Conquer')
    else:
        print("Invalid algorithm choice. Please enter 'bf' or 'dac'.")

    plt.legend()
    plt.grid(True)
    plt.show()

main()
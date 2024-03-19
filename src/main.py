import matplotlib.pyplot as plt
import numpy as np
import time
import os
import sys
from bezier import get_user_input, brute_force, divide_conquer

def welcome_menu():
    print("Welcome to Bézier Curve Generator!")
    print("1. Divide and Conquer")
    print("2. Brute Force")
    print("3. Exit")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause_system():
    if os.name == 'nt':
        os.system('pause')
    else:
        os.system('read -p "Press any key to continue..."')

def main():
    while True:
        clear_screen()
        welcome_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            control_points, iterations, algorithm = get_user_input()
            bezier, midpoints = divide_conquer(control_points, iterations)
            print("Divide and Conquer results plotted!")
            pause_system()
        elif choice == '2':
            control_points, iterations, algorithm = get_user_input()
            bezier = brute_force(control_points, iterations)
            print("Brute Force results plotted!")
            pause_system()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            pause_system()

def main():
    control_points, iterations, algorithm = get_user_input()
    
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

if __name__ == "__main__":
    main()

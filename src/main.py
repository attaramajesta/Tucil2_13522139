import matplotlib.pyplot as plt
import numpy as np
import time
from algorithm import brute_force, divide_conquer
import os
import sys

def welcome_menu():
    print("\033[95mWelcome to Bézier Curve Generator!\033[0m\n\n")
    print("\033[95m───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\033[0m")
    print("\033[95m───█▒▒░░░░░░░░░▒▒█───\033[0m")
    print("\033[95m────█░░█░░░░░█░░█────\033[0m")
    print("\033[95m─▄▄──█░░░▀█▀░░░█──▄▄─\033[0m")
    print("\033[95m█░░█─▀▄░░░░░░░▄▀─█░░█\033[0m")
    print("\033[95m█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\033[0m")
    print("\033[95m█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\033[0m")
    print("\033[95m█░░║║║╠─║─║─║║║║║╠─░░█\033[0m")
    print("\033[95m█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\033[0m")
    print("\nChoose your algorithm below:")
    print("1. Divide and Conquer")
    print("2. Brute Force")
    print("3. Exit")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:

        clear_screen()
        welcome_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            control_points, iterations = get_user_input()
            calculate(control_points, iterations, 'dac')
            print("Divide and Conquer results plotted!")
            os.system('pause')
            os.system('cls' if os.name == 'nt' else 'clear')
        elif choice == '2':
            control_points, iterations = get_user_input()
            calculate(control_points, iterations, 'bf')
            print("Brute Force results plotted!")
            os.system('pause')
            os.system('cls' if os.name == 'nt' else 'clear')
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    
def get_user_input():
    while True:
        try:
            print("Enter three control points to generate the Bézier curve.\n")
            control_points = []
            for i in range(3):
                x, y = map(float, input(f"Enter the x and y coordinates of control point {i + 1}, separated by a space: ").split())
                control_points.append((x, y))
            
            iterations = int(input("Enter the number of iterations: "))
            
            return control_points, iterations
        
        except ValueError:
            print("Error: Invalid input format. Please enter numeric values.")
        except Exception as e:
            print("An error occurred:", e)

def calculate(control_points, iterations, algorithm):
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
            plt.pause(0.2)
            plt.plot(points[0], points[1], 'ko')

        bezier.extend([control_points[0], control_points[-1]])
        sorted_bezier = sorted(bezier, key=lambda point: point[0])

        plt.pause(1)
        plt.plot(*zip(*sorted_bezier), color='g', label='Brute Force')
    elif algorithm == 'dac':
        bezier, midpoints = divide_conquer(control_points, iterations)

        end_time = time.time()

        for pair in midpoints: 
            plt.pause(0.1)
            plt.plot(pair[0][0], pair[0][1], 'ko', alpha=0.25, markersize=5) 
            plt.pause(0.15)
            plt.plot([pair[0][0], pair[1][0]], [pair[0][1], pair[1][1]], color='b', alpha=0.25)  
            plt.plot(pair[1][0], pair[1][1], 'ko', alpha=0.25, markersize=5) 
            plt.pause(0.15)
            plt.plot(pair[2][0], pair[2][1], 'ko', alpha=1, markersize=5) 
            plt.text(pair[2][0] + 0.1, pair[2][1], f'  ({pair[2][0]:.2f}, {pair[2][1]:.2f})', fontsize=8, ha='left', va='center')
            plt.pause(0.15)

        bezier.extend([control_points[0], control_points[-1]])
        sorted_bezier = sorted(bezier, key=lambda point: point[0])

        plt.pause(1)
        plt.plot(*zip(*sorted_bezier), color='g', label='Divide And Conquer')

    execution_time = format((end_time - start_time) * 1000, '.10f')
    print("Execution Time:", execution_time, "ms")
    print("Close the plot to continue...")

    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()

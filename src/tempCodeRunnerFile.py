# def divide_conquer(control_points, iterations, midpoints=[], current_iteration=1):
#     print("--------------------\nControl points:", control_points)
#     print("Iteration:", iterations)
#     print("Current iteration:", current_iteration)
#     if iterations == 0:
#         return control_points, midpoints  # Return only bezier and midpoints
#     else:
#         new_control_points = []
#         for idx in range(0, len(control_points) - 1, 1):
#             # Calculate midpoints
#             print("idx:", idx)
#             print("idx+1:", idx + 1)
#             midpoint = calculate_midpoint(control_points[idx], control_points[idx + 1])
#             print("midpoint result:", midpoint)
#             midpoints.extend([midpoint])
#         new_control_points = midpoints[len(midpoints) // 2]
#         new_control_points = [control_points[0]] + [new_control_points] + [control_points[-1]]
#         print("new control points:", new_control_points)
#         print("midpoints:", midpoints)

#         return new_control_points, midpoints

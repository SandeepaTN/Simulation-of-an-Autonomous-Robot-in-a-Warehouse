# warehouse_simulation.py

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time
import heapq
import random
from matplotlib.animation import FuncAnimation


def run_simulation(speed, stop_time, num_obstacles):
    # Constants
    WAREHOUSE_SIZE = (10, 10)
    START = (0, 0)
    DESTINATION = (7, 9)
    MOVE_DISTANCE = 1  # Each move in the grid is 1 meter

    # Generate random obstacles while avoiding start and destination points
    def generate_random_obstacles(num_obstacles, warehouse_size, start, destination):
        obstacles = set()
        while len(obstacles) < num_obstacles:
            obstacle = (random.randint(
                0, warehouse_size[0] - 1), random.randint(0, warehouse_size[1] - 1))
            if obstacle != start and obstacle != destination:
                obstacles.add(obstacle)
        return obstacles

    # Heuristic for A* algorithm (Manhattan distance)
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # A* algorithm to find path from start to destination avoiding obstacles
    def a_star(start, goal, obstacles):
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: heuristic(start, goal)}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                path = [current]
                while current in came_from:
                    current = came_from[current]
                    path.append(current)
                path.reverse()
                return path

            x, y = current
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Neighboring cells
                neighbor = (x + dx, y + dy)
                if (0 <= neighbor[0] < WAREHOUSE_SIZE[0] and
                    0 <= neighbor[1] < WAREHOUSE_SIZE[1] and
                        neighbor not in obstacles):

                    tentative_g_score = g_score[current] + 1
                    if tentative_g_score < g_score.get(neighbor, float('inf')):
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = tentative_g_score + \
                            heuristic(neighbor, goal)
                        if neighbor not in [i[1] for i in open_set]:
                            heapq.heappush(
                                open_set, (f_score[neighbor], neighbor))
        return None  # No path found

    # Generate random obstacles
    obstacles = generate_random_obstacles(
        num_obstacles, WAREHOUSE_SIZE, START, DESTINATION)

    # Generate path from A* algorithm
    path = a_star(START, DESTINATION, obstacles)
    if path is None:
        print("No path found")
        return

    # Visualization setup
    fig, ax = plt.subplots(figsize=(6, 6))
    plt.xlim(-0.5, WAREHOUSE_SIZE[0] - 0.5)
    plt.ylim(-0.5, WAREHOUSE_SIZE[1] - 0.5)
    ax.set_xticks(range(WAREHOUSE_SIZE[0]))
    ax.set_yticks(range(WAREHOUSE_SIZE[1]))
    plt.grid(True)

    # Plot obstacles, start, and destination
    for (ox, oy) in obstacles:
        ax.add_patch(patches.Rectangle(
            (ox - 0.5, oy - 0.5), 1, 1, color='gray'))
    ax.plot(START[0], START[1], 'go', label="Start")  # Start as a green dot
    ax.plot(DESTINATION[0], DESTINATION[1], 'ro',
            label="Destination")  # Destination as a red dot

    # Initialize robot position and movement trail
    robot, = ax.plot([], [], 'bo', markersize=10)  # Blue dot for the robot
    # Cyan line for the path trail
    trail, = ax.plot([], [], 'c-', linewidth=2, label="Path")
    plt.legend()

    # Calculate interval time based on speed
    # Convert to milliseconds for FuncAnimation
    interval_time = (MOVE_DISTANCE / speed) * 1000

    # Movement Simulation with Animation
    def animate_robot(i):
        if i < len(path):
            x, y = path[i]
            robot.set_data((x,), (y,))
            trail.set_data([p[0] for p in path[:i+1]], [p[1]
                           for p in path[:i+1]])

            # Pause to simulate robot stopping for specified time after each move
            if i > 0 and i % 2 == 0:
                time.sleep(stop_time)

    # Create animation
    anim = FuncAnimation(fig, animate_robot, frames=len(
        path), interval=interval_time, repeat=False)

    # Display plot with animated path
    plt.show()

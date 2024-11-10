
# Simulation of an Autonomous Robot in a Warehouse

This project simulates an autonomous robot navigating through a warehouse to reach a destination while avoiding obstacles. The simulation visualizes the robot's pathfinding using the A* algorithm, with configurable speed, stopping time, and a set number of obstacles.

## GitHub Repository
[GitHub Repository](https://github.com/SandeepaTN/Simulation-of-an-Autonomous-Robot-in-a-Warehouse)

## Features
- **Obstacle Generation**: Randomly places obstacles within the warehouse grid.
- **Pathfinding**: Uses the A* algorithm to find the optimal path from the start to the destination.
- **Simulation Controls**: Users can control robot speed, stop time, and the number of obstacles.
- **Visualization**: Animates the robot's movement along the calculated path.

## Technologies Used
- Python
- Flask
- JavaScript (for frontend form submission and interaction)
- HTML & CSS (for UI)
- Matplotlib (for visualization)
- Numpy

## Project Structure
- `app.py`: Main Flask application file.
- `warehouse_simulation.py`: Contains the logic for the warehouse simulation, pathfinding, and animation.
- `templates/index.html`: Frontend HTML form for user input.
- `static/`: Contains any additional static files, like CSS or JavaScript files (if required).

## Getting Started

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/SandeepaTN/Simulation-of-an-Autonomous-Robot-in-a-Warehouse.git
   cd Simulation-of-an-Autonomous-Robot-in-a-Warehouse
   ```

2. **Install Dependencies**  
   Install the required Python packages from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application Locally**  
   Start the Flask application:
   ```bash
   python app.py
   ```
   Access the application locally at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Usage
1. Visit the application at [http://127.0.0.1:5000](http://127.0.0.1:5000).
2. Adjust simulation parameters:
   - **Robot Speed (m/s)**: Speed at which the robot moves.
   - **Stop Time (s)**: Time the robot pauses after each move.
   - **Number of Obstacles**: Number of obstacles in the warehouse.
3. Click **Run Simulation** to start the simulation.
4. Watch the robot navigate through the warehouse on the visualized path.


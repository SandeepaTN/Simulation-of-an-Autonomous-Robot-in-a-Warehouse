# app.py
from flask import Flask, render_template, request, jsonify
import warehouse_simulation

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run_simulation', methods=['POST'])
def run_simulation():
    data = request.form
    speed = float(data['speed'])
    stop_time = float(data['stop_time'])
    num_obstacles = int(data['num_obstacles'])

    # Run the simulation
    warehouse_simulation.run_simulation(speed, stop_time, num_obstacles)
    return jsonify({"status": "Simulation completed"})


if __name__ == '__main__':
    app.run(debug=False)

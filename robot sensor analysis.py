import numpy as np
import matplotlib.pyplot as plt
import time

# Simulated sensor data (distance readings in cm)
# Negative values indicate faulty readings
sensor_data = [50, 48, 45, 43, 30, 15, 10, 8, 50, 60, 55, 40, 10, -5, 7, 9]

# Predefined safety distance threshold (in cm)
SAFETY_DISTANCE = 20

def clean_sensor_data(data):
    """Clean raw sensor data by removing negative or nonsensical values."""
    return [x if x > 0 else np.nan for x in data]

def detect_obstacles(data, threshold):
    """Detect obstacles by checking if distances fall below a threshold."""
    return [True if reading < threshold else False for reading in data]

def visualize_data(raw_data, clean_data, obstacles):
    """Visualize sensor data and highlight obstacle points."""
    time_steps = list(range(len(raw_data)))
    plt.figure(figsize=(10, 6))
    plt.plot(time_steps, clean_data, label="Clean Sensor Data", marker="o", color="blue")
    plt.axhline(y=SAFETY_DISTANCE, color="red", linestyle="--", label="Safety Threshold")
    
     # Highlight points where obstacles are detected
    for i, obstacle in enumerate(obstacles):
        if obstacle:
            plt.scatter(i, clean_data[i], color="red", label="Obstacle Detected" if i == obstacles.index(True) else "")
            
    plt.title("Robot Sensor Data Analysis")
    plt.xlabel("Time Step")
    plt.ylabel("Distance (cm)")
    plt.legend()
    plt.grid(True)
    plt.show()

def robot_action(obstacles):
    """Simulate robot's reaction based on obstacle detection."""
    for i, obstacle in enumerate(obstacles):
        if obstacle:
            print(f"Time Step {i}: Obstacle detected! Taking evasive action.")
        else:
            print(f"Time Step {i}: Path is clear. Moving forward.")


# Main workflow
cleaned_data = clean_sensor_data(sensor_data)
obstacle_detected = detect_obstacles(cleaned_data, SAFETY_DISTANCE)

# Visualization
visualize_data(sensor_data, cleaned_data, obstacle_detected)

# Simulated robot response
robot_action(obstacle_detected)

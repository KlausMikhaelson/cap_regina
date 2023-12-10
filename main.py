import numpy as np
import matplotlib.pyplot as plt

def reentry_trajectory(mass, initial_angle, drag_coefficient, area, initial_velocity, initial_altitude, time_step, duration, planet_gravity, atmosphere_density, parachute_altitude, safe_g_load):
    # Convert initial angle to radians
    initial_angle_rad = np.radians(initial_angle)

    # Calculate initial x and y components of velocity
    initial_velocity_x = initial_velocity * np.cos(initial_angle_rad)
    initial_velocity_y = initial_velocity * np.sin(initial_angle_rad)

    # Initialize variables
    velocity_x = initial_velocity_x
    velocity_y = initial_velocity_y
    altitude = initial_altitude
    time = 0
    g_load = 0
    velocities = []
    altitudes = []

    # Simulation loop
    while altitude > 0 and time < duration:
        # Calculate gravitational force
        gravity_force = planet_gravity * mass

        # Calculate atmospheric drag force
        velocity = np.sqrt(velocity_x**2 + velocity_y**2)
        drag_force = 0.5 * atmosphere_density * velocity**2 * drag_coefficient * area

        # Calculate net force
        net_force_x = 0  # Assuming no horizontal forces for simplicity
        net_force_y = gravity_force - drag_force

        # Calculate acceleration
        acceleration_x = net_force_x / mass
        acceleration_y = net_force_y / mass

        # Update velocity components and altitude using Euler's method
        velocity_x += acceleration_x * time_step
        velocity_y += acceleration_y * time_step
        altitude -= velocity_y * time_step

        # Update time
        time += time_step

        # Update g-load
        g_load = np.sqrt(acceleration_x**2 + acceleration_y**2) / 9.81

        # Store data for plotting
        velocities.append(np.sqrt(velocity_x**2 + velocity_y**2))
        altitudes.append(altitude)

        # Check for parachute deployment conditions
        if altitude <= parachute_altitude and g_load <= safe_g_load:
            print("Parachute deployed successfully.")
            break

    # Plot the trajectory
    time_points = np.arange(0, time, time_step)
    plt.plot(time_points, altitudes)
    plt.xlabel('Time (s)')
    plt.ylabel('Altitude (m)')
    plt.title('Re-entry Trajectory')
    plt.show()
# Example usage
mass = 5000  # spacecraft mass in kg
initial_angle = 45  # initial trajectory angle in degrees
drag_coefficient = 0.2  # drag coefficient
area = 20  # area in square meters
initial_velocity = -500  # initial velocity in m/s, it's negative since it's re-entering
initial_altitude = 100000  # initial altitude in meters
time_step = 0.1  # time step for simulation in seconds
duration = 1000  # maximum simulation time in seconds
planet_gravity = 9.81  # gravity of the planet/moon in m/s^2
atmosphere_density = 0.02  # average atmosphere density in kg/m^3
parachute_altitude = 5000  # altitude for parachute deployment in meters
safe_g_load = 3  # maximum allowable g-load for astronauts since astronauts are trained to withstand up to 3 g's


def main():
    print("Hello World!")
    reentry_trajectory(mass, initial_angle, drag_coefficient, area, initial_velocity, initial_altitude, time_step, duration, planet_gravity, atmosphere_density, parachute_altitude, safe_g_load)


if __name__ == "__main__":
    main()
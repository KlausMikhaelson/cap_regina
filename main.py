import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from reenter import reentry_trajectory, mass, initial_angle, drag_coefficient, area, initial_velocity, initial_altitude, time_step, duration, planet_gravity, atmosphere_density, parachute_altitude, safe_g_load

def main():
    st.title("Rocket Re-entry Simulation Model")
    st.text("You can use the slider in the sidebar to change the input parameters.")

    # Sidebar input widgets for changing parameters for the simulation
    mass = st.sidebar.slider("Spacecraft Mass (kg)", 1844, 10000, 5000)
    initial_angle = st.sidebar.slider("Initial Entry Angle (degrees)", 0, 90, 45)
    planet_gravity = st.sidebar.slider("Planet Gravity (m/s^2)", 6.35, 20.0, 9.81)
    initial_velocity = st.sidebar.slider("Initial Velocity (m/s)", -1000, 0, -500)
    initial_altitude = st.sidebar.slider("Initial Altitude (m)",44500, 100000, 100000)
    duration = st.sidebar.slider("Duration (s)", 76, 2000, 1000)

    time_points, altitudes = reentry_trajectory(mass, initial_angle, drag_coefficient, area, initial_velocity, initial_altitude, time_step, duration, planet_gravity, atmosphere_density, parachute_altitude, safe_g_load)

    # Ploting the trajectory
    st.line_chart(list(zip(time_points, altitudes)), use_container_width=True)

if __name__ == "__main__":
    main()
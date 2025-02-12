import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def simulate_projectile():
    try:
        v0 = float(velocity_entry.get())  # Initial velocity
        angle = float(angle_entry.get())  # Launch angle
        g = 9.81  # Gravity (m/s^2)
        
        theta = np.radians(angle)
        t_flight = (2 * v0 * np.sin(theta)) / g  # Total flight time
        t = np.linspace(0, t_flight, num=100)  # Time intervals
        
        x = v0 * np.cos(theta) * t  # X-coordinates
        y = v0 * np.sin(theta) * t - (0.5 * g * t**2)  # Y-coordinates
        
        ax.clear()
        ax.plot(x, y)
        ax.set_xlabel("Distance (m)")
        ax.set_ylabel("Height (m)")
        ax.set_title("Projectile Motion")
        ax.grid()
        canvas.draw()
    except ValueError:
        error_label.config(text="Please enter valid numbers")

# GUI setup
root = tk.Tk()
root.title("Projectile Motion Simulator")
root.geometry("600x500")

frame = ttk.Frame(root)
frame.pack(pady=10)

tt = ttk.Label(frame, text="Enter Initial Velocity (m/s):")
tt.grid(row=0, column=0)
velocity_entry = ttk.Entry(frame)
velocity_entry.grid(row=0, column=1)

tt2 = ttk.Label(frame, text="Enter Launch Angle (degrees):")
tt2.grid(row=1, column=0)
angle_entry = ttk.Entry(frame)
angle_entry.grid(row=1, column=1)

simulate_button = ttk.Button(frame, text="Simulate", command=simulate_projectile)
simulate_button.grid(row=2, columnspan=2, pady=5)

error_label = ttk.Label(root, text="", foreground="red")
error_label.pack()

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()
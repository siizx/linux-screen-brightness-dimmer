#!/usr/bin/env python
import subprocess
import tkinter as tk
from tkinter import Scale

# Define the minimum allowed brightness
MIN_BRIGHTNESS = 10

def set_brightness(brightness):
    # Replace 'your_display_name' with your actual display name, e.g., 'eDP-1'
    display_name = 'eDP-1'
    
    # Ensure the brightness is not below the minimum
    brightness = max(int(brightness), MIN_BRIGHTNESS)
    
    # Set the brightness using xrandr
    brightness_value = brightness / 100.0
    subprocess.run(['xrandr', '--output', display_name, '--brightness', str(brightness_value)])

def update_brightness(value):
    set_brightness(value)

# Create a simple tkinter window
window = tk.Tk()
window.title("Brightness Control")

# Create a brightness scale
brightness_label = tk.Label(window, text="Brightness")
brightness_label.pack()
brightness_scale = Scale(window, from_=MIN_BRIGHTNESS, to=100, orient="horizontal", command=update_brightness)
brightness_scale.set(100)  # Initialize to maximum brightness
brightness_scale.pack()

# Start the GUI
window.mainloop()


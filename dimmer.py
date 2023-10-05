#!/usr/bin/env python

import subprocess

def set_brightness(brightness):
    # Replace 'your_display_name' with your actual display name, e.g., 'eDP-1'
    display_name = 'eDP-1'
    
    # Set the brightness using xrandr
    brightness_value = brightness / 100.0
    subprocess.run(['xrandr', '--output', display_name, '--brightness', str(brightness_value)])

def main():
    while True:
        try:
            brightness = float(input("Enter brightness (10-100): "))
            if 10 <= brightness <= 100:
                set_brightness(brightness)
            else:
                print("Brightness value must be between 10 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number between 10 and 100.")

if __name__ == '__main__':
    main()


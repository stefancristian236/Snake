#!/bin/bash
source pygame-env/bin/activate
python main.py
deactivate
# This script activates the virtual environment and runs the main.py file.
# After the script finishes, it deactivates the virtual environment.
# Make sure to give execute permission to this script before running it.
# You can do this by running:
# chmod +x run.sh
# Then you can run the script with:
# ./run.sh
# Make sure to replace 'pygame-env' with the name of your virtual environment if it's different.
# This script assumes that you have a virtual environment set up with the necessary dependencies installed.
# If you haven't set up a virtual environment yet, you can do so with the following commands:
# python3 -m venv pygame-env
# source pygame-env/bin/activate
# pip install pygame
# pip install numpy
# pip install matplotlib
# pip install opencv-python         
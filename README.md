# DIGIT-FSR-GUI

## Overview

**DIGIT-FSR-GUI** is a custom extension of the original [DIGIT-GUI](https://github.com/gemixin/digit-gui), developed to support the collection of a bespoke dataset using a single [DIGIT](https://digit.ml/) tactile sensor with an attached Force Sensing Resistor ([FSR](https://wiki.seeedstudio.com/Grove-Round_Force_Sensor_FSR402/)). The FSR is affixed to the rear of the tactile sensor using adhesive and is connected to a Raspberry Pi Pico (via a [Grove Shield](https://wiki.seeedstudio.com/Grove-Starter-Kit-for-Raspberry-Pi-Pico/)). 

This version adds functionality specifically for force-conditioned tactile data collection:

- Establishes a USB serial connection for receiving streamed FSR measurements.
- Allows the user to select the target force level (1–3) for data capture.
- Filters captured tactile images according to the chosen force level.
- Logs FSR voltage readings alongside corresponding tactile images in a CSV file.

## Requirements

- **Operating System:** Linux only (DIGIT sensors are supported on Linux only)  
- **Tested Environment:** Ubuntu 22.04, Python 3.10.12 
- **Python Environment:** Use a regular Python virtual environment (Tkinter and Anaconda have compatibility issues on Linux)
- **Packages:** See `requirements.txt`

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gemixin/digit-fsr-gui.git
   cd digit-fsr-gui

2. **(Optional) Set up a virtual environment:** 
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate

3. **Install required packages:**  
    ```bash
    python3 -m pip install -r requirements.txt

## Citation

If you use DIGIT or this repo in your research, please cite:

**DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation**  
Mike Lambeta, Po-Wei Chou, Stephen Tian, Brian Yang, Benjamin Maloon, Victoria Rose Most, Dave Stroud, Raymond Santos, Ahmad Byagowi, Gregg Kammerer, Dinesh Jayaraman, Roberto Calandra  
_IEEE Robotics and Automation Letters (RA-L), vol. 5, no. 3, pp. 3838–3845, 2020_  
[https://doi.org/10.1109/LRA.2020.2977257](https://doi.org/10.1109/LRA.2020.2977257)
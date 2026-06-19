# Serial Port Terminal

A Python-based Serial Port Terminal application for communicating with embedded systems through UART/Serial interfaces. This tool allows users to send and receive data over serial ports, monitor communication in real time, and save logs for debugging and analysis.

## Features
* Detect available serial ports
* Connect and disconnect from serial devices
* Configure baud rate, parity, stop bits, and data bits
* Send text commands to the target device
* Receive and display serial data in real time
* Timestamp received messages
* Save communication logs to a file
* Clear terminal output
* Cross-platform support (Windows/Linux)

## Applications

**This project is useful for:**

* Embedded firmware debugging
* Microcontroller communication testing
* UART driver validation
* Sensor data monitoring
* Bootloader communication
* Learning serial communication concepts

## Technologies Used
* Python 3.x
* PySerial
* Tkinter (optional GUI version)

## Required Packages
    Pyserial

## Installation
* To build a serial port terminal in Python, the industry-standard library is `pySerial`.

        pip install pyserial

## To Find Available Serial Ports
* Run this quick script to find out which COM port (Windows) or tty device (Linux/Mac) your hardware is plugged into:

        import serial.tools.list_ports

        ports = serial.tools.list_ports.comports()
        for port in ports:
            print(f"Port: {port.device} | Description: {port.description}")

## Creating the package files
You will now add files that are used to prepare the project for distribution. When you’re done, the project structure will look like this:

    packaging_tutorial/
    ├── LICENSE
    ├── pyproject.toml
    ├── README.md
    ├── src/
    │   └── example_package_YOUR_USERNAME_HERE/
    │       ├── __init__.py
    │       └── example.py
    └── tests/
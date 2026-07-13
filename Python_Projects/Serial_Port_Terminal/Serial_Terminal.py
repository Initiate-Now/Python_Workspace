'''*****************************************************
* Name   : Serial_Terminal.py
* Purpose: To create an interactive terminal for serial communication with a device
* Author : Navin Chakravarthy Kamalakannan
*********************************************************'''

import serial
import threading
import sys

# Terminal Configurations
PORT = 'COM4'
BAUDRATE = 115200

def read_from_port(ser):
    """ Continuously monitors and prints incoming data from the serial device."""
    while ser.is_open:
        try:
            if ser.in_waiting > 0:
                # Read available bytes in buffer
                incoming = ser.readline()
                print(f"\n[Device]: {incoming.decode('utf-8', errors='ignore').strip()}")
                print("[You]: ", end="", flush=True)
        except Exception as e:
            print(f"\nRead Error: {e}")
            break

def main():
    try:
        ser = serial.Serial(PORT, BAUDRATE, timeout=1)
        print(f"--- Interactive Terminal Started on {PORT} ({BAUDRATE} baud) ---")
        print("--- Type your message and press Enter. Type 'EXIT' to quit. ---\n")
    except serial.SerialException as e:
        print(f"Failed to connect to {PORT}: {e}")
        sys.exit(1)

    # Spin up background thread for handling live reads
    read_thread = threading.Thread(target=read_from_port, args=(ser,), daemon=True)
    read_thread.start()

    # Handle user inputs via main thread
    try:
        while True:
            user_input = input("[You]: ")
            if user_input.strip().upper() == "EXIT":
                print("Closing application...")
                break
            
            # Send message with a carriage return and newline line terminator
            command = user_input + "\r\n"
            ser.write(command.encode('utf-8'))
            
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    finally:
        ser.close()
        print("Serial connection cleanly severed.")

if __name__ == "__main__":
    main()

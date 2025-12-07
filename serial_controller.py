import serial

# Constants
BAUDRATE = 115200
TIMEOUT = 1
PORT = '/dev/ttyACM0'


class SerialController:
    """
    A controller class for managing the USB serial connection and operations.

    Author: Gemma McLean
    Date: December 2025
    """

    def __init__(self):
        """
        Initialise the SerialController to manage USB serial connections.
        Auto connects to the device at the default port.
        """

        # Connect and store the instance
        try:
            self.serial_connection = serial.Serial(PORT, BAUDRATE, timeout=TIMEOUT)
        except serial.SerialException:
            self.serial_connection = None

    # --- Public getters ---
    def get_reading(self):
        """
        Get a reading from the serial connection. First clears the input buffer.
        Then reads a line, decodes it and strips any trailing whitespace.

        Returns:
            str: The decoded string read from the serial connection.
        """
        if self.serial_connection:
            try:
                self.serial_connection.reset_input_buffer()
                return self.serial_connection.readline().decode('utf-8').rstrip()
            except Exception as e:
                print(f'Failed to read from serial connection: {e}')
                return None

    # --- Public setters/actions ---
    def disconnect(self):
        """Disconnect the serial device."""

        if self.serial_connection:
            try:
                self.serial_connection.close()
            except Exception as e:
                print(f'Failed to disconnect serial connection: {e}')

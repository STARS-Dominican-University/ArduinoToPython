import serial

ser = serial.Serial('/dev/cu.usbmodem113301', 9600)  # Adjust the serial port and baud rate

while True:
    # Read data from the serial port
    data = ser.readline().decode('utf-8').strip()

    # Process the received data
    print(data)

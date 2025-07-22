# recv_raw.py
import serial
ser = serial.Serial('COM11', 9600, timeout=1)
print('listening COM11...')
while True:
    n = ser.in_waiting
    if n:
        data = ser.read(n)
        print(data.hex(' '))

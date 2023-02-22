import serial 
import time

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)


while True:
    try:
        data = arduino.readline()
        if data == b'Hi Jetson!\r\n':
        # if data:
            print(data)
            time.sleep(1)
            print('Hi Arduino')


    except:
        arduino.close() 

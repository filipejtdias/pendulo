import os, sys, inspect, serial, time
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

import config as CONFIG

class Main:
    
    @staticmethod
    def run(COMMAND):
        
        SERIALPORT = CONFIG.PENDULO.SERIAL_PORT
        BAUDRATE = CONFIG.PENDULO.BAUDRATE

        ser = serial.Serial(SERIALPORT, BAUDRATE)
        ser.bytesize = serial.EIGHTBITS
        ser.parity = serial.PARITY_NONE
        ser.stopbits = serial.STOPBITS_ONE
        ser.timeout = None
        ser.xonxoff = False
        ser.rtscts = False
        ser.dsrdtr = False
        ser.writeTimeout = 0

        try:
            ser.open()

        except Exception, e:
            pass

        if ser.isOpen():

            try:
                ser.flushInput() #flush input buffer, discarding all its contents
                ser.flushOutput()#flush output buffer, aborting current output

                COMMAND = COMMAND + "\r" # Simulate Enter

                write_data = COMMAND.encode('utf-8')

                ser.write(write_data)

                time.sleep(0.5)

                numOfLines = 0

                while True:
                    response = ser.readline()
                    print("read data: " + response)

                    numOfLines = numOfLines + 1

                    if (numOfLines >= 5):
                        break

                    ser.close()

            except Exception, e:
                print "error communicating...: " + str(e)

        else:
            print "Serial port not opened"

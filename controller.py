import pyfirmata2

comport='/dev/cu.usbmodem14201'

board=pyfirmata2.Arduino(comport)


led_1=board.get_pin('d:8:o')
led_2=board.get_pin('d:9:o')
led_3=board.get_pin('d:10:o')
led_4=board.get_pin('d:11:o')
led_5=board.get_pin('d:12:o')
# use switch case and function taking in variables for function led write

def ledWrite(f1, f2, f3, f4, f5):
        led_1.write(f1)
        led_2.write(f2)
        led_3.write(f3)
        led_4.write(f4)
        led_5.write(f5)
def led(fingerUp):
    # one finger combinations
    if fingerUp==[0,0,0,0,0]:
        ledWrite(0,0,0,0,0)
    elif fingerUp==[1,0,0,0,0]:
        ledWrite(1,0,0,0,0)
    elif fingerUp==[0,1,0,0,0]:
        ledWrite(0,1,0,0,0)
    elif fingerUp==[0,0,1,0,0]:
        ledWrite(0,0,1,0,0)
    elif fingerUp==[0,0,0,1,0]:
        ledWrite(0,0,0,1,0)
    elif fingerUp==[0,0,0,0,1]:
        ledWrite(0,0,0,0,1)
    #two finger combinations
    elif fingerUp==[1,1,0,0,0]:
        ledWrite(1,1,0,0,0)  
    elif fingerUp==[1,0,1,0,0]:
        ledWrite(1,0,1,0,0) 
    elif fingerUp==[1,0,0,1,0]:
        ledWrite(1,0,0,1,0)
    elif fingerUp==[1,0,0,0,1]:
        ledWrite(1,0,0,0,1)
    elif fingerUp==[0,1,1,0,0]:
        ledWrite(0,1,1,0,0)
    elif fingerUp==[0,1,0,1,0]:
        ledWrite(0,1,0,1,0)
    elif fingerUp==[0,1,0,0,1]:
        ledWrite(0,1,0,0,1)
    elif fingerUp==[0,0,1,1,0]:
        ledWrite(0,0,1,1,0)
    elif fingerUp==[0,0,1,0,1]:
        ledWrite(0,0,1,0,1)
    elif fingerUp==[0,0,0,1,1]:
        ledWrite(0,0,0,1,1)
    #three finger combinations
    elif fingerUp==[1,1,1,0,0]:
        ledWrite(1,1,1,0,0)
    elif fingerUp==[0,1,1,1,0]:
        ledWrite(0,1,1,1,0)
    elif fingerUp==[0,0,1,1,1]:
        ledWrite(0,0,1,1,1)
    elif fingerUp==[1,1,0,1,0]:
        ledWrite(1,1,0,1,0)
    elif fingerUp==[1,1,0,0,1]:
        ledWrite(1,1,0,0,1)
    elif fingerUp==[0,1,1,0,1]:
        ledWrite(0,1,1,0,1)
    elif fingerUp==[1,0,1,0,1]:
        ledWrite(1,0,1,0,1)
    elif fingerUp==[1,0,0,1,1]:
        ledWrite(1,0,0,1,1)
    #four finger combinations
    elif fingerUp==[0,1,1,1,1]:
        ledWrite(0,1,1,1,1)
    elif fingerUp==[1,1,1,1,0]:
        ledWrite(1,1,1,1,0)
    elif fingerUp==[1,1,0,1,1]:
        ledWrite(1,1,0,1,1)
    elif fingerUp==[1,1,1,1,1]:
        ledWrite(1,1,1,1,1)
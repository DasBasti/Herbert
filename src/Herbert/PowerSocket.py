import time
import RPi.GPIO as GPIO

BTN = [0, 17, 4, 27]
BTN1 = 17
BTN2 = 4
BTN3 = 27
SEL = 22
#gp17 btn 1
#gp4 btn 2
#gp27 btn 3
#gp22 sel

def Setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BTN1, GPIO.OUT, initial=1)
    GPIO.setup(BTN2, GPIO.OUT, initial=1)
    GPIO.setup(BTN3, GPIO.OUT, initial=1)
    GPIO.setup(SEL, GPIO.OUT, initial=1)

def Toggle(rel):
    rel = int(rel)
       
    if rel > 3:
        rel = rel - 3
        GPIO.output(SEL, 0)
    else:
        GPIO.output(SEL, 1)
     
    time.sleep(0.1)
    GPIO.output(BTN[rel], 0)
    time.sleep(0.2)
    GPIO.output(BTN[rel], 1)
              
    #return "toggle: "+str(rel)

def CreateLink(socket, name, field):
    return "<p> <a class=\"button\" href=\"/PowerSocket/Toggle/"+str(socket)+"\">"+name+"</a> </p>"

def CreateText():
    return ""

def Unset():
    GPIO.cleanup()

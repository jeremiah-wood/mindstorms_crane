#file: /home/pi/crane2.py
# Jeremiah Wood 3-27-17

from BrickPi import*
BrickPiSetup()

#this makes the claws on the crane close
BrickPi.MotorEnable[PORT_B] = 1
BrickPi.MotorSpeed[PORT_B] = -20
for i in range (600):
    BrickPiUpdateValues() 
   
#this turns the crane counter clockwise viewed from above
BrickPi.MotorEnable[PORT_A] = 1
BrickPi.MotorSpeed[PORT_A] = 50
for i in range (400):
   BrickPiUpdateValues() 

#time.sleep(6)     # sleep 

#crane rotates back
BrickPi.MotorEnable[PORT_A] = 1
BrickPi.MotorSpeed[PORT_A] = -50
for i in range (200):
   BrickPiUpdateValues()
   
#claws open to release object
BrickPi.MotorEnable[PORT_B] = 1
BrickPi.MotorSpeed[PORT_B] = 20
for i in range (150):
    BrickPiUpdateValues()

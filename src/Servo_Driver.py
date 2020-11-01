import RPi.GPIO as GPIO
import time


class Servo_Driver:
    SERVO_PIN = None
    SERVO_PULSE = 50 # HZ
    SERVO_HOME_POSITION = 2 # duty cycle
    servo = None
    MOVE_ANGLE = 35

    def __init__(self, servo_pin):
        print('Intializing Srervo...')
        self.SERVO_PIN = servo_pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.SERVO_PIN,GPIO.OUT)
        self.servo = GPIO.PWM(self.SERVO_PIN,self.SERVO_PULSE)
        
        print('Done. Servo intialization done at pin ', self.SERVO_PIN, ' @ ', self.SERVO_PULSE, ' Hz pulse \n')

    def start(self):
        print("Servo Start called.\n")
        self.servo.start(0)
        
    
    def move( self,counter ):
        try:
            while counter > 0:
                time.sleep(1)
                self.servo.ChangeDutyCycle(self.SERVO_HOME_POSITION)
                time.sleep(1)
                # move servo to self.MOVE_ANGLE degree
                print('Rotate by ', self.MOVE_ANGLE, ' degree')
                self.servo.ChangeDutyCycle( 2 + (self.MOVE_ANGLE / 18) )
                time.sleep(0.2)
                self.servo.ChangeDutyCycle(0)

                print('Rotate it back to home position')
                counter = counter - 1
        finally:
            print('Servo Done...!!')
    
    def stop(self):
        print("Servo Start called.\n")
        # self.servo.stop() # Raspberry Pi PWN issue, after stop PWM does not work.
        self.servo.ChangeDutyCycle(0)
    
    def cleanup(self):
        print("Servo ceanup called.\n")
        self.servo.stop()


if __name__ == "__main__":
    servo = Servo_Driver(13)

    servo.start()
    servo.move(5)
    # servo.stop()        

    # servo.start()
    servo.move(5)
    servo.stop()        



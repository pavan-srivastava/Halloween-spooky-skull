import RPi.GPIO as GPIO
import time
import pygame
import Servo_Driver as Servo

class SpookySkull:

    GPIO_PIN_LED = 3
    GPIO_PIN_PIR = 11
    GPIO_PIN_SERVO = 13
    jaw = None
    
    def __init__(self):       
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.GPIO_PIN_PIR, GPIO.IN)         #Read output from PIR motion sensor
        GPIO.setup(self.GPIO_PIN_LED, GPIO.OUT)
        self.jaw = Servo.Servo_Driver(self.GPIO_PIN_SERVO)
        self.jaw.start()
        pygame.mixer.init()
        pygame.mixer.music.load("/home/shared/projects/khopadi/sound/Haloween.mp3")
        pygame.mixer.music.set_volume(1.0)

    def start(self):
        try:
            while True:
                pir = GPIO.input(self.GPIO_PIN_PIR)
                
                if pir == 0:                 #When output from motion sensor is LOW
                    # print ("No intruders",pir)
                    GPIO.output(self.GPIO_PIN_LED, 0)  #Turn OFF LED
                    time.sleep(0.1)
                elif pir == 1:               #When output from motion sensor is HIGH
                    print ("Intruder detected",pir)
                    pygame.mixer.music.play()
                    GPIO.output(self.GPIO_PIN_LED, 1)  #Turn ON LED
                    time.sleep(0.1)
                    self.jaw.move(3)
                    pygame.mixer.music.stop()
        finally:
                self.jaw.cleanup()
                GPIO.output(self.GPIO_PIN_LED, 0)  #Turn OFF LED
                GPIO.cleanup()

if __name__ == "__main__":
    skull = SpookySkull()
    skull.start()


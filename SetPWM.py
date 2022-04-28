import RPi.GPIO as GPIO   # Import the GPIO library.
import time               # Import time library


class SetPWM:
    def __init__(self):
        # Set Pi to use pin number when referencing GPIO pins.
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)  # Set GPIO pin 12 to output mode.
        # Initialize PWM on pwmPin 100Hz frequency
        self.pwm = GPIO.PWM(18, 100)
        self.Ontime = int(1024 * 0.09777)  # set dc variable to 0 for 0%
        # print(self.Ontime)
        self.pwm.start(50)
        # self.led_brightness(0)

    def led_brightness(self, value):
        self.Ontime = value
        if self.Ontime == 0:
            self.Ontime = 0
        else:
            if self.Ontime < 400:
                self.Ontime = 100
            if 1025 > self.Ontime > 400:
                self.Ontime = (int)(self.Ontime/10.24)
                self.Ontime = 100 - self.Ontime
                self.Ontime = self.Ontime + 10
            if self.Ontime > 1024:
                self.Ontime = 20
        #print('Brightness Done' + str(self.Ontime))

        self.pwm.ChangeDutyCycle(self.Ontime)
        time.sleep(0.05)

    def endprogram(self):
        self.pwm.stop()

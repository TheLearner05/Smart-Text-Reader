from operator import index
import RPi.GPIO as GPIO
import time


class SPIConfig:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(9, GPIO.IN)  # MISO
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(8, GPIO.OUT)
        GPIO.output(11, GPIO.HIGH)  # CLK
        GPIO.output(8, GPIO.HIGH)  # CS
        self._Continue = False
        self.index = 0
        self.BitArr = [1, 2, 4, 8, 16, 32, 64, 128, 256,
                       512, 1024, 2048, 4096, 8162, 16384, 32768]
        self.ADC_Value = 0
        self.ADC_Arr = []

    def AmbientLightVal(self):
        self.ADC_Value = 0
        self._Continue = True
        while self._Continue:
            GPIO.output(8, GPIO.LOW)
            GPIO.output(11, GPIO.LOW)
            time.sleep(0.002)
            GPIO_Value = GPIO.input(9)
            if GPIO_Value:
                self.ADC_Value |= self.BitArr[self.index]
            self.index += 1
            GPIO.output(11, GPIO.HIGH)
            time.sleep(0.002)
            if self.index > 15:
                self.index = 0
                self.ADC_Value = self.ADC_Value
                self.ADC_Arr.append(self.ADC_Value)
                # print(self.ADC_Value)
                self._Continue = False
            GPIO.output(8, GPIO.HIGH)
            time.sleep(0.002)
        return self.ADC_Value

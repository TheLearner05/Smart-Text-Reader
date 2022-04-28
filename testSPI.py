# spitest.py
# A brief demonstration of the Raspberry Pi SPI interface, using the Sparkfun
# Pi Wedge breakout board and a SparkFun Serial 7 Segment display:
# https://www.sparkfun.com/products/11629

import time
import spidev

# We only have SPI bus 0 available to us on the Pi
bus = 0

#Device is the chip select pin. Set to 0 or 1, depending on the connections
device = 0

# Enable SPI
spi = spidev.SpiDev()
spi.open(bus, device)
# Open a connection to a specific bus and device (chip select pin)


# Set SPI speed and mode
spi.max_speed_hz = 7629
spi.mode = 1




# Turn on one segment of each character to show that we can
# address all of the segments
i = 1
while i < 100:

    # The decimals, colon and apostrophe dots
    
    valueLow = spi.xfer2([0x01])
    #print(result)
    time.sleep(.001)
    result = valueLow[0]
    #print(valueLow[0])
    valueHigh = spi.xfer2([0x01])
    #result |=  valueHigh[0] <<8
    #print(valueHigh[0])
    print(result)
    time.sleep(1)
    i = i+1


# Clear display again

print("Test completed")

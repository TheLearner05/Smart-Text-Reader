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
spi.mode = 0

# Clear display
msg = [0xAA] #76
spi.xfer(msg)

time.sleep(5)

# Turn on one segment of each character to show that we can
# address all of the segments
i = 1
temp_result = []
while i < 11:

    # The decimals, colon and apostrophe dots
    msg = [0x00]
    #msg.append(i)s

    temp_result.append (spi.xfer2(msg))
   
    temp_result.append(spi.xfer2(msg))
    #result |= (result_L[0] << 8)
    # Increment to next segment in each character
    i = i + 1

    # Pause so we can see them
    time.sleep(1)

    print(temp_result)




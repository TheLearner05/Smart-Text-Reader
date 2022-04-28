import picamera
#from picamera import mmal, mmalobj as mo
from time import sleep

# create object for PiCamera class

camera = picamera.PiCamera()
# camera.stop_preview()
# sleep(5)
camera.start_preview()
sleep(5)
camera.stop_preview()

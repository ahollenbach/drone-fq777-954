from dronecontrol import DroneControl
from dronevideo import DroneVideo
import time
import os
#from cStringIO import StringIO
#from StringIO import StringIO
from io import BytesIO as StringIO

from opencvtest import decode

import logging
logging.basicConfig(level=logging.DEBUG)

RUNTIME = 10
video = DroneVideo()
drone = DroneControl()
drone.connect()
start = time.time()
stopTime = start+RUNTIME

lasttime = start

data = StringIO()


while( time.time() < stopTime):
    try:
        drone.cmd(t=20)

        newdata = video.fetch_video()
        if newdata is not None:
            data.write(newdata)
        print( time.time() - lasttime, time.time() - start)
        lasttime = time.time()
    except Exception as e:
        print(e)
        print("fuck! reconnecting!")
        video.reconnect()
        drone.reconnect()


#decode(data)
with open("stream.mp4",'wb') as f:
    f.write(data.getvalue())

decode("stream.mp4")
print("run for ", time.time() - start)

drone.stop()
drone.disconnect()

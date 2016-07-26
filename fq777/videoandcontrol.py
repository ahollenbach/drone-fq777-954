from dronecontrol import DroneControl
from dronevideo import DroneVideo
import time
import os

from opencvtest import decode

RUNTIME = 180
video = DroneVideo()
drone = DroneControl()
drone.connect()
start = time.time()
stopTime = start+RUNTIME

lasttime = start
while( time.time() < stopTime):
    try:
        drone.cmd(t=20)

        newdata = video.fetch_video()
        if newdata is not None:
            with open("last.mp4", 'ab') as f:
                f.write(newdata)

        frames = decode("last.mp4")
        if frames > 3:
            videobuffer = ""
            os.remove('last.mp4')


        print( time.time() - lasttime, time.time() - start)
        lasttime = time.time()
    except:
        print("fuck! reconnecting!")
        video.reconnect()
        drone.reconnect()


print("run for ", time.time() - start)

drone.stop()
drone.disconnect()

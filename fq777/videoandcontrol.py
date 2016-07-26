from dronecontrol import DroneControl
from dronevideo import DroneVideo
import time

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
        video.fetch_video()
        print time.time() - lasttime, time.time() - start
        lasttime = time.time()
    except:
        print("fuck! reconnecting!")
        video.reconnect()
        drone.reconnect()


print("run for ", time.time() - start)

drone.stop()
drone.disconnect()

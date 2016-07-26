import av
import cv2
import time

lastFrame = -1

def decode(data):
    try:
        container = av.open(data, 'r', 'h264')
    except:
        return 0
    video = next(s for s in container.streams if s.type == b'video')
    frames = 0

    for packet in container.demux(video):
        try:
            for frame in packet.decode():
                time.sleep(0.01)
                cv2.imshow('frame',frame.to_nd_array(format='bgr24'))
                frames+=1
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        except av.AVError as e:
            print(e)
    return frames

if __name__ == "__main__":
    decode("fpv.mp4")

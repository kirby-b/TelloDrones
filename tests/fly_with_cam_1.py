# This script turns on and shows the drone camera
import cv2
from djitellopy import tello
from time import sleep
import threading

# Initialize drone
drone = tello.Tello()

def show_camera_frames():
    # Shows the camera frames through cv2
    while True:
        frame = drone.get_frame_read().frame
        cv2.imshow("Frame", frame)
        # While it is running, cv2 gets the current frame on the camera and outputs it to a window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

def movement():
    sleep(4)
    drone.move_up(60)
    sleep(7)
    drone.move_down(60)
    sleep(7)
    # moves up then down to see if the camera can handle it
    drone.land()
    # lands


def main():
    # Connect to drone
    drone.connect()
    # Turn on drone cam so we can get frames
    sleep(1)
    drone.takeoff()
    sleep(3)
    # Takes off
    drone.streamon()
    # Call the cv camera function thread so we actually see the drone cam
    t1 = threading.Thread(target=show_camera_frames, args=())
    # Makes the drone move so its not just a still image
    t2 = threading.Thread(target=movement, args=())
 
    t1.start()
    t2.start()
    # Starts the threads
 
    t1.join()
    t2.join()
    
    drone.streamoff()
    drone.end()


if __name__ == "__main__":
    main()
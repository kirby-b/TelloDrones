# This script turns on and shows the drone camera
import cv2
from djitellopy import tello
from time import sleep
import threading


def show_camera_frames(drone):
    # Shows the camera frames through cv2
    while True:
        frame = drone.get_frame_read().frame
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    drone.end()

def movement(drone):
    sleep(1)
    drone.rotate_counter_clockwise(90)
    sleep(6)
    drone.rotate_clockwise(90)
    sleep(6)
    # rotates back and forth
    drone.land()
    # lands
    drone.end()


def main():
    # Initialize drone
    drone = tello.Tello()
    # Connect to drone
    drone.connect()
    # Turn on drone cam
    drone.query_battery()
    # gets the battery percent
    sleep(1)
    drone.takeoff()
    sleep(3)
    # Takes off
    drone.streamon()
    # Call the cv camera function
    show_camera_frames(drone)
    t1 = threading.Thread(target=show_camera_frames, args=(drone))
    t2 = threading.Thread(target=movement, args=(drone))
 
    t1.start()
    t2.start()
 
    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
# This script turns on and shows the drone camera
import cv2
from djitellopy import tello


def show_camera_frames(drone):
    # Shows the camera frames through cv2
    while True:
        frame = drone.get_frame_read().frame
        cv2.imshow("Frame", frame)
        # While it is running, cv2 gets the current frame on the camera and outputs it to a window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    drone.end()


def main():
    # Initialize drone
    drone = tello.Tello()
    # Connect to drone. You dont need to sleep after 
    # connecting usually when using non flight commands
    drone.connect()
    # Turn on drone cam
    drone.streamon()
    # Call the cv camera function
    show_camera_frames(drone)


if __name__ == "__main__":
    main()

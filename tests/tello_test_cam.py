import cv2
from djitellopy import tello

def show_camera_frames(drone):
    # Shows the camera frames through cv2
    while True:
        frame = drone.get_frame_read().frame
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    drone.end()

def main():
    # Initialize drone
    drone = tello.Tello()
    # Connect to drone
    drone.connect()
    # Turn on drone cam
    drone.streamon()
    # Call the cv camera function
    show_camera_frames(drone)

if __name__ == "__main__":
    main()
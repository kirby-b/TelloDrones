# This script is a faster version of 5 with an added function that makes the drone fly in a square. 
# This was both for stress testing and making sure you can use user defined functions
from djitellopy import tello
from time import sleep

drone = tello.Tello()


def main():
    drone.connect()
    sleep(1)
    # connects and sleeps to ensure it is ready
    sleep(1)
    drone.takeoff()
    sleep(4)
    # takes off
    drone.set_speed(60)
    sleep(5)
    # Sets speed
    for i in range(5):
        drone.flip("l")
        sleep(6)
        drone.rotate_clockwise(360)
        sleep(5)
        square()
    # flips the drone left and does a 360 clockwise 5 times
    # It sleeps in between each so the drone doesnt error
    for i in range(5):
        drone.flip("r")
        sleep(6)
        drone.rotate_counter_clockwise(360)
        sleep(5)
        square()
    # flips the drone left and does a 360 counter-clockwise 5 times
    # It sleeps in between each so the drone doesnt error
    drone.land()
    # lands
    drone.end()


def square():
    for i in range(4):
        drone.rotate_clockwise(90)
        sleep(6)
        drone.move_forward(100)
        sleep(6)
    # Flies in a square by turning 90 degrees and moving forward 4 times
    # It sleeps in between each so the drone doesnt error


if __name__ == "__main__":
    main()

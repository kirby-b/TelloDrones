# Faster version of 5 wth some extras
from djitellopy import tello
from time import sleep

drone = tello.Tello()


def main():
    drone.connect()
    sleep(1)
    # connects
    drone.query_battery()
    # gets the battery percent
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
    for i in range(5):
        drone.flip("r")
        sleep(6)
        drone.rotate_counter_clockwise(360)
        sleep(5)
        square()
    # flips the drone left and does a 360 counter-clockwise 5 times
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

if __name__ == "__main__":
    main()
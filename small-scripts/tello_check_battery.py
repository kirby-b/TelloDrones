from djitellopy import tello

drone = tello.Tello()

drone.connect()
# Connects to the drone

drone.query_battery()
# gets the battery percent

drone.end()
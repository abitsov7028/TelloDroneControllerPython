from djitellopy import Tello
import keyboard
import cv2
import time

# Connect to Tello drone
tello = Tello()
tello.connect()

# Set up keyboard controls
keyboard.add_hotkey('w', lambda: tello.move_forward(30))
keyboard.add_hotkey('s', lambda: tello.move_back(30))
keyboard.add_hotkey('a', lambda: tello.move_left(30))
keyboard.add_hotkey('d', lambda: tello.move_right(30))
keyboard.add_hotkey('space', lambda: tello.takeoff())
keyboard.add_hotkey('esc', lambda: tello.land())

# Set up video stream
tello.streamon()
video_capture = cv2.VideoCapture('udp://0.0.0.0:11111')

# Keep the program running
while True:
    ret, frame = video_capture.read()
    cv2.imshow('Tello Video Feed', frame)

    # Break the loop when 'esc' key is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release resources
video_capture.release()
cv2.destroyAllWindows()

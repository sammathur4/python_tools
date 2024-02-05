import time
import cv2
import mediapipe as mp
import pyautogui
import threading
import sys
from collections import deque

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

mp_drawing = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Webcam not found.")
    sys.exit(1)

delay_time = 0.5
gesture_queue = deque(maxlen=5)  # Keep a sliding window of the last 5 detected gestures
switching_tabs = False


def detect_swipe_direction(landmarks):
    thumb_x = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
    pinky_x = landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x

    return "left" if thumb_x > pinky_x else "right"


def switch_tab(direction):
    global switching_tabs
    switching_tabs = True

    if direction == "right":
        print("Going right")
        pyautogui.hotkey("alt", "tab")
        time.sleep(delay_time)

    elif direction == "left":
        print("Going left")
        pyautogui.hotkey("shift", "alt", "tab")
        time.sleep(delay_time)

    switching_tabs = False


def process_gesture_queue():
    global gesture_queue
    while cap.isOpened():
        if not switching_tabs and gesture_queue:
            swipe_direction = gesture_queue.popleft()
            threading.Thread(target=switch_tab, args=(swipe_direction,)).start()

        time.sleep(0.1)  # Adjust sleep time as needed


def gesture_recognition():
    global switching_tabs, gesture_queue
    hand_landmarks_window = deque(
        maxlen=5
    )  # Keep a sliding window of the last 5 hand landmarks
    while cap.isOpened():
        ret, frame = cap.read()

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                hand_landmarks_window.append(landmarks)
                if len(hand_landmarks_window) == hand_landmarks_window.maxlen:
                    current_hand_landmarks = hand_landmarks_window[-1]
                    swipe_direction = detect_swipe_direction(current_hand_landmarks)
                    gesture_queue.append(swipe_direction)

                handedness = (
                    results.multi_handedness[
                        results.multi_hand_landmarks.index(landmarks)
                    ]
                    .classification[0]
                    .label
                )
                mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow("Gesture Recognition", frame)

        key = cv2.waitKey(10)
        if key & 0xFF == ord("q"):
            clean_exit()

    clean_exit()


def clean_exit():
    cap.release()
    cv2.destroyAllWindows()
    print("Program terminated.")
    sys.exit(0)


# Start gesture recognition
gesture_thread = threading.Thread(target=gesture_recognition)
gesture_thread.start()

# Start gesture processing thread
processing_thread = threading.Thread(target=process_gesture_queue)
processing_thread.start()

# Wait for gesture recognition thread to finish
gesture_thread.join()

# Wait for gesture processing thread to finish
processing_thread.join()

# Release resources
clean_exit()

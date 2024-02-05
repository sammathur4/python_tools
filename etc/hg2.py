import time
import cv2
import mediapipe as mp
import pyautogui
import threading
import sys

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

mp_drawing = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Webcam not found.")
    sys.exit(1)

prev_x = None
prev_y = None

# Set the delay time in seconds (configurable)
delay_time = 0.5  # You can adjust this value based on your preference

# Variable to check if tab switching is in progress
switching_tabs = False


def detect_swipe_direction(landmarks):
    thumb_x = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
    pinky_x = landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x

    # Determine handedness based on x-coordinate of thumb and pinky
    if thumb_x > pinky_x:
        handedness = "left"
    else:
        handedness = "right"

    return handedness


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


def gesture_recognition():
    global switching_tabs
    while cap.isOpened():
        ret, frame = cap.read()

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                handedness = (
                    results.multi_handedness[
                        results.multi_hand_landmarks.index(landmarks)
                    ]
                    .classification[0]
                    .label
                )

                mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

                index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                middle_tip = landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                ring_tip = landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
                pinky_tip = landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
                thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

                # Add conditions for only the index and middle fingers to be raised
                condition_fulfilled = (
                    index_tip.y < middle_tip.y
                    and ring_tip.y > middle_tip.y
                    and pinky_tip.y > middle_tip.y
                    and thumb_tip.y > middle_tip.y
                )

                print(index_tip.y, middle_tip.y, ring_tip.y, thumb_tip.y)

                if not switching_tabs and condition_fulfilled:
                    swipe_direction = detect_swipe_direction(landmarks)
                    if swipe_direction:
                        threading.Thread(
                            target=switch_tab, args=(swipe_direction,)
                        ).start()

        cv2.imshow("Gesture Recognition", frame)

        if cv2.waitKey(10) & 0xFF == ord("q"):
            clean_exit()

    clean_exit()


def gesture_recognition_og():
    global switching_tabs
    while cap.isOpened():
        ret, frame = cap.read()

        # mirror image
        frame = cv2.flip(frame, 1)

        # Convert to rgb
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                handedness = (
                    results.multi_handedness[
                        results.multi_hand_landmarks.index(landmarks)
                    ]
                    .classification[0]
                    .label
                )

                mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

                index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                index_mid = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP]

                # Check for index finger raised and swipe gesture
                if not switching_tabs and index_tip.y < index_mid.y:
                    swipe_direction = detect_swipe_direction(landmarks)
                    if swipe_direction:
                        threading.Thread(
                            target=switch_tab, args=(swipe_direction,)
                        ).start()

        cv2.imshow("Gesture Recognition", frame)

        if cv2.waitKey(10) & 0xFF == ord("q"):
            clean_exit()

    clean_exit()


def clean_exit():
    cap.release()
    cv2.destroyAllWindows()
    print("Program terminated.")
    sys.exit(0)


# Start gesture recognition thread
gesture_thread = threading.Thread(target=gesture_recognition)
gesture_thread.start()

# Wait for gesture recognition thread to finish
gesture_thread.join()

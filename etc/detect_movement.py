import time
import cv2
import mediapipe as mp
import pyautogui
import threading

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

mp_drawing = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()

cap = cv2.VideoCapture(0)
prev_x = None
prev_y = None

# Set the delay time in seconds
delay_time = 1  # You can adjust this value based on your preference

# Variable to check if tab switching is in progress
switching_tabs = False


def switch_tab(direction):
    global switching_tabs
    switching_tabs = True
    if direction == "right":
        print("Going right")
        pyautogui.hotkey('alt', 'tab')

    elif direction == "left":
        print('Going left')
        pyautogui.hotkey('shift', 'alt', 'tab')

    switching_tabs = False


def gesture_recognition():
    global switching_tabs
    while cap.isOpened():
        ret, frame = cap.read()

        # mirror image
        frame = cv2.flip(frame, 1)

        # Convert to rgb --bgr is cv ka default...convert to rgb bcs mediapipe rgb me operate krta hai
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)  # hand landmarks detect krne ko
        if results.multi_hand_landmarks:  # agar hands detect hue to
            for landmarks in results.multi_hand_landmarks:
                # hand check krne ko
                handedness = results.multi_handedness[results.multi_hand_landmarks.index(landmarks)].classification[
                    0].label

                mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)
                # draws hand landmarks and connections on the frame
                index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                index_mid = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP]

                print(handedness)
                if handedness == "Right" and not switching_tabs:  # left mouse
                    threading.Thread(target=switch_tab, args=("right",)).start()

                if handedness == "Left" and not switching_tabs:  # left mouse
                    threading.Thread(target=switch_tab, args=("left",)).start()

        cv2.imshow("Gesture Recognition", frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# Start gesture recognition thread
gesture_thread = threading.Thread(target=gesture_recognition)
gesture_thread.start()

# Wait for gesture recognition thread to finish
gesture_thread.join()

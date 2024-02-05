import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(rgb_frame)

    # Check if hands are detected
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Extract hand landmarks
            for point, landmark in enumerate(landmarks.landmark):
                height, width, _ = frame.shape
                cx, cy = int(landmark.x * width), int(landmark.y * height)
                cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)

        # You can implement hand gesture recognition logic here
        # For example, based on the position of landmarks

    # Display the frame
    cv2.imshow("Hand Gesture Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

# Release the capture and destroy windows
cap.release()
cv2.destroyAllWindows()

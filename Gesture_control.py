import cv2
import mediapipe as mp
import pyautogui
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

position_buffer = []
buffer_size = 10  # Number of frames to calculate mean position

swipe_threshold = 0.15  # Adjust based on screen size and sensitivity

cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Ignoring empty camera frame.")
            continue

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        h, w, _ = frame.shape

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                curr_x, curr_y = hand_landmarks.landmark[8].x, hand_landmarks.landmark[8].y

                position_buffer.append((curr_x, curr_y))
                if len(position_buffer) > buffer_size:
                    position_buffer.pop(0)  # Keep only the most recent positions

                if len(position_buffer) == buffer_size:
                    mean_x = np.mean([pos[0] for pos in position_buffer])
                    mean_y = np.mean([pos[1] for pos in position_buffer])

                    # Calculate deltas relative to the mean position
                    delta_x = curr_x - mean_x
                    delta_y = curr_y - mean_y

                    if delta_x < -swipe_threshold:
                        cv2.putText(frame, "Swipe Left", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        pyautogui.hotkey('alt', 'left')  # Trigger previous page/tab
                        position_buffer.clear()  # Clear buffer to reset mean position

                    elif delta_x > swipe_threshold:
                        cv2.putText(frame, "Swipe Right", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
                        pyautogui.hotkey('alt', 'right')  # Trigger next page/tab
                        position_buffer.clear()

                    elif delta_y < -swipe_threshold:
                        cv2.putText(frame, "Swipe Up", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                        pyautogui.scroll(300)  # Scroll up
                        position_buffer.clear()

                    elif delta_y > swipe_threshold:
                        cv2.putText(frame, "Swipe Down", (10, 190), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                        pyautogui.scroll(-300)  # Scroll down
                        position_buffer.clear()

        cv2.imshow('Swipe Gesture Control', frame)

        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

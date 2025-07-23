import cv2
import mediapipe as mp
import pyautogui
pyautogui.click()        # Left click
pyautogui.rightClick()# Right click
pyautogui.mouseDown()   # Hold click # move your hand (pointer moves)
pyautogui.mouseUp()   # Release click

pyautogui.scroll(20)   # Scroll up
pyautogui.scroll(-20)  # Scroll down

  
# Initialize hand detection
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

# Screen size
screen_w, screen_h = pyautogui.size()

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Flip for mirror effect
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # Extract landmark 8 (index finger tip) and 4 (thumb tip)
            lmList = []
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((id, cx, cy))

            if lmList:
                x1, y1 = lmList[8][1:]   # Index finger tip
                x2, y2 = lmList[4][1:]   # Thumb tip

                # Draw circle on index finger tip
                cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)

                # Move mouse
                screen_x = int((x1 / w) * screen_w)
                screen_y = int((y1 / h) * screen_h)
                pyautogui.moveTo(screen_x, screen_y)

                # If index and thumb are close → click
                if abs(x1 - x2) < 30 and abs(y1 - y2) < 30:
                    pyautogui.click()
                    cv2.circle(img, (x1, y1), 15, (0, 255, 0), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Virtual Mouse", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

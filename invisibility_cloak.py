import cv2
import numpy as np
import time

def get_background(cap, num_frames=40, delay=0.05):
    frames = []
    for _ in range(num_frames):
        ret, frame = cap.read()
        if not ret:
            continue
        frame = cv2.flip(frame, 1)
        frames.append(frame)
        time.sleep(delay)
    return np.median(np.array(frames), axis=0).astype(np.uint8)

cap = cv2.VideoCapture(0)

print("Capturing background, please stay out of the frame...")
time.sleep(2)
background = get_background(cap)
print("Background captured. Press 'q' or ESC to quit.")

# HSV ranges for maroon (dark reddish-brown)
# You may need to tweak depending on lighting and exact shade
lower_maroon1 = np.array([0, 100, 20])    # darker reds
upper_maroon1 = np.array([10, 255, 150])
lower_maroon2 = np.array([160, 100, 20])  # wraparound reds
upper_maroon2 = np.array([180, 255, 150])

kernel = np.ones((3, 3), np.uint8)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Apply maroon ranges
    mask1 = cv2.inRange(hsv, lower_maroon1, upper_maroon1)
    mask2 = cv2.inRange(hsv, lower_maroon2, upper_maroon2)
    mask = mask1 | mask2

    # Clean up
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=1)
    inv_mask = cv2.bitwise_not(mask)

    cloak_area = cv2.bitwise_and(background, background, mask=mask)
    non_cloak_area = cv2.bitwise_and(frame, frame, mask=inv_mask)
    final = cv2.addWeighted(cloak_area, 1, non_cloak_area, 1, 0)

    cv2.imshow("Invisibility Cloak (Maroon)", final)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        break

cap.release()
cv2.destroyAllWindows()

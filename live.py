import cv2
from names import color_name

cap = cv2.VideoCapture(0)

while True:
    ok, frame = cap.read()
    if not ok:
        break

    frame = cv2.flip(frame, 1)                  
    h, w = frame.shape[:2]
    cx, cy = w // 2, h // 2                     

    
    patch = frame[cy-5:cy+6, cx-5:cx+6]
    b, g, r = patch.mean(axis=(0, 1))
    name = color_name(int(b), int(g), int(r))

    cv2.circle(frame, (cx, cy), 10, (255, 255, 255), 2)
    cv2.putText(frame, name, (cx + 20, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 4)
    cv2.putText(frame, name, (cx + 20, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("ChromaLens", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
import cv2
from names import color_name

img = cv2.imread("IMG_1450-1536x1024.webp")     
img = cv2.resize(img, (960, 640))               
display = img.copy()

def on_click(event, x, y, flags, param):
    global display
    if event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = img[y, x]
        name = color_name(int(b), int(g), int(r))
        display = img.copy()
        cv2.circle(display, (x, y), 8, (255, 255, 255), 2)
        cv2.putText(display, name, (x + 15, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 4)
        cv2.putText(display, name, (x + 15, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

cv2.namedWindow("ChromaLens")
cv2.setMouseCallback("ChromaLens", on_click)

while True:
    cv2.imshow("ChromaLens", display)
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
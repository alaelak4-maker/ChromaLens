import cv2

frame = cv2.imread("IMG_1450-1536x1024.webp")    

if frame is None:
    print("Image not found. Check the filename and folder.")
    exit()

print(frame.shape, frame.dtype)

cv2.imshow("image", frame)              
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
from google.colab.patches import cv2_imshow

def detect(num):
    if (num < 0.5):
        print("有戴口罩")
        img = cv2.imread("good.jpg")
        cv2_imshow(img)
    elif (num > 0.65):
        print("沒戴口罩")
        img = cv2.imread("bad.jpg")
        cv2_imshow(img)
    else:
        print("無法判斷")
        img = cv2.imread("dontknow.jpg")
        cv2_imshow(img)
    
import cv2
import glob

images = ["face_detect\\baby2.png", "face_detect\\news.jpg",
          "face_detect\\photo.jpg", "face_detect\\resized_me.jpg", "face_detect\\image_me.jpg",
          "face_detect\\2.jpg", "face_detect\\cats.jpg",
          "face_detect\\3.jpg", "face_detect\\4.jpg", "face_detect\\many.jpg"]

png = glob.glob("face_detect\\*.png")

jpg = glob.glob("aa\\*.jpg")


def detect_image(img):
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = cascade.detectMultiScale(img,
                                     scaleFactor=1.15,
                                     minNeighbors=5)

    for x, y, w, h in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3)

    print(faces)

    cv2.imshow("Photo", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


for image in jpg:
    img = cv2.imread(image)

    if img.shape[0] > 800 and img.shape[1] > 800:
        resize = cv2.resize(img, (int(img.shape[1] / 10), int(img.shape[0] / 10)))
        #        cv2.imwrite("resized_" + image, resize)
        detect_image(resize)
        print(img.shape)
    else:
        #    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #    resized_img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))
        print(img.shape)
        detect_image(img)

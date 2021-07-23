import cv2


def single(image):
    # Loading image
    image = cv2.imread(image)

    print(image)
    print(image.ndim)
    print(image.shape)

    # resizing the image
    resize = cv2.resize(image, (int(image.shape[1] / 9), int(image.shape[0] / 9)))

    # Writing the image i.e. creating a new image
    cv2.imwrite("resized_me.jpg", resize)

    # Display the image
    cv2.imshow("image", resize)
    print(resize.shape)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    return resize


def multiple_image():
    import glob
    images = glob.glob("images\\*.jpg")

    for image in images:
        img = cv2.imread(image, 1)
        print(img.shape)
        #        resize = cv2.resize(img, (200, 200))
        #        cv2.imshow("image", resize)
        cv2.imshow("color_img", img)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
#        cv2.imwrite("gray_" + image, img)
        print(type(image))

multiple_image()
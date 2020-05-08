import numpy as np
import cv2
from sklearn.preprocessing import OneHotEncoder


# tables to store captured images and assigned letter
images_x = []
images_y = []

# auxilary list of possible values required for the OneHotEncoder to work as we want
signs_categories = ([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],)

# dictionary of ASCII values representing specific letters to encode
letters_dict = {
    97: 0,
    98: 1,
    99: 2,
    100: 3,
    101: 4,
    102: 5,
    103: 6,
    104: 7,
    105: 8,
    106: 8,
    107: 9,
    108: 10,
    109: 11,
    110: 12,
    111: 13,
    112: 14,
    113: 15,
    114: 16,
    115: 17,
    116: 18,
    117: 19,
    118: 20,
    119: 21,
    120: 22,
    121: 23
}

# OpenCV capturing video
cap = cv2.VideoCapture(0)

# collecting images from the camera and assigned letters
while(True):

    # Capture frame-by-frame
    ret, frame = cap.read()

    #### camera configuration - may require manual changes in order
    #### to find best cropping for your computer/camera

    # cropping the area that we capture with the camera
    crop = frame[0:500, 0:500]

    # setting up mirrored preview for ease of use
    preview_img = crop
    preview_img = cv2.flip(preview_img,1)

    # preparing images that we want to process
    process_img = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    process_img = cv2.resize(process_img,(100,100))

    # displaying the preview frame
    cv2.imshow("video_capture_window",preview_img)

    # setting up esc key to end the collecting of images
    k = cv2.waitKey(1)
    if k%256 == 27:
        break

    # only small caps letters to be recorded - using ASCII codes and letters dictionary defined earlier
    if 96 < k < 122:
        images_x.append(process_img)
        images_y.append([letters_dict[k]])


# after images are collected and in memory creating approriate input-output training data for the model
x_train = np.array(images_x)
x_train = x_train.reshape(-1,100,100,1)
y_train = np.array(images_y)
y_train = OneHotEncoder(categories=signs_categories).fit_transform(y_train.reshape(-1,1)).toarray()

# saving it as a separate file to be used by the training module
np.save('data/x_train.npy', x_train)
np.save('data/y_train.npy', y_train)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
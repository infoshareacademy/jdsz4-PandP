import numpy as np
import pandas as pd
import numpy as np

import tensorflow as tf
import os.path as path
import tensorflow.keras as keras
import matplotlib.pyplot as plt
import cv2
import time


##########################
##### WAŻNE - PONIŻSZE 2 LINIJKI MUSZĄ BYĆ "WŁĄCZONE: JESLI KORZYSTAMY Z GPU
##### JEŚLI CPU - CHYBA TRZEBA TO WYKOMENTOWAĆ

# physical_devices = tf.config.experimental.list_physical_devices('GPU')
# tf.config.experimental.set_memory_growth(physical_devices[0], enable=True)


def interpretation(y_pred):
    y_dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'k', 10: 'l',
              11: 'm', 12: 'n', 13: 'o', 14: 'p', 15: 'q', 16: 'r', 17: 's', 18: 't', 19: 'u', 20: 'v',
              21: 'w', 22: 'x', 23: 'y'}

    i = np.argmax(y_pred)
    if np.max(y_pred) > 0.95:
        return y_dict[i]
    else:
        return ' '


# wczytanie wytrenowanego modelu

saved_file = 'trained_model_user.h5'
loaded_model = keras.models.load_model(saved_file)


def predict_letter(img):
    tmpImg = img / 255.0
    tmpImg = tmpImg.reshape(1,img.shape[0],img.shape[1],1)
    predict = loaded_model.predict(tmpImg)
    return interpretation(predict)



cap = cv2.VideoCapture(0)
#img_counter = 0
images = []
# font definition
font = cv2.FONT_HERSHEY_SIMPLEX
# org
org = (50, 50)
# fontScale
fontScale = 2
# Blue color in BGR
color = (115, 172, 53)
# Line thickness of 2 px
thickness = 2
# Using cv2.putText() method
while(True):

    # Capture frame-by-frame
    ret, frame = cap.read()

    ################ KONFIGURACJA KAMERKI - PEWNIE U KAŻDEGO INACZEJ CROP #########

    # cropping the area that we capture with the camera
    crop = frame[0:500, 0:500]

    ###################################

    preview_img = crop
    preview_img = cv2.flip(preview_img,1)
    # preparing images that we want to process
    process_img = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    process_img = cv2.resize(process_img,(100,100))

    # using model to predict the letter
    onScreenText = predict_letter(process_img)




    #onScreenText = 'B'
    # preparing preview
    preview_img = cv2.putText(preview_img, onScreenText, org, font,
                   fontScale, color, thickness, cv2.LINE_AA)
    # displaying the preview frame
    cv2.imshow("video_capture_window",preview_img)
    # esc key to end the whole thing
    k = cv2.waitKey(1)
    if k%256 == 27:
        cap.release()
        cv2.destroyAllWindows()
        break
    if k%256 == 32:
        # img_name = "opencv_frame_{}.png".format(img_counter)
        # cv2.imwrite(img_name, img)
        # print("{} written!".format(img_name))
        # img_counter += 1
        images.append(process_img)
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

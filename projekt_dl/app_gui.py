from tkinter import *
from tkinter import ttk
#from ttkthemes import themed_tk as tk
#from PIL import Image, ImageTk

import os.path as path
import tensorflow.keras as keras

import cv2
from sklearn.preprocessing import OneHotEncoder

import numpy as np

import tkinter.messagebox


version = 'v0.102'





############# definicje fukcji ##########


# pomocnicza z kursu tkinter
def doNothing():
    print("ok ok I won't...")


#pomocnicza funkcja sprawdzająca (w konsoli) czy została zapisana wartość globalnej zmiennej main_chosen
def run_magic():
    print("magic run")

####### pomocnicze zmienne listy itp #####################

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

saved_file = 'trained_model.h5'
loaded_model = keras.models.load_model(saved_file)


def predict_letter(img):
    tmpImg = img / 255.0
    tmpImg = tmpImg.reshape(1,img.shape[0],img.shape[1],1)
    predict = loaded_model.predict(tmpImg)
    return interpretation(predict)

def mainMain():
    cap = cv2.VideoCapture(0)

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
    while (True):

        # Capture frame-by-frame
        ret, frame = cap.read()

        ################ KONFIGURACJA KAMERKI - PEWNIE U KAŻDEGO INACZEJ CROP #########

        # cropping the area that we capture with the camera
        crop = frame[0:500, 0:500]

        ###################################

        preview_img = crop
        preview_img = cv2.flip(preview_img, 1)
        # preparing images that we want to process
        process_img = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        process_img = cv2.resize(process_img, (28, 28))

        # using model to predict the letter
        onScreenText = predict_letter(process_img)

        # onScreenText = 'B'
        # preparing preview
        preview_img = cv2.putText(preview_img, onScreenText, org, font,
                                  fontScale, color, thickness, cv2.LINE_AA)
        # displaying the preview frame
        cv2.imshow("video_capture_window", preview_img)
        # esc key to end the whole thing
        k = cv2.waitKey(1)
        if k % 256 == 27:
            cap.release()
            cv2.destroyAllWindows()
            break
        if k % 256 == 32:
            # img_name = "opencv_frame_{}.png".format(img_counter)
            # cv2.imwrite(img_name, img)
            # print("{} written!".format(img_name))
            # img_counter += 1
            images.append(process_img)
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def mainCollect():
    # tables to store captured images and assigned letter
    images_x = []
    images_y = []

    # auxilary list of possible values required for the OneHotEncoder to work as we want
    signs_categories = ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],)

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
    while (True):

        # Capture frame-by-frame
        ret, frame = cap.read()

        #### camera configuration - may require manual changes in order
        #### to find best cropping for your computer/camera

        # cropping the area that we capture with the camera
        crop = frame[0:500, 0:500]

        # setting up mirrored preview for ease of use
        preview_img = crop
        preview_img = cv2.flip(preview_img, 1)

        # preparing images that we want to process
        process_img = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        process_img = cv2.resize(process_img, (100, 100))

        # displaying the preview frame
        cv2.imshow("video_capture_window", preview_img)

        # setting up esc key to end the collecting of images
        k = cv2.waitKey(1)
        if k % 256 == 27:
            break

        # only small caps letters to be recorded - using ASCII codes and letters dictionary defined earlier
        if 96 < k < 122:
            images_x.append(process_img)
            images_y.append([letters_dict[k]])

    # after images are collected and in memory creating approriate input-output training data for the model
    x_train = np.array(images_x)
    x_train = x_train.reshape(-1, 100, 100, 1)
    y_train = np.array(images_y)
    y_train = OneHotEncoder(categories=signs_categories).fit_transform(y_train.reshape(-1, 1)).toarray()

    # saving it as a separate file to be used by the training module
    np.save('data/x_train.npy', x_train)
    np.save('data/y_train.npy', y_train)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def mainTrain():
    # path to the folder, where training data is stored
    rel_path = 'data'

    x_train = np.load(path.join(rel_path, 'x_train.npy'))
    y_train = np.load(path.join(rel_path, 'y_train.npy'))

    input_shape = x_train.shape[1:]
    out_shape = y_train.shape[1]

    base_model = keras.Sequential()
    base_model.add(keras.layers.Input(shape=(input_shape)))

    base_model.add(keras.layers.Conv2D(32, (3, 3)))
    base_model.add(keras.layers.Activation('relu'))
    base_model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))

    base_model.add(keras.layers.Conv2D(64, (3, 3)))
    base_model.add(keras.layers.Activation('relu'))
    base_model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))

    # the model so far outputs 3D feature maps (height, width, features)

    base_model.add(keras.layers.Flatten())  # this converts our 3D feature maps to 1D feature vectors
    base_model.add(keras.layers.Dense(100))
    base_model.add(keras.layers.Activation('relu'))
    base_model.add(keras.layers.Dropout(0.5))

    # base_model.add(keras.layers.Dense(64))
    # base_model.add(keras.layers.Activation('relu'))
    # base_model.add(keras.layers.Dropout(0.4))

    base_model.add(keras.layers.Dense(out_shape))
    base_model.add(keras.layers.Activation('sigmoid'))

    base_model.compile(loss='categorical_crossentropy',
                       optimizer=keras.optimizers.Adam(learning_rate=0.001),
                       metrics=['accuracy'])

    _batch_size = 128
    _epochs = 60
    _validation_split = 0.2

    base_model.fit(x_train, y_train, epochs=_epochs, batch_size=_batch_size, validation_split=_validation_split)

    base_model.save("trained_model_user.h5")

def mainUserModel():
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
        tmpImg = tmpImg.reshape(1, img.shape[0], img.shape[1], 1)
        predict = loaded_model.predict(tmpImg)
        return interpretation(predict)

    cap = cv2.VideoCapture(0)
    # img_counter = 0
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
    while (True):

        # Capture frame-by-frame
        ret, frame = cap.read()

        ################ KONFIGURACJA KAMERKI - PEWNIE U KAŻDEGO INACZEJ CROP #########

        # cropping the area that we capture with the camera
        crop = frame[0:500, 0:500]

        ###################################

        preview_img = crop
        preview_img = cv2.flip(preview_img, 1)
        # preparing images that we want to process
        process_img = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        process_img = cv2.resize(process_img, (100, 100))

        # using model to predict the letter
        onScreenText = predict_letter(process_img)

        # onScreenText = 'B'
        # preparing preview
        preview_img = cv2.putText(preview_img, onScreenText, org, font,
                                  fontScale, color, thickness, cv2.LINE_AA)
        # displaying the preview frame
        cv2.imshow("video_capture_window", preview_img)
        # esc key to end the whole thing
        k = cv2.waitKey(1)
        if k % 256 == 27:
            cap.release()
            cv2.destroyAllWindows()
            break
        if k % 256 == 32:
            # img_name = "opencv_frame_{}.png".format(img_counter)
            # cv2.imwrite(img_name, img)
            # print("{} written!".format(img_name))
            # img_counter += 1
            images.append(process_img)
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


################### definicja interfesju ############
'''
Tkinter opiera się o "ramki" - frames, w których upakowuje się poszczególne fragmentu interfejsu:
- przyciski
- pola tekstowe
- menu wybieralne
- slidery
- okienka inputu
i pewnie jeszce wiele innych

ramek może być wiele poziomów, sam stosuje poniżej "ramki w większych ramkach"

'''



# ***** GUI start *****


#root - główna, najbardziej zewnętrzna ramka, definiowana jako klasa ThemedTk (themed, zeby skorzystać z predefiniowanego styu)
# "okno programu, nazwa root wzięta z kursu"

root = tk.ThemedTk()
root.geometry('1000x600')
root.set_theme("clearlooks")




# ***** The Toolbar - górny pasek z przyciakami  *****

#pierwsza zewnętrzna ramka, umieszczamy ją w oknie 'root', "pakujemy" na górze
toolbar = ttk.Frame(root)
toolbar.pack(side = TOP)

#### poniżej definicja przycików używanych, które "pakujemy" w w ramce "toolbar"
#### w dalszej części na podobnej zasadzie są zdefiniowane i "upakowane" pozostałe elementy interfejsu

# *** toolbar buttons *****
insertButt = ttk.Button(toolbar, text="USE THE BUILT-IN MODEL", command=mainMain)
insertButt.pack(side=LEFT, padx=10, pady=10)

testButt = ttk.Button(toolbar, text="COLLECT OWN IMAGES", command=mainCollect)
testButt.pack(side=LEFT, padx=10, pady=10)

testButt = ttk.Button(toolbar, text="TRAIN YOUR MODEL", command=mainTrain)
testButt.pack(side=LEFT, padx=10, pady=10)

testButt = ttk.Button(toolbar, text="USE YOUR MODEL", command=mainUserModel)
testButt.pack(side=LEFT, padx=10, pady=10)

quitButt = ttk.Button(toolbar, text="Quit", command=root.quit)
quitButt.pack(side=RIGHT, padx=10, pady=10)



# ***** Status Bar *****

status = ttk.Label(root, text=f"PandP, ML_project, {version}", relief=GROOVE, anchor=W)

status.pack(side=BOTTOM, fill=X)



# "włączenie" programu, interfejs musi się zawierać pomiędzy "otwarciem" roota i jego "mainloop'em", trochę jak w html'u
root.mainloop()



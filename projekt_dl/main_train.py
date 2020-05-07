import pandas as pd
import numpy as np

import os.path as path
import tensorflow.keras as keras


# path to the folder, where training data is stored
rel_path = 'data'

x_train = np.load(path.join(rel_path,'x_train.npy'))
y_train = np.load(path.join(rel_path,'y_train.npy'))

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

# base_model.add(keras.layers.Conv2D(32, (3, 3)))
# base_model.add(keras.layers.Activation('relu'))
# base_model.add(keras.layers.MaxPooling2D(pool_size=(2, 2))) # the model so far outputs 3D feature maps (height, width, features)

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
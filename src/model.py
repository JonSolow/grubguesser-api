import numpy as np
from keras.utils.data_utils import get_file
from config import MODEL_HDF5_PATH


LABELS = np.loadtxt("labels.txt", dtype=object, delimiter="\n")

def initialize_model():
    # import the necessary packages
    from keras.models import Sequential
    from keras.layers import BatchNormalization
    from keras.layers.convolutional import Conv2D, MaxPooling2D
    from keras.layers.core import Flatten, Dropout, Dense

    # CONV => RELU => POOL
    cnn = Sequential()
    inputShape = (224, 224, 3)
    chanDim = -1
    classes = 101
    # Sequence of Convolution (scan filters), BatchNormalization (normalize numbers),
    #  MaxPooling (shrink tensor down), Dropout (prevent overfit)
    cnn.add(
        Conv2D(32, (3, 3), padding="same", input_shape=inputShape, activation="relu")
    )
    cnn.add(BatchNormalization(axis=chanDim))
    cnn.add(MaxPooling2D(pool_size=(3, 3)))
    cnn.add(Dropout(rate=0.25))
    cnn.add(Conv2D(64, (3, 3), padding="same", activation="relu"))
    cnn.add(BatchNormalization(axis=chanDim))
    cnn.add(Conv2D(64, (3, 3), padding="same", activation="relu"))
    cnn.add(BatchNormalization(axis=chanDim))
    cnn.add(MaxPooling2D(pool_size=(2, 2)))
    cnn.add(Dropout(rate=0.25))
    cnn.add(Conv2D(128, (3, 3), padding="same", activation="relu"))
    cnn.add(BatchNormalization(axis=chanDim))
    cnn.add(Conv2D(128, (3, 3), padding="same", activation="relu"))
    cnn.add(BatchNormalization(axis=chanDim))
    cnn.add(MaxPooling2D(pool_size=(2, 2)))
    cnn.add(Dropout(rate=0.25))
    cnn.add(Flatten())
    cnn.add(Dense(1024, activation="relu"))
    cnn.add(BatchNormalization())
    cnn.add(Dropout(rate=0.5))
    # softmax classifier
    cnn.add(Dense(classes, activation="softmax"))

    return cnn


CNN = initialize_model()


CNN.load_weights(
    get_file(
        "weights.hdf5",
        MODEL_HDF5_PATH,
    )
)

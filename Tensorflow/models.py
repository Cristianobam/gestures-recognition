import tensorflow as tf

def ConvBatch(shape=(100, 100, 3), momentum=.9):
    model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(64, (3,3), input_shape=shape, padding='same', activation='relu'),
    tf.keras.layers.Dropout(.2),
    tf.keras.layers.Conv2D(64, (3,3), padding='same', activation='relu'),
    tf.keras.layers.Dropout(.2),
    tf.keras.layers.BatchNormalization(momentum=momentum),
    tf.keras.layers.MaxPool2D(),
    tf.keras.layers.Conv2D(128, (3,3), padding='same', activation='relu'),
    tf.keras.layers.Dropout(.2),
    tf.keras.layers.Conv2D(128, (3,3), padding='same', activation='relu'),
    tf.keras.layers.Dropout(.2),
    tf.keras.layers.BatchNormalization(momentum=momentum),
    tf.keras.layers.MaxPool2D(),
    tf.keras.layers.Conv2D(256, (3,3), padding='same', activation='relu'),
    tf.keras.layers.Dropout(.2),
    tf.keras.layers.Conv2D(256, (3,3), padding='same', activation='relu'),
    tf.keras.layers.Dropout(.2),
    tf.keras.layers.BatchNormalization(momentum=momentum),
    tf.keras.layers.MaxPool2D(),
    tf.keras.layers.Conv2D(512, (3,3), padding='same', activation='relu'),
    tf.keras.layers.Dropout(.2),
    tf.keras.layers.Conv2D(512, (3,3), padding='same', activation='relu'),
    tf.keras.layers.Dropout(.2),
    tf.keras.layers.BatchNormalization(momentum=momentum),
    tf.keras.layers.GlobalAveragePooling2D()
    ])
    return model
    
def build_model(shape=(1, 100, 100, 3), n_classes = 3, convnet=None):
    assert convnet is not None, "Please, provide a build model function."
    convnet_model = convnet(shape[1:])
    model = tf.keras.Sequential([
        tf.keras.layers.TimeDistributed(convnet_model, input_shape=shape),
        tf.keras.layers.GRU(120, activation='relu'),
        tf.keras.layers.Dropout(.2),
        tf.keras.layers.Dense(60, activation='relu'),
        tf.keras.layers.Dropout(.2),
        tf.keras.layers.Dense(30, activation='relu'),
        tf.keras.layers.Dropout(.2),
        tf.keras.layers.Dense(n_classes, activation='softmax')
    ])
    return model

import os

os.environ["CUDA_VISIBLE_DEVICES"] = '0'
import tensorflow as tf
from tensorflow import keras
from keras import layers

# physical_devices = tf.config.list_physical_devices("GPU")
# tf.config.experimental.set_memory_growth(physical_devices[0], True)


def conv_layer(x, training, filters):
    # print('---------  is ', filters)
    x = layers.BatchNormalization()(x, training=training)
    x = layers.ReLU()(x)
    x = layers.Conv2D(
        filters,
        (3, 3),
        strides=[1, 1],
        padding='same',
        dilation_rate=[1, 1],
        activation=None,
        kernel_initializer=tf.keras.initializers.GlorotUniform(), )(x)
    x = layers.Dropout(0.2)(x)
    return x


def dense_block(x, training, block_nb, Filter):
    dense_out = []
    for i in range(block_nb):
        conv = conv_layer(x, training, Filter)
        # print('=============', x.shape)
        x = layers.concatenate([conv, x], 3)
        dense_out.append(conv)

    x = layers.concatenate(dense_out, 3)

    return x


class DoubleConv_encode(layers.Layer):
    def __init__(self, out_channels, block_nb):
        super(DoubleConv_encode, self).__init__()
        self.out_channels = out_channels
        self.block_nb = block_nb

    def call(self, input_tensor, training=True):
        x = dense_block(input_tensor, training, self.block_nb, self.out_channels)
        x = layers.concatenate([x, input_tensor], 3)
        return x


class DoubleConv_decode(layers.Layer):
    def __init__(self, out_channels, block_nb):
        super(DoubleConv_decode, self).__init__()
        self.out_channels = out_channels
        self.block_nb = block_nb

    def call(self, input_tensor, training=True):
        x = dense_block(input_tensor, training, self.block_nb, self.out_channels)
        return x


IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS = 512, 512, 1


class DesNet(layers.Layer):
    def __init__(self, out_chanals=1, features=(4, 8, 16, 32, 64, 128, 256, 512)):
        super(DesNet, self).__init__()
        Num_of_Desnet_layers = 2
        self.Num_of_Desnet_layers = Num_of_Desnet_layers
        self.ups = []
        self.downs = []
        self.features = features

        self.pool = layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2))
        for feature in features:
            self.downs.append(DoubleConv_encode(feature, Num_of_Desnet_layers))

        for feature in reversed(features):
            self.ups.append(
                layers.Conv2DTranspose(
                    filters=feature, kernel_size=3, strides=(2, 2)
                ))
            self.ups.append(DoubleConv_decode(feature, Num_of_Desnet_layers))

        # self.pre_final_conv = layers.Conv2D(out_chanals , 1, activation=layers.ReLU())
        self.pre_final_conv = layers.Conv2D(out_chanals, 1)
        # self.final_conv = layers.Conv2DTranspose(
        #         filters = 16, kernel_size = 2, strides = (2, 2)
        # )

    # def call(self, x , training = False):
    def call(self, x, training=True):
        skip_connections = []
        for i in range(len(self.downs)):
            x = self.downs[i].call(x, training=True)
            skip_connections.append(x)
            x = layers.BatchNormalization()(x, training=training)
            x = layers.ReLU()(x)
            x = layers.Conv2D(
                filters=x.shape[3],
                kernel_size=[1, 1],
                strides=[1, 1],
                padding='same', )(x)
            x = layers.Dropout(0.2)(x)
            x = self.pool(x)

        x = dense_block(x, training, self.Num_of_Desnet_layers, self.features[-1] * 2)
        skip_connections = skip_connections[::-1]

        for idx in range(0, len(self.ups), 2):
            x = self.ups[idx](x)

            skip_connection = skip_connections[idx // 2]

            if x.shape[1] != skip_connection.shape[1] or x.shape[2] != skip_connection.shape[2]:
                x = tf.image.resize(x, [skip_connection[0, :, :, i].shape[0], skip_connection[0, :, :, i].shape[1]],
                                    antialias=True)
            concat_skip = layers.concatenate([skip_connection, x], 3)
            x = self.ups[idx + 1].call(concat_skip, )
        x = self.pre_final_conv(x)
        return tf.keras.activations.sigmoid(x)

    def model(self, shape=(512, 512, 1)):
        x = keras.Input(shape=shape)
        return (keras.Model(inputs=[x], outputs=self.call(x)))

model = DesNet(1).model(shape = (512, 512, 1))
model.summary()
keras.utils.plot_model(model, to_file = "FCN_DesNet_ImageSeg.png", show_shapes=True, expand_nested=True,)
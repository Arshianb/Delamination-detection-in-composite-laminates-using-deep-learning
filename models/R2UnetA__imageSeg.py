import os
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# os.environ["CUDA_VISIBLE_DEVICES"] = '0'

# physical_devices = tf.config.list_physical_devices("GPU")
# tf.config.experimental.set_memory_growth(physical_devices[0], True)


class Recurrent_block(layers.Layer):

    def __init__(self, ch_out, t=4):
        super(Recurrent_block, self).__init__()
        self.t = t
        self.ch_out = ch_out
        self.conv = layers.Conv2D(ch_out, (3, 3), padding='same', strides=(1, 1), use_bias=True)
        self.ban = layers.BatchNormalization()
        # self.relu = keras.activations.tanh()
        self.relu = layers.ReLU()

    def call(self, x, training):
        for i in range(self.t):
            if i==0:
                x1 = self.conv(x)
                x1 = self.ban(x1 , training = training)
                x1 = self.relu(x1)
            
            x1 = self.conv(x + x1)
            x1 = self.ban(x1 , training = training)
            x1 = self.relu(x1)
        #     print(x1.shape)
        # print('--- end ---')
        return x1


class RRCNN_block(layers.Layer):
    def __init__(self, ch_out, t=3):
        super(RRCNN_block,self).__init__()
        # self.RCNN = tf.keras.Sequential()
        # self.RCNN.add(Recurrent_block(ch_out,t=t))
        # self.RCNN.add(Recurrent_block(ch_out,t=t))
        self.RCNN1 = Recurrent_block(ch_out, t=t)
        self.RCNN2 = Recurrent_block(ch_out, t=t)
        self.Conv_1x1 = layers.Conv2D(ch_out, (1, 1), padding='valid', strides=(1, 1))
        # self.relu = layers.ReLU()

    def call(self, x, training):
        x = self.Conv_1x1(x)
        x1 = self.RCNN1.call(x, training = training)
        x1 = self.RCNN2.call(x1, training = training)
        # x = self.relu(x+x1)
        return x+x1
        # residual learning


class DoubleConv_encode(layers.Layer):
    def __init__(self, out_channels, t = 3):
        super(DoubleConv_encode, self).__init__()

        self.RRCNN = RRCNN_block(ch_out=out_channels,t=t)

        # # self.conv1 = layers.Conv2D(out_channels, (3, 3),padding = 'same', strides = (1, 1) , use_bias=False, activity_regularizer=keras.regularizers.L2(0.01))
        # self.conv1 = layers.Conv2D(out_channels, (3, 3),padding = 'same', strides = (1, 1) , use_bias=True)
        # self.ban1 = layers.BatchNormalization()
        # # self.rel1 = layers.ReLU()
        # self.rel1 = layers.ReLU()
        # # self.dro1 = layers.Dropout(0.7)
        # self.conv2 = layers.Conv2D(out_channels, (3, 3), strides = (1, 1), padding = 'same', use_bias=True)
        # self.ban2 = layers.BatchNormalization()
        # # self.rel2 = layers.LeakyReLU(alpha=0.1)
        # self.rel2 = layers.ReLU()
        # self.BeforeSum = layers.Conv2D(out_channels, 1, padding="same", strides=1)
        # self.add = layers.Add()
        # # self.dro2 = layers.Dropout(0.5)
        # # self.conv3 = layers.Conv2D(out_channels, (3, 3), strides = (1, 1), padding = 'same', use_bias=True )
        # # self.ban3 = layers.BatchNormalization()
        # # self.rel3 = layers.LeakyReLU()

    def call(self, input_tensor, training = True):
        x = self.RRCNN.call(input_tensor, training = training)


        # if encode_step == 1:
        #     x = self.ban1(input_tensor, training = training)
        #     x = self.rel1(x)
        #     x = self.conv1(x)
        #     # x = self.dro1(x)
        #     x = self.ban2(x, training = training)
        #     x = self.rel2(x)
        #     x = self.conv2(x)
        #     s = self.BeforeSum(input_tensor)
        #     x = self.add([s, x])
        # else:
        # x = self.conv1(input_tensor)
        # x = self.ban1(x, training = training)
        # x = self.rel1(x)
        # x = self.conv2(x)
        # s = self.ban2(x, training = training)
        # x = self.rel2(x)

        # x = self.dro2(x)
        # x = self.conv3(x)
        # x = self.ban3(x, training = training)
        # x = self.rel3(x)
        return x


class DoubleConv_decode(layers.Layer):
    def __init__(self, out_channels, t = 3):
        super(DoubleConv_decode, self).__init__()

        self.Up_RRCNN4 = RRCNN_block(ch_out=out_channels,t=t)

        # self.conv1 = layers.Conv2D(out_channels, (3, 3), strides = (1, 1) , padding="same", use_bias=True)
        # # self.dro1 = layers.Dropout(0.5)
        # self.ban1 = layers.BatchNormalization()
        # self.rel1 = layers.ReLU()
        # self.conv2 = layers.Conv2D(out_channels, (3, 3), strides = (1, 1) , padding="same", use_bias=True)
        # self.ban2 = layers.BatchNormalization()
        # self.rel2 = layers.ReLU()
        # self.rel2 = layers.LeakyReLU()
        # self.BeforeSum = layers.Conv2D(out_channels, 1, padding="same", strides=1)
        
        # self.add = layers.Add()
        # # self.dro2 = layers.Dropout(0.5)
        # # self.conv3 = layers.Conv2D(out_channels, (3, 3), strides = (1, 1) , padding="same", use_bias=True )
        # # self.ban3 = layers.BatchNormalization()
        # # self.rel3 = layers.LeakyReLU()

    def call(self, input_tensor, training = True):
        x = self.Up_RRCNN4.call(input_tensor, training = training)


        # x = self.conv1(input_tensor)
        # x = self.ban1(x, training = training)
        # x = self.rel1(x)
        # x = self.conv2(x)
        # s = self.ban2(x, training = training)
        # x = self.rel2(x)
        # # x = self.dro2(x)
        # # x = self.conv3(x)
        # # # # x = self.dro2(x)
        # # x = self.ban3(x)
        # # x = self.rel3(x)
        return x


def add(tensor_a, tensor_b):
    return layers.Add()([tensor_a, tensor_b])


# def attention(tensor, att_tensor, n_filters=512, kernel_size=(1, 1)):
#     n_filters = int(n_filters)
#     # Stride changed had formula
#     g1 = layers.Conv2D(int(n_filters), strides=(2, 2), kernel_size = (3, 3), use_bias=True, padding="same")(tensor)
#     g1 = layers.BatchNormalization()(g1, training = True)
#     x1 = layers.Conv2D(int(n_filters), strides=(2, 2), kernel_size = (1, 1), use_bias=True, padding="same")(att_tensor)
#     x1 = layers.BatchNormalization()(x1, training = True)
#     net = add(g1, x1)
#     net = layers.ReLU()(net)
#     net = layers.Conv2D(n_filters, strides=(2, 2), kernel_size = kernel_size, use_bias=True, padding="same")(net)
#     net = layers.BatchNormalization()(net, training = True)
#     net = keras.activations.sigmoid(net)
    
#     # net = tf.concat([att_tensor, net], axis=-1)
#     # print('att_tensor=', att_tensor)
#     # print('tensor=', tensor)
#     # Do UpSampling
#     net = net * att_tensor
#     return net

def attention(tensor, att_tensor, n_filters=512, kernel_size=[1, 1]):
    g1 = layers.Conv2D(n_filters, kernel_size=kernel_size)(tensor)
    g1 = layers.BatchNormalization()(g1, training = True)
    x1 = layers.Conv2D(n_filters, kernel_size=kernel_size)(att_tensor)
    x1 = layers.BatchNormalization()(x1, training = True)
    net = add(g1, x1)
    net = layers.ReLU()(net)
    net = layers.BatchNormalization()(net, training = True)
    net = layers.Conv2D(n_filters, kernel_size=kernel_size)(net)
    net = keras.activations.sigmoid(net)
    # net = tf.concat([att_tensor, net], axis=-1)
    net = net * att_tensor
    return net


IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS = 512, 512, 1


class UNET(layers.Layer):
    def __init__(self, out_chanals=1, features=(16, 32, 64, 128, 256)):
        super(UNET , self).__init__()
        self.ups = []
        self.downs = []
        t = 1

        self.pool = layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2))
        for feature in features:
            self.downs.append(DoubleConv_encode(feature, t=t))

        for feature in reversed(features):
            UpSampling = tf.keras.Sequential()
            UpSampling.add(layers.UpSampling2D(size=(2, 2)))
            UpSampling.add(layers.Conv2D(feature, (3, 3),padding = 'same', strides = (1, 1) , use_bias=True))
            UpSampling.add(layers.BatchNormalization())
            UpSampling.add(layers.ReLU())
            self.ups.append(
                UpSampling
                # layers.Conv2DTranspose(
                # filters=feature, kernel_size=2, strides=(2, 2))
            )
            self.ups.append(DoubleConv_decode(feature, t = t))

        self.bottleneck = DoubleConv_encode(features[-1]*2, t=t)
        # self.pre_final_conv = layers.Conv2D(out_channels , 1, activation=layers.LeakyReLU())
        self.final_conv = layers.Conv2D(out_chanals, 1 ,padding = 'same', activation='sigmoid')
        # self.final_conv = layers.Conv2DTranspose(
        # filters = 16, kernel_size = 2, strides = (2, 2))

    # def call(self, x , training = False):

    def call(self, x, training=True):
        skip_connections = []
        for i in range(len(self.downs)):
            x = self.downs[i].call(x, training=training)
            skip_connections.append(x)
            x = self.pool(x)

        x = self.bottleneck.call(x, training=training)
        skip_connections = skip_connections[::-1]

        for idx in range(0, len(self.ups), 2):
            x = self.ups[idx](x, training=training)
            skip_connection = skip_connections[idx//2]
            skip_connection = attention(tensor=skip_connection, att_tensor=x, n_filters=x.shape[3])

            if x.shape[1] != skip_connection.shape[1] or x.shape[2] != skip_connection.shape[2]:
                x = tf.image.resize(x, [skip_connection[0, :, :, i].shape[0], skip_connection[0, :, :, i].shape[1]], antialias=True)
            concat_skip = layers.concatenate([skip_connection, x], 3)
            x = self.ups[idx + 1].call(concat_skip, training=training)
        # x = self.pre_final_conv(x)
        return self.final_conv(x)

    def model(self, shape=(512, 512, 1)):
        x = keras.Input(shape=shape)
        return self.call(x).shape, keras.Model(inputs=[x], outputs=self.call(x))

(OUtoutDim, model) = UNET(out_chanals=1).model(shape = (256, 256, 3))
model.summary()
keras.utils.plot_model(model, to_file = "R2UnetA__imageSeg.png", show_shapes=True, expand_nested=True,)
# import cv2
import numpy as np
import copy

from keras.layers import Dense, MaxPooling2D, AveragePooling2D, ZeroPadding2D, Dropout, Flatten, \
    Reshape, Activation, Lambda, GlobalAveragePooling2D, Layer, InputSpec, Add, Input
from keras.layers import Conv2D
from tensorflow import keras

from keras.optimizers import SGD
from keras.layers import BatchNormalization
from keras.models import Model
from keras import initializers
# from keras.engine import InputSpec
from keras import backend as K
from keras import backend
import sys

# sys.setrecursionlimit(3000)

class Scale(Layer):
    def __init__(self, weights=None, axis=-1, momentum=0.9, beta_init='zero', gamma_init='one', **kwargs):
        self.momentum = momentum
        self.axis = axis
        self.beta_init = initializers.get(beta_init)
        self.gamma_init = initializers.get(gamma_init)
        self.initial_weights = weights
        super(Scale, self).__init__(**kwargs)

    def build(self, input_shape):
        self.input_spec = [InputSpec(shape=input_shape)]
        shape = (int(input_shape[self.axis]),)
        # , name = '{}_gamma'.format(self.name)
        self.gamma = self.gamma_init(shape)
        self.beta = self.beta_init(shape, )
        self._trainable_weights = [self.gamma, self.beta]

        if self.initial_weights is not None:
            self.set_weights(self.initial_weights)
            del self.initial_weights

    def call(self, x, mask=None):
        input_shape = self.input_spec[0].shape
        broadcast_shape = [1] * len(input_shape)
        broadcast_shape[self.axis] = input_shape[self.axis]

        out = K.reshape(self.gamma, broadcast_shape) * x + K.reshape(self.beta, broadcast_shape)
        return out

    def get_config(self):
        config = {"momentum": self.momentum, "axis": self.axis}
        base_config = super(Scale, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))


def identity_block(input_tensor, kernel_size, filters, stage, block):
    '''The identity_block is the block that has no conv layer at shortcut
    # Arguments
        input_tensor: input tensor
        kernel_size: defualt 3, the kernel size of middle conv layer at main path
        filters: list of integers, the nb_filters of 3 conv layer at main path
        stage: integer, current stage label, used for generating layer names
        block: 'a','b'..., current block label, used for generating layer names
    '''
    eps = 1.1e-5
    nb_filter1, nb_filter2, nb_filter3 = filters
    conv_name_base = 'res' + str(stage) + block + '_branch'
    bn_name_base = 'bn' + str(stage) + block + '_branch'
    scale_name_base = 'scale' + str(stage) + block + '_branch'

    x = Conv2D(nb_filter1, (1, 1), name=conv_name_base + '2a', use_bias=True)(input_tensor)
    x = BatchNormalization(name=bn_name_base + '2a')(x, training=True)
    # x = Scale(axis=bn_axis, name=scale_name_base + '2a')(x)
    x = Activation('relu', name=conv_name_base + '2a_relu')(x)

    x = ZeroPadding2D((1, 1), name=conv_name_base + '2b_zeropadding')(x)
    x = Conv2D(nb_filter2, (kernel_size, kernel_size),
                      name=conv_name_base + '2b', use_bias=True)(x)
    x = BatchNormalization(name=bn_name_base + '2b')(x, training=True)
    # x = Scale(axis=bn_axis, name=scale_name_base + '2b')(x)
    x = Activation('relu', name=conv_name_base + '2b_relu')(x)

    x = Conv2D(nb_filter3, (1, 1), name=conv_name_base + '2c', use_bias=True)(x)
    x = BatchNormalization(name=bn_name_base + '2c')(x, training=True)
    # x = Scale(axis=bn_axis, name=scale_name_base + '2c')(x)

    x = Add(name='res' + str(stage) + block)([x, input_tensor])
    x = Activation('relu', name='res' + str(stage) + block + '_relu')(x)
    return x


def conv_block(input_tensor, kernel_size, filters, stage, block, strides=(2, 2)):
    eps = 1.1e-5
    nb_filter1, nb_filter2, nb_filter3 = filters
    conv_name_base = 'res' + str(stage) + block + '_branch'
    bn_name_base = 'bn' + str(stage) + block + '_branch'
    scale_name_base = 'scale' + str(stage) + block + '_branch'

    x = Conv2D(nb_filter1, (1, 1), strides=strides,
                      name=conv_name_base + '2a', use_bias=True)(input_tensor)
    x = BatchNormalization(name=bn_name_base + '2a')(x, training=True)
    # x = Scale(axis=bn_axis, name=scale_name_base + '2a')(x)
    x = Activation('relu', name=conv_name_base + '2a_relu')(x)

    x = ZeroPadding2D((1, 1), name=conv_name_base + '2b_zeropadding')(x)
    x = Conv2D(nb_filter2, (kernel_size, kernel_size),
                      name=conv_name_base + '2b', use_bias=True)(x)
    x = BatchNormalization(name=bn_name_base + '2b')(x, training=True)
    # x = Scale(axis=bn_axis, name=scale_name_base + '2b')(x)
    x = Activation('relu', name=conv_name_base + '2b_relu')(x)

    x = Conv2D(nb_filter3, (1, 1), name=conv_name_base + '2c', use_bias=True)(x)
    x = BatchNormalization(name=bn_name_base + '2c')(x, training=True)
    # x = Scale(axis=bn_axis, name=scale_name_base + '2c')(x)

    shortcut = Conv2D(nb_filter3, (1, 1), strides=strides,
                             name=conv_name_base + '1', use_bias=True)(input_tensor)
    shortcut = BatchNormalization(name=bn_name_base + '1')(shortcut, training=True)
    # shortcut = Scale(axis=bn_axis, name=scale_name_base + '1')(shortcut)

    x = Add(name='res' + str(stage) + block)([x, shortcut])
    x = Activation('relu', name='res' + str(stage) + block + '_relu')(x)
    return x


def resnet152_model(input_tensor = None,
            input_shape=[None, None, 1],
            classes=6,
            **kwargs):
    eps = 1.1e-5
    if input_tensor is None:
        img_input = Input(shape=input_shape)
    else:
        if not backend.is_keras_tensor(input_tensor):
            img_input = Input(tensor=input_tensor, shape=input_shape)
        else:
            img_input = input_tensor
    # if backend.image_data_format() == 'channels_last':
    global bn_axis
    bn_axis = 1
    x = ZeroPadding2D((3, 3),)(img_input)
    x = Conv2D(64, (7, 7), strides=(2, 2), use_bias=True)(x)
    x = BatchNormalization()(x, training=True)
    # x = Scale(axis=bn_axis, name='scale_conv1')(x)
    x = Activation('relu', name='conv1_relu')(x)
    x = MaxPooling2D((3, 3), strides=(2, 2),)(x)

    x = conv_block(x, 3, [64, 64, 256], stage=2, block='a', strides=(1, 1))
    # x = Dropout(0.3)(x)
    x = identity_block(x, 3, [64, 64, 256], stage=2, block='b')
    # x = Dropout(0.3)(x)
    x = identity_block(x, 3, [64, 64, 256], stage=2, block='c')
    # x = Dropout(0.3)(x)

    x = conv_block(x, 3, [128, 128, 512], stage=3, block='a')
    for i in range(1, 8):
        x = identity_block(x, 3, [128, 128, 512], stage=3, block='b' + str(i))
        # x = Dropout(0.3)(x)

    x = conv_block(x, 3, [256, 256, 1024], stage=4, block='a')
    for i in range(1, 36):
        x = identity_block(x, 3, [256, 256, 1024], stage=4, block='b' + str(i))
        # x = Dropout(0.3)(x)

    x = conv_block(x, 3, [512, 512, 2048], stage=5, block='a')
    x = identity_block(x, 3, [512, 512, 2048], stage=5, block='b')
    # x = Dropout(0.3)(x)
    x = identity_block(x, 3, [512, 512, 2048], stage=5, block='c')
    # x = Dropout(0.3)(x)

    x_fc = AveragePooling2D((7, 7))(x)
    x_fc = Flatten()(x_fc)
    x_fc = Dense(1000, activation='relu')(x_fc)
    x_fc = Dense(512, activation='relu')(x_fc)
    # x_fc = Dropout(0.3)(x_fc)
    x_fc = Dense(classes, activation='sigmoid')(x_fc)
    
    
    model = Model(img_input, x_fc, name='resnet152')


    return model

if __name__ == '__main__': 

  # Test pretrained model
  model = resnet152_model(input_shape=[256, 256, 1], classes=100)
  model.summary()
#   keras.utils.plot_model(model, to_file = "ResNet152.png", show_shapes=True, expand_nested=True,)

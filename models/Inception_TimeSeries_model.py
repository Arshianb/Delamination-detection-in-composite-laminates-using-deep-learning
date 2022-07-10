
from keras.layers import *
from tensorflow import keras
import tensorflow_addons as tfa

class InceptionModule(Layer):
    def __init__(self, ni, nf, ks=40, bottleneck=True):
        super(InceptionModule, self).__init__()

        ks = [ks // (2**i) for i in range(3)]
        ks = [k if k % 2 != 0 else k - 1 for k in ks]  # ensure odd ks
        bottleneck = bottleneck if ni > 1 else False
        self.bottleneck = Conv1D(
            nf,
            1,
            strides= 1 ,
            padding='same',
            use_bias=False,
        )
        self.convs = [Conv1D(nf, kernel_size = k, padding = 'same' , use_bias=False) for k in ks]
        self.maxconvpool = keras.Sequential([MaxPool1D(3, strides=1, padding='same'), Conv1D(nf, kernel_size = 1, padding = 'same' , use_bias=False)])
        self.bn = BatchNormalization(axis=-1)
        self.act = ReLU()
        self.concat = Concatenate()
    def call(self, x):
        input_tensor = x
        x = self.bottleneck(input_tensor)
        x = self.concat([l(x) for l in self.convs] + [self.maxconvpool(input_tensor)])
        return self.act(self.bn(x))

class ConvBlock(Layer):
    def __init__(self, ch_out, kernel_size):
        super(ConvBlock, self).__init__()
        self.ch_out = ch_out
        self.conv = Conv1D(ch_out, kernel_size, padding='same', strides=1, use_bias=False)
        self.ban = BatchNormalization()
        # self.relu = keras.activations.tanh()
        self.relu = ReLU()

    def call(self, x, training=True):
        x1 = self.conv(x)
        x1 = self.ban(x1 , training = training)
        x1 = self.relu(x1)
        return x1


class InceptionBlock(Layer):
    def __init__(self, ni, nf=32, residual=True, depth=6, **kwargs):
        super(InceptionBlock, self).__init__()
        self.residual, self.depth = residual, depth
        self.inception, self.shortcut = [], []
        for d in range(depth):
            self.inception.append(InceptionModule(ni = ni if d == 0 else nf * 4, nf = nf))
            if self.residual and d % 3 == 2:
                n_in, n_out = ni if d == 2 else nf * 4, nf * 4
                self.shortcut.append(BatchNormalization() if n_in == n_out else ConvBlock(n_out, 1))
        self.add = Add()
        self.act = ReLU()

    def call(self, x):
        res = x
        for d, l in enumerate(range(self.depth)):
            # print("self.inception[d](x) = ", self.inception[d](x))
            x = self.inception[d].call(x)
            if self.residual and d % 3 == 2: res = x = self.act(self.add([x, self.shortcut[d//3](res)]))
            # print("here1 d = ", d)
        return x

class GAP1d(Layer):
    def __init__(self, output_size=1):
        super(GAP1d, self).__init__()
        self.gap = tfa.layers.AdaptiveAveragePooling1D(1)
        self.flatten = Flatten()
    def call(self, x):
        return self.flatten(self.gap(x))


class InceptionTime(Layer):
    def __init__(self, c_in, c_out, nf=32, **kwargs):
        super(InceptionTime, self).__init__()
        self.inceptionblock = InceptionBlock(c_in, nf)
        self.gap = GAP1d(1)
        self.fc = Dense(c_out)

    def call(self, x):
        x = self.inceptionblock.call(x)
        x = self.gap.call(x)
        x = self.fc(x)
        return x

def model_InceptionTime(c_in, c_out, nf=32,):
    x = keras.Input(shape=[nf, c_in])
    return keras.Model(inputs=[x], outputs=InceptionTime(c_in, c_out, nf)(x))

model = model_InceptionTime(1, 100, nf=1024)
print(model.summary())
keras.utils.plot_model(model, to_file = "Inception_timeSeries_model.png", show_shapes=True, expand_nested=True,)
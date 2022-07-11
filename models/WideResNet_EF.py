from tensorflow.keras import layers
import tensorflow as tf
from tensorflow import keras

class BasicBlock(layers.Layer):
    def __init__(self, in_planes, out_planes, stride, dropout=0.0, activate_before_residual=False):
        super(BasicBlock, self).__init__()
        self.bn1 = layers.BatchNormalization(momentum=0.001)
        self.relu1 = layers.LeakyReLU(alpha=0.1)
        self.conv1 = layers.Conv2D(
                out_planes,
                kernel_size=3,
                strides=stride,
                padding='same', use_bias=False)
        self.bn2 = layers.BatchNormalization(momentum=0.001)
        self.relu2 = layers.LeakyReLU(alpha=0.1)
        self.conv2 = layers.Conv2D(
                out_planes,
                kernel_size=3,
                strides=1,
                padding='same', use_bias=False)
        self.dropout = dropout
        self.equalInOut = (in_planes == out_planes)
        self.convShortcut = (not self.equalInOut) and layers.Conv2D(
        out_planes,
        kernel_size=1,
        strides=stride,
        padding='valid', use_bias=False) or None
        self.activate_before_residual = activate_before_residual

    def call(self, x):
        if not self.equalInOut and self.activate_before_residual is True:
            x = self.relu1(self.bn1(x))
        else:
            out = self.relu1(self.bn1(x))
        out = self.relu2(self.bn2(self.conv1(out if self.equalInOut else x)))
        if self.dropout > 0:
            out = layers.Dropout(self.dropout,)(out, training=False)
            # out = F.dropout(out, p=self.dropout, training=self.training)
        out = self.conv2(out)
        return layers.Add()([x if self.equalInOut else self.convShortcut(x), out])


class NetworkBlock(layers.Layer):
    def __init__(self, nb_layers, in_planes, out_planes, block, stride, dropout=0.0,
                 activate_before_residual=False):
        super(NetworkBlock, self).__init__()
        self.layer = self._make_layer(
            block, in_planes, out_planes, nb_layers, stride, dropout, activate_before_residual)

    def _make_layer(self, block, in_planes, out_planes, nb_layers, stride, dropout,
                    activate_before_residual):
        layers = []
        for i in range(int(nb_layers)):
            layers.append(block(i == 0 and in_planes or out_planes, out_planes,
                                i == 0 and stride or 1, dropout, activate_before_residual))
        return layers

    def call(self, x):
        index = 0
        for layer in self.layer:
            index+=1
            if index == 1:
                out = layer.call(x)
            else:
                out = layer.call(out)
                
        return out


class WideResNet(layers.Layer):
    def __init__(self, num_classes, depth=28, widen_factor=2, dropout=0.0, dense_dropout=0.0):
        super(WideResNet, self).__init__()
        channels = [16, 16 * widen_factor, 32 * widen_factor, 64 * widen_factor]
        assert((depth - 4) % 6 == 0)
        n = (depth - 4) / 6
        block = BasicBlock
        # 1st conv before any network block
        self.conv1 = layers.Conv2D(
                        channels[0],
                        kernel_size=3,
                        strides=1,
                        padding='same', use_bias=False)
        # 1st block
        self.block1 = NetworkBlock(
            n, channels[0], channels[1], block, 1, dropout, activate_before_residual=True)
        # 2nd block
        self.block2 = NetworkBlock(
            n, channels[1], channels[2], block, 2, dropout)
        # 3rd block
        self.block3 = NetworkBlock(
            n, channels[2], channels[3], block, 2, dropout)
        # global average pooling and classifier
        self.bn1 = layers.BatchNormalization(momentum=0.001)
        self.relu = layers.LeakyReLU(alpha=0.1)
        self.drop = layers.Dropout(dense_dropout)
        self.fc = layers.Dense(num_classes)
        self.channels = channels[3]

        # for m in self.modules():
        #     if isinstance(m, nn.Conv2d):
        #         nn.init.kaiming_normal_(m.weight,
        #                                 mode='fan_out',
        #                                 nonlinearity='leaky_relu')
        #     elif isinstance(m, nn.BatchNorm2d):
        #         nn.init.constant_(m.weight, 1.0)
        #         nn.init.constant_(m.bias, 0.0)
        #     elif isinstance(m, nn.Linear):
        #         nn.init.xavier_normal_(m.weight)
        #         nn.init.constant_(m.bias, 0.0)

    def call(self, x):
        out = self.conv1(x)
        out = self.block1.call(out)
        out = self.block2.call(out)
        out = self.block3.call(out)
        out = self.relu.call(self.bn1(out))
        out = layers.GlobalAveragePooling2D()(out)
        # out = out.view(-1, self.channels)
        out = layers.Flatten()(out)
        return self.fc(self.drop(out))


def build_wideresnet(num_classes = 8, input_shape = (256, 256, 1), depth=34, widen_factor=8):
  
    out = WideResNet(num_classes=num_classes,
                       dropout=0,
                       dense_dropout=0, depth=depth, widen_factor=widen_factor)
    x = keras.Input(shape=input_shape)
    return keras.Model(inputs=[x], outputs=out.call(x))
    

if __name__ == '__main__':
    model = build_wideresnet(num_classes = 100, input_shape = (256, 256, 1), depth=16, widen_factor=16)
    model.summary()
    # keras.utils.plot_model(model, to_file = "WideResNet_EF.png", show_shapes=True, expand_nested=True,)
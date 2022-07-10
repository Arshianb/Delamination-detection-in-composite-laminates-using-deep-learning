from keras.layers import *
import tensorflow as tf
import keras
import numpy as np
# UNQ_C1 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# GRADED FUNCTION: djmodel

def Recurrent_model(depth_layer_num, Tx, n_values_output, densor, reshaper, n_values_input):

    n_values_input = n_values_input
    X = Input(shape=(Tx, n_values_input)) 
    a0 = Input(shape=(n_values_output,), name='a0')
    c0 = Input(shape=(n_values_output,), name='c0')
    
    
    # x = X[:, t, :]
    out_put_each_layer = []
    input_each_layer = []
    for l in range(depth_layer_num):
        a = a0
        out_put_each_layer = []
        c = c0
        LSTM_cell = LSTM(n_values_output, return_state = True)
        if l == 0:
            for _input__num in range(Tx):
                input_each_layer.append(reshaper[0](X[:, _input__num, :]))
        for t in range(Tx):
            
            a, _, c = LSTM_cell(inputs=input_each_layer[t], initial_state=[a, c])
            # print(a.shape)
            out_put_each_layer.append(reshaper[1](a))
        input_each_layer = []
        input_each_layer= out_put_each_layer
    out = densor(out_put_each_layer[-1])
    model = keras.Model(inputs=[X, a0, c0], outputs=out)    
    return model
n_values_output = 1024
n_values_input = 64
reshaper_input = Reshape((1, n_values_input))
reshaper_layers = Reshape((1, n_values_output))
densor = Dense(100, activation='softmax')
model = Recurrent_model(depth_layer_num = 5, Tx=50, n_values_output = n_values_output, densor=densor, reshaper=[reshaper_input, reshaper_layers], n_values_input = n_values_input)

model.summary()
keras.utils.plot_model(model, to_file = "Recurrent_nerual_network.png", show_shapes=True, expand_nested=True,)
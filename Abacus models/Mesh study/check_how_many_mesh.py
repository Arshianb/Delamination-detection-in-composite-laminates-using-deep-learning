import numpy as np
last_mesh = 0
index = 1
for i in np.linspace(0.04, 0.005, 10000):
    current_mesh = round(0.0512/i)
    if current_mesh!=last_mesh:
        print("i = ", i)
        index = index + 1
        last_mesh = round(0.0512/i)
        print("index = ", index)
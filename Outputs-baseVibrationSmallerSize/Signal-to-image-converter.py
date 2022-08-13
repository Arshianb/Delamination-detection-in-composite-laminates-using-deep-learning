import glob
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
for i in glob.glob("C:\\Users\\arshi\\OneDrive\\Desktop\\Delamination-detection-in-composite-laminates-using-deep-learning\\Outputs-baseVibrationSmallerSize/*.csv"):
    if "A3" in i:
        print(i)
        with open(i, 'r', newline='') as file:
            chanel1 = []
            for row in file:
                row = row.split(",")
                if len(row) > 1:
                    col1 = float(row[1])
                    chanel1.append(col1)
            f, t, Zxx = signal.stft(chanel1, 10e3, nperseg=1000)
            print(t)
            print(f)
            print(Zxx)
            plt.pcolormesh(t, f, np.abs(Zxx), vmin=0, vmax = 0.01)
            plt.title('STFT Magnitude')
            plt.ylabel('Frequency [Hz]')
            plt.xlabel('Time [sec]')
            plt.show()
            # print(chanel1)
            # exit()
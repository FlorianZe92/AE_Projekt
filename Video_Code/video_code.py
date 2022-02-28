import matplotlib.pyplot as plt
import pandas as pd
import sys
import cv2
import numpy as np
import glob
# Übergabe von selben Werten für it_range und it_step_number, wie bei main_graph.cpp Ausführung

list = sys.argv
it_range = int(list[1])
it_step_number = int(list[2])

# Bilder werden erstellt in Ordner Output
for i in range(1,it_step_number):
    iter = i*it_range
    filename_x = "Output/" + "x_"+str(iter)+".csv"
    filename_y = "Output/" + "y_"+str(iter)+".csv"
    data_x =  pd.read_csv(filename_x, header = None, sep = '\t')
    data_y = pd.read_csv(filename_y, header = None, sep = '\t' )
    plt.plot(data_x,data_y,'bs')
    plt.xlim((-5, 105))
    plt.ylim((-5, 105))
    plt.tight_layout()
    plt.savefig("Output/" + str(iter))
    plt.clf()

# Video wird im Folgenden erstellt.

filenames = []
for i in range(1,it_step_number):
    iter = i*it_range
    filename = str(iter)+".png"
    filenames.append(filename)

img_array = []
for filename in filenames:
    img = cv2.imread("Output/" + filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

out = cv2.VideoWriter('Video.avi', cv2.VideoWriter_fourcc(*'DIVX'), 10, size)
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
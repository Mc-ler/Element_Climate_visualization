# import needy models
import csv
import datetime
from matplotlib import pyplot as plt

#read data from file and explore data frame
filename = "./源代码文件/chapter_16/Temp_Pri/data_ori.csv"
with open(filename) as f:
    read_data = csv.reader(f)
    header = next(read_data)        # get the header row
    t = 0
    for line in read_data:
        print("station:{},date:{},H:{},L:{}".format(line[0],line[1],line[2],line[3]))
        t += 1
        if t == 5:
            break
        
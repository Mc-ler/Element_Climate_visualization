# import needy models
import csv
from datetime import datetime 
from matplotlib import pyplot as plt

#read data from file and explore data frame
filename = "./源代码文件/chapter_16/Temp_Pri/data_ori.csv"
with open(filename) as f:
    read_data = csv.reader(f)
    header = next(read_data)        # get the header row
    
    # clear and prepare for data
    s1_date = []; s1_emnt = []; s1_emxt = []
    s2_date = []; s2_emnt = []; s2_emxt = []
    for row in read_data:
        if row[0] == "CHM00057127":
            data = datetime.strptime(row[1],'%Y-%m')
            try:
                H = int(row[2])
                L = int(row[3])
            except ValueError:
                print(f'Missing month {data}')
            else:
                s1_date.append(data)
                s1_emnt.append(H)
                s1_emxt.append(L)
        elif row[0] == 'CHM00057131':
            data = datetime.strptime(row[1], '%Y-%m')
            try:
                H = int(row[2])
                L = int(row[3])
            except ValueError:
                print(f'Missing month {data}')
            else:
                s2_date.append(data)
                s2_emnt.append(H)
                s2_emxt.append(L)

    
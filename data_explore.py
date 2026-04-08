# import needy models
import csv
from datetime import datetime 
from matplotlib import pyplot as plt

#read data from file and explore data frame (This func can explore to any station_ID search)
def data_read(row,station_ID):
    s_date = []; s_emnt = []; s_emxt = []
    if row[0] == station_ID:
        data = datetime.strptime(row[1],'%Y-%m')
        data = data.strftime('%Y-%m')
        try:
            H = int(row[2])
            L = int(row[3])
        except ValueError:
            print(f'Missing month {data}')
        else:
            s_date.append(data)
            s_emnt.append(H)
            s_emxt.append(L)
    print(s_date)
    return s_date, s_emnt, s_emxt

filename = "./源代码文件/chapter_16/Temp_Pri/data_ori.csv"
with open(filename) as f:
    read_data = csv.reader(f)
    header = next(read_data)        # get the header row
    
    # clear and prepare for data
    s1_date = []; s1_emnt = []; s1_emxt = []
    
    for row in read_data:
        if row[0] == "CHM00057127":
            data = datetime.strptime(row[1],'%Y-%m')
            data = data.strftime('%y-%m')
            try:
                H = int(row[2])
                L = int(row[3])
            except ValueError:
                print(f'Missing month {data}')
            else:
                s1_date.append(data)
                s1_emnt.append(H)
                s1_emxt.append(L)
        s2_date, s2_emnt, s2_emxt = data_read(row, "CHM00057131")
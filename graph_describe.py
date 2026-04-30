# import needy models
import csv
from datetime import datetime 
from matplotlib import pyplot as plt
import seaborn as sns
from PIL import Image



#read data from file and explore data frame (This func can explore to any station_ID search)
def data_read(data:list,station_ID):
    s_date = []; s_emnt = []; s_emxt = []
    for row in data:
        if row[0] == station_ID:
            data = datetime.strptime(row[1],'%Y-%m')
            data = data.strftime('%Y-%m')
            try:
                H = int(row[2])
                L = int(row[3])
            except ValueError:
                print(f'Station {station_ID} Missing month {data}')
            else:
                s_date.append(data)
                s_emnt.append(H)
                s_emxt.append(L)
    return s_date, s_emnt, s_emxt

filename = "./源代码文件/chapter_16/Temp_Pri/data_ori.csv"
with open(filename) as f:
    read_data = list(csv.reader(f))
    # header = next(read_data)        # get the header row
    
    # clear and prepare for data
    s1_date, s1_emnt, s1_emxt = data_read(read_data,"CHM00057127")
    s2_date, s2_emnt, s2_emxt = data_read(read_data,"CHM00057131")

img_1 = Image.open("./源代码文件/chapter_16/Temp_Pri/image/figure_1_1.jpg")
img_2 = Image.open("./源代码文件/chapter_16/Temp_Pri/image/figure_1_2.jpg")
def get_extent(dt_list, y_low, y_high):
    left = dt_list[0]
    right = dt_list[-1]
    pad = (y_high - y_low) * 0.1   
    return [left, right, y_low - pad, y_high + pad]

# Settings of fonts
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'SimSun']




# plot figures (combination of two station with H/L data)
plt.style.use("ggplot")
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].plot(s1_date, s1_emnt, c='#bcab90', alpha=0.8)
ax[0].plot(s1_date, s1_emxt, c='#594d45', alpha=0.8)
ax[0].fill_between(s1_date, s1_emnt, s1_emxt, facecolor='#ac7e54',alpha=0.5)
ax[0].set_xticks(s1_date[::5])
ax[0].set_xticklabels(s1_date[::5], rotation=60, ha='right')
ax[0].set_xlabel("Date(Year)", fontsize=14, labelpad=10)
ax[0].set_ylabel("Temperature($^\circ$C)",fontsize=14, labelpad=10)
ax[0].imshow(img_2, extent=get_extent(s1_date, min(s1_emnt), max(s1_emxt)), aspect='auto', zorder=0)

ax[1].plot(s2_date, s2_emnt, c='#0073ad', alpha=0.8)
ax[1].plot(s2_date, s2_emxt, c='#123057', alpha=0.8)
ax[1].fill_between(s2_date, s2_emnt, s2_emxt, facecolor='#0067a7', alpha=0.5)
ax[1].set_xticks(s1_date[::5])
ax[1].set_xticklabels(s1_date[::5], rotation=60, ha='right')
ax[1].set_xlabel("Date(Year)", fontsize=14, labelpad=10)
ax[1].set_ylabel("Temperature($^\circ$C)",fontsize=14, labelpad=10)
ax[1].imshow(img_1, extent=get_extent(s2_date, min(s2_emnt), max(s2_emxt)), aspect='auto', zorder=0)



title = f"Monthly High Tempeture VS. Low Temp Of Two Stations".title()
fig.text(0.5, 0.9, title, fontsize=18, ha='center', transform=fig.transFigure)
fig.autofmt_xdate()
plt.show()

 
import matplotlib.pyplot as plt
import csv
from datetime import datetime

filename='data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader=csv.reader(f)
    head_row=next(reader)

    for index,column_header in enumerate(head_row):
        print(index,column_header)
    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            low = int(row[6])
            high = int(row[5])
        except ValueError:
            print(f'Miss data for {date}')
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

    fig, ax = plt.subplots(figsize=(10, 6))
    # alpha 透明度 0-1
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolors='yellow', alpha=0.1)

    # 设置图形格式
    ax.set_title('2018年死亡谷每日最高最低温度', fontsize=24)
    ax.set_xlabel('日期', fontsize=16)
    # 绘制倾斜的标签
    fig.autofmt_xdate()
    ax.set_ylabel('温度（F）', fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)

    # Get dates and high temperatures from this file:
    # dates, highs, lows = [], [], []
    dates, prcp = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        prcps = float(row[3])
        # high = int(row[5])
        # low = int(row[6])
        dates.append(current_date)
        prcp.append(prcps)
        # highs.append(high)
        # lows.append(low)

    #print(highs)

    # Plot the high and low temperatures.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, prcp, c='red', alpha=0.5)
    #ax.plot(dates, lows, c='blue', alpha=0.5)
    ax.fill_between(dates, prcp, facecolor='blue', alpha=0.1)

    # Format Plot.
    ax.set_title("Daily Rainfall - 2018", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Rainfall", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

    # Get the index of the header row
    for index, column_header in enumerate(header_row):
        print(index, column_header)
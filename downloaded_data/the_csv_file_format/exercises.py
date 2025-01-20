from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

''' 
    Exercise 16-1: Sitka Rainfall
        Plots histogram of daily precipitation levels in Sitka in 2021.
        Final image found: sitkarainfall.png        
'''
def sitka_rain_levels():
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.bar(s_dates, lvls, color='blue')
    
    ax.set_title(f"Daily Precipitation in Sitka 2021 \n {s_name}", fontsize=16)
    ax.set_xlabel("", fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Precipitation Levels (in)", fontsize=16)
    
    plt.savefig('sitkarainfall.png', bbox_inches='tight')
    plt.show()

'''
    Exercise 16-2: Sitka vs Death Valley Comparison
        Plots both high and low temperatures of Sitka and Death Valley.
        Shown in same plot for comparison.
        Final image found: citycomparison.png
'''
def city_comparison():
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    
    ax.plot(s_dates, s_highs, color='red', alpha=0.3)
    ax.plot(s_dates, s_lows, color='blue', alpha=0.3)
    ax.fill_between(s_dates, s_highs, s_lows, facecolor='blue', alpha=0.1)
    
    ax.plot(s_dates, dv_highs, color='red', alpha=0.6)
    ax.plot(s_dates, dv_lows, color='blue', alpha=0.6)
    ax.fill_between(s_dates, dv_highs, dv_lows, facecolor='blue', alpha=0.1)
    
    ax.set_title(f"Sitka and Death Valley Temperatures, 2021\n {s_name} & {dv_name}"
                 , fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(labelsize=16)
    
    plt.savefig('citycomparison.png', bbox_inches='tight')
    plt.show()

'''
    Exercise 16-4: Automated Indexes
        Dynamically save temperatures, station name, precipitation levels
        as appropriate for two cities.
'''
path = Path('weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

sitka_reader = csv.reader(lines)
sitka_header_row = next(sitka_reader)

s_high_index = sitka_header_row.index("TMAX")
s_low_index = sitka_header_row.index("TMIN")
s_rain_index = sitka_header_row.index("PRCP")
s_name_index = sitka_header_row.index("NAME")

# Extract station name, dates, precipitation levels, and temperatures.
s_dates, s_highs, s_lows, lvls = [], [], [], []
s_name = ""
for row in sitka_reader:
    if not s_name:
        s_name = row[s_name_index]        
        
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[s_high_index])
        low = int(row[s_low_index])
        rain = float(row[s_rain_index])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:      
        s_dates.append(current_date)
        s_highs.append(high)
        s_lows.append(low)
        lvls.append(rain)
        
path = Path('weather_data/death_valley_2021_full.csv')
lines = path.read_text().splitlines()

dv_reader = csv.reader(lines)
dv_header_row = next(dv_reader)

dv_high_index = dv_header_row.index("TMAX")
dv_low_index = dv_header_row.index("TMIN")
dv_name_index = dv_header_row.index("NAME")

# Extract station name, dates, and  temperatures.
dv_dates, dv_highs, dv_lows = [], [], []
dv_name = ""
for row in dv_reader:
    if not dv_name:
        dv_name = row[dv_name_index]
    
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[dv_high_index])
        low = int(row[dv_low_index])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:      
        dv_dates.append(current_date)
        dv_highs.append(high)
        dv_lows.append(low)
        
sitka_rain_levels()
   
city_comparison()
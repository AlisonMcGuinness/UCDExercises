# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt
import pandas as pd

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

# Call the show function to show the result
# plt.show()  = this is a blank chart no data.

'''
Adding data to a figure is done by calling methods of the Axes object. 
In this exercise, we will use the plot method to add data about rainfall in two American cities: 
Seattle, WA and Austin, TX.

The data are stored in two Pandas DataFrame objects that are already loaded into memory: 
seattle_weather stores information about the weather in Seattle, 
and austin_weather stores information about the weather in Austin. 
Each of the data frames has a MONTHS column that stores the three-letter name of the months. 
Each also has a column named "MLY-PRCP-NORMAL" that stores the average 
rainfall in each month during a ten-year period.

'''
seattle_weather = pd.read_csv('Data7\\seattle_weather.csv', sep=',')
austin_weather = pd.read_csv('Data7\\austin_weather.csv', sep=',')
# Plot MLY-PRCP-NORMAL from seattle_weather against the MONTH
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"],color="b", marker="o", linestyle="--")

# Plot Austin data, setting data appearance
# note plot(x axis data, y axis data, other key words)
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color="r", marker="v", linestyle="--")

# Customize the x-axis label
ax.set_xlabel("Time (months)")

# Customize the y-axis label
ax.set_ylabel("Precipitation (inches)")

# Add the title
ax.set_title("Weather patterns in Austin and Seattle")
# Call the show function
plt.show()

print('')
print('subplots!')
'''
You can have multiple graphs all in one with subplots
'''
# Create a Figure and an array of subplots with 2 rows and 2 columns
fig, ax = plt.subplots(2, 2)

# Addressing the top left Axes as index 0, 0, plot month and Seattle precipitation
ax[0, 0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])

# In the top right (index 0,1), plot month and Seattle temperatures
ax[0, 1].plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])

# In the bottom left (1, 0) plot month and Austin precipitations
ax[1,0].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# In the bottom right (1, 1) plot month and Austin temperatures
ax[1,1].plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()

'''
another example
if all the data is the same type then use sharey so the y axis have the same scale
'''
# Create a figure and an array of axes: 2 rows, 1 column with shared y axis
fig, ax = plt.subplots(2, 1, sharey=True)

# Plot Seattle precipitation data in the top axes
ax[0].plot(seattle_weather["MONTH"], seattle_weather['MLY-PRCP-NORMAL'], color = "b")
ax[0].plot(seattle_weather["MONTH"], seattle_weather['MLY-PRCP-25PCTL'], color = "b", linestyle = "--")
ax[0].plot(seattle_weather["MONTH"], seattle_weather['MLY-PRCP-75PCTL'], color = "b", linestyle = "--")

# Plot Austin precipitation data in the bottom axes
ax[1].plot(austin_weather["MONTH"], austin_weather['MLY-PRCP-NORMAL'], color = "r")
ax[1].plot(austin_weather["MONTH"], austin_weather['MLY-PRCP-25PCTL'], color = "r", linestyle = "--")
ax[1].plot(austin_weather["MONTH"], austin_weather['MLY-PRCP-75PCTL'], color = "r", linestyle = "--")

#plt.show()

print('')
print('Time series data')
print('make sure the time data is stored as a date and is in the index')

# Read the data from file using read_csv
climate_change = pd.read_csv('Data7\\climate_change.csv', parse_dates=True, index_col="date")

fig, ax = plt.subplots()
# Add the time-series for "relative_temp" to the plot
# Note using the index here!
ax.plot(climate_change.index, climate_change['relative_temp'])
# Set the x-axis label
ax.set_xlabel('Time')
# Set the y-axis label
ax.set_ylabel('Relative temperature (Celsius)')
# Show the figure
#plt.show()

'''
drill down to just data for certain years
'''
# Use plt.subplots to create fig and ax
fig, ax = plt.subplots()
# Create variable seventies with data from "1970-01-01" to "1979-12-31"
seventies = climate_change["1970-01-01":"1979-12-31"]
# Add the time-series for "co2" data from seventies to the plot
ax.plot(seventies.index, seventies["co2"])
# Show the figure
#plt.show()

print('')
print('plotting 2 sets of data for the same time series on the same graph')
'''
if you plot 2 set of data it can be not useful if the scales are different
so you can have 2 separate y sclaes one on each side of the graph
need to use colors on the plot AND on the y axix ticks ad label so it
is clear which data belongs to which y scale. 
'''

# Define a function called plot_timeseries
def plot_timeseries(axes, x, y, color, xlabel, ylabel):

  # Plot the inputs x,y in the provided color
  axes.plot(x, y, color=color)

  # Set the x-axis label
  axes.set_xlabel(xlabel)

  # Set the y-axis label
  axes.set_ylabel(ylabel, color=color)

  # Set the colors tick params for y-axis
  axes.tick_params('y', colors=color)

ig, ax = plt.subplots()

# Plot the CO2 levels time-series in blue
plot_timeseries(ax, climate_change.index, climate_change['co2'], "blue", 'Time (years)', 'CO2 levels')

# Create a twin Axes object that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature data in red
plot_timeseries(ax2, climate_change.index, climate_change['relative_temp'], "red", 'Time (years)', 'Relative temperature (Celsius)')

# Annotate point with relative temperature >1 degree
'''
annotate good for pointing key data
xy is the coords of the focal data
xytext is where the text appears
arrowprops will show an arrow from the text tothe focal point
the coords are based on the scales on the axes. 
'''
ax2.annotate(">1 degree", xy=[pd.Timestamp('2015-10-06'), 1], xytext=[pd.Timestamp('2008-10-06'), -0.2], arrowprops={'arrowstyle':'->', 'color':'gray'})
#plt.show()

print('')
print('BAR CHARTS')
'''
use bar() method instead of plot()
similar enough first 2 params are x axis data nd y axis data
can also use label param to label each bar, then call ax.legend() before plt.show to show a legend 
from the labels.

for a stacked bar chart, keep calling .bar but set the bottom parameter to the previous data
so it knows that the bottom of the data should be shown at that position. 
'''
medals = pd.read_csv('Data7\\medals_by_country_2016.csv', index_col=0)
fig, ax = plt.subplots()

# Add bars for "Gold" with the label "Gold"
ax.bar(medals.index, medals['Gold'], label='Gold')

# Stack bars for "Silver" on top with label "Silver"
ax.bar(medals.index, medals['Silver'], bottom=medals['Gold'], label='Silver')

# Stack bars for "Bronze" on top of that with label "Bronze"
ax.bar(medals.index, medals['Bronze'], bottom = medals['Gold'] + medals['Silver'], label='Bronze')
# Set the x-axis tick labels to the country names
ax.set_xticklabels(medals.index, rotation=90)

# Set the y-axis label
ax.set_ylabel('Number of medals')

# Display the legend
ax.legend()
plt.show()

print('')
print('Histograms')
print('histogram shows distribution of values of a variable')
'''
use .hist(column of data, label='blah', bins=x, or bins= [x, y ,z], histtype='step')
the x axis will have the values in the variable (in bins) default 10 bins
the y axis has the number of times each value appears in the column
'''
fig, ax = plt.subplots()

# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing['Weight'], label="Rowing", histtype='step', bins=5)
# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics['Weight'], label="Gymnastics", histtype="step", bins=5)

ax.set_xlabel("Weight (kg)")
ax.set_ylabel("# of observations")

# Add the legend and show the Figure
ax.legend()
plt.show()



print('Statistical plotting')
'''
do no tunderstand any of this but here is the exmaples
'''

print('errorbars on a PLOT')
fig, ax = plt.subplots()

# Add Seattle temperature data in each month with error bars
ax.errorbar(seattle_weather['MONTH'], seattle_weather['MLY-TAVG-NORMAL'], yerr=seattle_weather['MLY-TAVG-STDDEV'])

# Add Austin temperature data in each month with error bars
ax.errorbar(austin_weather['MONTH'], austin_weather['MLY-TAVG-NORMAL'], yerr=austin_weather['MLY-TAVG-STDDEV'])

print('box plots')
'''
for example can see how many individuals are outliers in their group.
or something - this is quite sophisticated stats and I don't get it
can readon you tube/wikipedia if need to understand it.
'''
fig, ax = plt.subplots()

# Add a boxplot for the "Height" column in the DataFrames
ax.boxplot([mens_rowing['Height'], mens_gymnastics['Height']])

# Add x-axis tick labels:
ax.set_xticklabels(['Rowing', 'Gymnastics'])

# Add a y-axis label
ax.set_ylabel('Height (cm)')

plt.show()
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

plt.show()
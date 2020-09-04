#!/usr/bin/env python
# coding: utf-8

# This is a data visualization project. With Yahoo Finance's finanacial database, Netflix's 2017 stock data will be analyzed. The visualizations are the following:
# 
#  - The distribution of the stock prices for the past year
#  - Netflix's earnings and revenue in the last four quarters
#  - The actual vs. estimated earnings per share for the four quarters in 2017
#  - A comparison of the Netflix Stock price vs the Dow Jones Industrial Average price in 2017 
# 
# Financial Data Source: [Yahoo Finance](https://finance.yahoo.com/quote/DATA/)
# 

# In[5]:


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


# In[7]:


# Loading NFLX.csv

netflix_stocks = pd.read_csv('NFLX.csv')
print(netflix_stocks)


# In[9]:


# Loading DJI.csv

dowjones_stocks = pd.read_csv('DJI.csv')
print(dowjones_stocks)


# In[10]:


# Loading NFLX_daily_by_quarter.csv

netflix_stocks_quarterly = pd.read_csv('NFLX_daily_by_quarter.csv')
print(netflix_stocks_quarterly)


# In[18]:


print(netflix_stocks.head())


# In[24]:


# Modifying column 'Adj Close' to 'Price' for the three dataframes

netflix_stocks.rename(columns = {'Adj Close': 'Price'}, inplace = True)
dowjones_stocks.rename(columns = {'Adj Close': 'Price'}, inplace = True)
netflix_stocks_quarterly.rename(columns = {'Adj Close': 'Price'}, inplace = True)


# In[25]:


print(netflix_stocks.head())
print(dowjones_stocks.head())
print(netflix_stocks_quarterly.head())


# In[81]:


# Plotting the distribution of Netflix stock prices using sns.violinplot

ax = sns.violinplot(
    data = netflix_stocks_quarterly,
    x = "Quarter",
    y = "Price"
)

ax.set_title(
    label = "Distribution of 2017 Netflix Stock Prices by Quarter"
)

ax.set(
    xlabel = "Business Quarters in 2017",
    ylabel = "Closing Stock Price",
)

plt.savefig("Visualization1.png")
plt.show()


#  

#  

# In[80]:


# Plotting the actual and estimate EPS using plt.scatter

x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017","2Q2017","3Q2017","4Q2017"]
earnings_actual =[.4, .15,.29,.41]
earnings_estimate = [.37,.15,.32,.41 ]

plt.scatter(x_positions, earnings_actual, color = 'red', alpha = 0.5)
plt.scatter(x_positions, earnings_estimate, color = 'blue', alpha = 0.5)
plt.legend(["Actual", "Estimate"])
plt.xticks(x_positions, chart_labels)
plt.title("Earnings Per Share in Cents")

plt.savefig("Visualization2.png")
plt.show()


#  

#  

# In[79]:


# Plotting the earnings and revenue for Netflix side-by-side

# The metrics below are in billions of dollars
revenue_by_quarter = [2.79, 2.98,3.29,3.7]
earnings_by_quarter = [.0656,.12959,.18552,.29012]
quarter_labels = ["2Q2017","3Q2017","4Q2017", "1Q2018"]

# Revenue
n = 1  # This is our first dataset
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.8 # Width of each bar
bars1_x = [t*element + w*n for element in range(d)]
# Here bars1_x is the list [0.8, 2.8, 4.8, 6.8], which are the middle points of the blue bars on the x-axis

plt.bar(bars1_x, revenue_by_quarter)

# Earnings
n = 2  # This is our second dataset
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.8 # Width of each bar
bars2_x = [t*element + w*n for element in range(d)]
# Here bars2_x is the list [1.6, 3.6, 5.6, 7.6], which are the middle points of the orange bars on the x-axis

middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
# Here middle_x is the list [1.2, 3.2, 5.2, 7.2], which are the lines on the x-axis separating the blue and orange bars

labels = ["Revenue", "Earnings"]

plt.bar(bars2_x, earnings_by_quarter)
plt.title("Earnings and Revenue Reported by Netflix per Quarter")
plt.legend(labels)
plt.xticks(middle_x, quarter_labels)
plt.savefig("Visualization3.png")
plt.show()



# In[86]:


# Subplotting the stock prices for Netflix and Dow using plt.subplot

# Left plot Netflix
# Here the first subplot has been assigned to ax1 at row 1, col 1
ax1 = plt.subplot(1, 2, 1)
plt.plot(netflix_stocks['Date'], netflix_stocks['Price'])
ax1.set_title('Netflix')
ax1.set_xlabel('Date')
ax1.set_ylabel('Stock Price')

# Right plot Dow Jones
# Here the first subplot has been assigned to ax1 at row 1, col 2
ax2 = plt.subplot(1, 2, 2)
plt.plot(dowjones_stocks['Date'], dowjones_stocks['Price'])
ax2.set_title('Dowjones')
ax2.set_xlabel('Date')
ax2.set_ylabel('Stock Price')

# Here the graph sizes is adjusted to ensure they are readable
plt.subplots_adjust(wspace = 0.5)
plt.savefig("Visualization4.png")
plt.show()






#  

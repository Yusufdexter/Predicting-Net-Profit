# -*- coding: utf-8 -*-
"""
Created on Sat May 23 12:21:52 2020

@author: Yusufdexter
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl



''' REVENUE '''

# Assumptions
average_revenue = 10000000    # 10 million
revenue_std = 1000000         # 1 million
iterations = 2000

np.random.seed(101)
revenue = np.random.normal(average_revenue, revenue_std, iterations)

# Running a check
print(f'Average Revenue: {revenue.mean()}')
print(f'Revenue Deviation: {revenue.std()}')
print(f'Min Revenue: {revenue.min()}')
print(f'Max Revenue: {revenue.max()}')


# VISUALIZATION
fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (10, 6))
axes[0].plot(revenue)
axes[0].set_ylabel('Revenue')
axes[0].set_title('Expected Revenue Line Plot')
axes[0].yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}')) # Format axis

axes[1].hist(revenue, bins = 100)
axes[1].set_xlabel('Revenue')
axes[1].set_title('Expected Revenue Normal Distribution')
axes[1].xaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}')) # Format axis
plt.annotate('The Average Revenue the Company would be making is between 9,000,000 to 11,000,000', 
             (0, 0), (-20, -60), fontsize = 10, xycoords = 'axes fraction', textcoords = 'offset points', va = 'top')
plt.tight_layout()



''' COST OF GOODS SOLD '''

# Assumption
# it is assumed that AVERAGE_COGS = 50% of Revenue & COGS_STD 3%
np.random.seed(101)
cost_of_goods_sold = -(revenue * np.random.normal(0.5, 0.03))

# Running a check
print(f'Average COGS: {cost_of_goods_sold.mean()}')
print(f'COGS Deviation: {cost_of_goods_sold.std()}')
print(f'Min COGS: {cost_of_goods_sold.min()}')
print(f'Max COGS: {cost_of_goods_sold.max()}')


# VISUALIZATION
fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (10, 6))
axes[0].plot(cost_of_goods_sold)
axes[0].set_ylabel('Cost of Goods Sold')
axes[0].set_title('Expected Cost of Goods Sold Line Plot')
axes[0].yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}')) # Format axis

axes[1].hist(cost_of_goods_sold, bins = 100)
axes[1].set_xlabel('Cost of Goods Sold')
axes[1].set_title('Expected Cost of Goods Sold Normal Distribution')
axes[1].xaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}')) # Format axis
plt.annotate('The Average COGS the Company would be making is between 5,200,000 to 6,300,000', 
             (0, 0), (-20, -60), fontsize = 10, xycoords = 'axes fraction', textcoords = 'offset points', va = 'top')
plt.tight_layout()



''' GROSS PROFIT '''

# Assumption
gross_profit = revenue + cost_of_goods_sold

# Running a check
print(f'Average Gross Profit: {gross_profit.mean()}')
print(f'Gross Profit Deviation: {gross_profit.std()}')
print(f'Min Gross Profit: {gross_profit.min()}')
print(f'Max Gross Profit: {gross_profit.max()}')


# VISUALIZATION
fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (10, 6))
axes[0].plot(gross_profit)
axes[0].set_ylabel('Gross Profit')
axes[0].set_title('Expected Gross Profit Line Plot')
axes[0].yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}')) # Format axis

axes[1].hist(gross_profit, bins = 100)
axes[1].set_xlabel('Gross Profit')
axes[1].set_title('Expected Gross Profit Normal Distribution')
axes[1].xaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}')) # Format axis
plt.annotate('The Average Gross Profit the Company would be making is between 3,800,000 to 4,600,000', 
             (0, 0), (-20, -60), fontsize = 10, xycoords = 'axes fraction', textcoords = 'offset points', va = 'top')
plt.tight_layout()



''' OPERATING EXPENSES '''

# Assumption
# it is assumed that OPERATING EXPENSES = 25% of GROSS PROFIT & STD = 3%
np.random.seed(101)
operating_expenses = -(revenue * np.random.normal(0.25, 0.03))

# Running a check
print(f'Average OPERATING EXPENSES: {operating_expenses.mean()}')
print(f'OPERATING EXPENSES Deviation: {operating_expenses.std()}')
print(f'Min OPERATING EXPENSES: {operating_expenses.min()}')
print(f'Max OPERATING EXPENSES: {operating_expenses.max()}')


# VISUALIZATION
fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (10, 6))
axes[0].plot(operating_expenses)
axes[0].set_ylabel('Operating Expenses')
axes[0].set_title('Expected Operating Expenses Line Plot')
axes[0].yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}')) # Format axis

axes[1].hist(operating_expenses, bins = 100)
axes[1].set_xlabel('Operating Expenses')
axes[1].set_title('Expected Operating Expenses Normal Distribution')
axes[1].xaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}')) # Format axis
plt.annotate('The Average Operating Expenses the Company would be making is between 3,000,000 to 3,500,000', 
             (0, 0), (-20, -60), fontsize = 10, xycoords = 'axes fraction', textcoords = 'offset points', va = 'top')
plt.tight_layout()



''' NET PROFIT '''

net_profit = gross_profit + operating_expenses

# Running a check
print(f'Average NET PROFIT: {net_profit.mean()}')
print(f'NET PROFIT Deviation: {net_profit.std()}')
print(f'Min NET PROFIT: {net_profit.min()}')
print(f'Max NET PROFIT: {net_profit.max()}')


# VISUALIZATION
fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (10, 6))
axes[0].plot(net_profit)
axes[0].set_ylabel('Net Profit')
axes[0].set_title('Expected Net Profit Line Plot')
axes[0].yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}')) # Format axis

axes[1].hist(net_profit, bins = 100)
axes[1].set_xlabel('Net Profit')
axes[1].set_title('Expected Net Profit Normal Distribution')
axes[1].xaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}')) # Format axis
plt.annotate('The Average Net Profit the Company would be making is overly between 800,000 to 1,000,000', 
             (0, 0), (-20, -60), fontsize = 10, xycoords = 'axes fraction', textcoords = 'offset points', va = 'top')
plt.tight_layout()


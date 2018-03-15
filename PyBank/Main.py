
# coding: utf-8

# In[1]:


# Import modules
import os
import pandas as pd
# This is for creating and printing to the text file
import sys


# In[2]:


# Open budget file - change folder and file name as needed
budget = os.path.join('raw_data', 'budget_data_2.csv')
budget_df = pd.read_csv(budget)
budget_df.head()


# In[3]:


# Calculate the number of data rows
month_count = budget_df["Date"].count() # len(budget_df["Date"])
month_count


# In[4]:


# Sum of monthly revenue
total_revenue = budget_df["Revenue"].sum()
total_revenue


# In[5]:


# Change in monthly revenue
budget_df["Change"] = budget_df["Revenue"].diff()
budget_df.head()


# In[6]:


# Average, minimum, and maximum revenue change
avgChange = budget_df["Change"].mean()
minChange = budget_df["Change"].min()
maxChange = budget_df["Change"].max()
avgChange, minChange, maxChange


# In[7]:


# Reindex to avgChange
budget_df = budget_df.set_index("Change")
budget_df.head()


# In[8]:


# Get min and max change values and months
min_date = budget_df.loc[minChange, "Date"]
max_date = budget_df.loc[maxChange, "Date"]
print(min_date,minChange)
print(max_date,maxChange)


# In[9]:


# To print the summary data
print("Financial Analysis")
print("---------------------------------")
print("Total months:  " + str(month_count))
print("Total Revenue:  " + str(total_revenue))
print("Average Revenue Change:  " + str(avgChange))
print("Greatest Increase in Revenue:  " + str(max_date) + " : " + str(maxChange))
print("Greatest Decrease in Revenue:  " + str(min_date) + " : " + str(minChange))


# In[ ]:


# Output to text file - change output file name for each budget file
output_path = os.path.join('Results', 'PyBank_2.txt')
sys.stdout=open(output_path,"w")
print("Financial Analysis")
print("---------------------------------")
print("Total months:  " + str(month_count))
print("Total Revenue:  " + str(total_revenue))
print("Average Revenue Change:  " + str(avgChange))
print("Greatest Increase in Revenue:  " + str(max_date) + " : " + str(maxChange))
print("Greatest Decrease in Revenue:  " + str(min_date) + " : " + str(minChange))
sys.stdout.close()


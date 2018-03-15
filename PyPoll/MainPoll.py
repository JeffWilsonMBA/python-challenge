
# coding: utf-8

# In[ ]:


# Import modules
import os
import pandas as pd
import numpy as np
# This is for creating and printing to the text file
import sys


# In[3]:


# Open election data file - change folder and file name as needed
election = os.path.join('raw_data', 'election_data_2.csv')
election_df = pd.read_csv(election)
election_df.head()


# In[4]:


# Calculate vote total
total_vote_count = election_df["Voter ID"].count() 
total_vote_count


# In[5]:


# List of candidates whoe received votes
candidates = election_df["Candidate"].unique()
candidates


# In[6]:


# Group by candidate
grouped_candidates_df = election_df.groupby(["Candidate"])


# In[7]:


# Number of votes by candidate
candidate_vote_count = grouped_candidates_df["Candidate"].count()

# Need to convert to %
percent_vote = round(grouped_candidates_df["Candidate"].count() / total_vote_count*100,)
# percent_vote = "{:.2%}".format(grouped_candidates_df["Candidate"].count() / total_vote_count)
# grouped_candidates_df.style.format({'percent_vote': '{:,.2%}'.format,})
# grouped_candidates_df['percent_vote'] = pd.Series(["{0:.2}%".format(percent_vote * 100)])
percent_vote


# In[8]:


# Create vote summary table
vote_summary_table = pd.DataFrame({"Percentage of Votes":percent_vote,
                                   "Number of Votes":candidate_vote_count,
                                  })
sorted_vote_summary_table = vote_summary_table.sort_values("Number of Votes", ascending=False)
sorted_vote_summary_table


# In[9]:


# Determine the winner
winner = sorted_vote_summary_table.index[0]
winner


# In[10]:


# To print the summary data
print("Election Results")
print("-----------------------------------------------")
print("Total votes:  " + str(total_vote_count))
print("-----------------------------------------------")
print(sorted_vote_summary_table)
print("-----------------------------------------------")
print("The winner is:  " + str(winner))
print("-----------------------------------------------")


# In[ ]:


# Output to text file - change output file name for each election file
output_path = os.path.join('Results', 'Election_Results_2.txt')
sys.stdout=open(output_path,"w")
print("Election Results")
print("-----------------------------------------------")
print("Total votes:  " + str(total_vote_count))
print("-----------------------------------------------")
print(sorted_vote_summary_table)
print("-----------------------------------------------")
print("The winner is:  " + str(winner))
print("-----------------------------------------------")
sys.stdout.close()


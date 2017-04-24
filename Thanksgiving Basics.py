
# coding: utf-8

# In[5]:

import pandas as pd

data = pd.read_csv("thanksgiving.csv", encoding="Latin-1")
data.head(3)


# In[6]:

data.columns


# In[7]:

data["Do you celebrate Thanksgiving?"].value_counts()


# In[8]:

data["What is typically the main dish at your Thanksgiving dinner?"].value_counts()
tofurkey_data = data[data["What is typically the main dish at your Thanksgiving dinner?"] == "Tofurkey"]
tofurkey_data["Do you typically have gravy?"]


# In[12]:

apple_pie = data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"]
pumpkin_pie = data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"]
pecan_pie = data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"]

apple_isnull = pd.isnull(apple_pie)
pumpkin_isnull = pd.isnull(pumpkin_pie)
pecan_isnull = pd.isnull(pecan_pie)

ate_pies = apple_isnull & pumpkin_isnull & pecan_isnull
ate_pies.value_counts()


# In[15]:

def age_tf(age_str):
    if pd.isnull(age_str):
        return None
    age_str = age_str.split(" ")[0]
    age_str = age_str.replace("+","")
    age_str = int(age_str)
    return age_str

age = data["Age"]
data["int_age"] = age.apply(age_tf)
data["int_age"].describe()


# # Findings
# 
# Although we only have a rough approximation of age, and it skews downward because we took the first value in each string (the lower bound), we can see that that age groups of respondents are fairly evenly distributed.
# 

# In[17]:

def income_tf(income_str):
    if pd.isnull(income_str):
        return None
    income_str = income_str.split(" ")[0]
    if income_str == "Prefer":
        return None
    income_str = income_str.replace("$","")
    income_str = income_str.replace(",","")
    income_str = int(income_str)
    return income_str

income = data["How much total combined money did all members of your HOUSEHOLD earn last year?"]
data["int_income"] = income.apply(income_tf)
data["int_income"].describe()


# # Findings
# 
# The income breakdown of the survey participants is - based on the percentile amounts - skewed left and downward, since we took the first amount from the range. The mean is significantly higher than the median and the std deviation is high.

# In[19]:

data[data["int_income"] < 150000]["How far will you travel for Thanksgiving?"].value_counts()


# In[20]:

data[data["int_income"] > 150000]["How far will you travel for Thanksgiving?"].value_counts()


# # Findings
# 
# The theory that people with a lower salary more frequently travel to their parents holds, as they are less inclined to travel far and host Thanksgiving at their own residences.

# In[21]:

data.pivot_table(index = "Have you ever tried to meet up with hometown friends on Thanksgiving night?", columns = 'Have you ever attended a "Friendsgiving?"', values = "int_age")


# In[22]:

data.pivot_table(index = "Have you ever tried to meet up with hometown friends on Thanksgiving night?", columns = 'Have you ever attended a "Friendsgiving?"', values = "int_income")


# # Findings
# 
# Younger people (who are generally of a lower income bracket) are more likely to meet with friends on Thanksgiving night or attend a "Friendsgiving."

# In[ ]:




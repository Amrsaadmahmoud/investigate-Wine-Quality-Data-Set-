
# coding: utf-8

# # about Wine Quality Data Set

# There are two datasets that provide information on samples of red and white variants of the Portuguese "Vinho Verde" wine. Each sample of wine was rated for quality by wine experts and examined with physicochemical tests. Due to privacy and logistic issues, only data on these physicochemical properties and quality ratings are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.)

# # step(1):-Gathering Data

# In[41]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().magic('matplotlib inline')


# In[9]:

df_red=pd.read_csv('E:/NTL/winequality-red.csv',sep=';')
df_red.head(5)


# In[17]:

df_white=pd.read_csv('E:/NTL/winequality-white.csv',sep=';')
df_white.head(5)


# # step(2):-Assessing Data

# In[11]:

df_red.shape


# In[12]:

df_white.shape


# In[14]:

df_red.isnull().sum()


# In[15]:

df_white.isnull().sum()


# In[18]:

sum(df_red.duplicated())


# In[19]:

sum(df_white.duplicated())


# In[21]:

df_red['quality'].nunique()


# In[22]:

df_white['quality'].nunique()


# In[23]:

df_red['density'].mean()


# In[24]:

df_white['density'].mean()


# # step(3):-Appending Data

# In[26]:

df_red.rename(columns={'total_sulfur-dioxide':'total_sulfur_dioxide'}, inplace=True)


# Create Color Columns

# Create two arrays as long as the number of rows in the red and white dataframes that repeat the value “red” or “white.”

# In[27]:

# create color array for red dataframe
color_red = np.repeat('red', df_red.shape[0])

# create color array for white dataframe
color_white = np.repeat('white', df_white.shape[0])


# Add arrays to the red and white dataframes.

# In[29]:

df_red['color']=color_red
df_red.head(5)


# In[30]:

df_white['color']=color_white
df_white.head(5)


# Combine DataFrames

# In[31]:

wine_df=df_red.append(df_white)


# In[36]:

wine_df.head(5)


# rename the columns name

# In[38]:

col=['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar',
       'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density',
       'pH', 'sulphates', 'alcohol', 'quality', 'color']


# In[39]:

wine_df.columns=col


# In[40]:

wine_df.head(2)


# # step(4):-EDA with Visuals

# In[42]:

wine_df.head(5)


# In[43]:

wine_df['fixed_acidity'].hist()


# In[44]:

wine_df['total_sulfur_dioxide'].hist()


# In[45]:

wine_df['pH'].hist()


# In[47]:

wine_df['alcohol'].hist()


# In[50]:

wine_df.plot(x="volatile_acidity",y="quality",kind="scatter")


# In[51]:

wine_df.plot(x="residual_sugar",y="quality",kind="scatter")


# In[52]:

wine_df.plot(x="pH",y="quality",kind="scatter")


# In[53]:

wine_df.plot(x="alcohol",y="quality",kind="scatter")


# # step(5):-Drawing Conclusions

# Is a certain type of wine associated with higher quality?

# In[54]:

wine_df.groupby('color').mean().quality


# What level of acidity receives the highest average rating?

# In[56]:

wine_df['pH'].describe()


# In[57]:

bin_edges = [2.72, 3.11, 3.21, 3.32, 4.01] 


# In[58]:

bin_names = ['high', 'mod_high', 'medium', 'low']


# In[60]:

wine_df['acidity_levels'] = pd.cut(wine_df['pH'], bin_edges, labels=bin_names)


# In[61]:

wine_df.head(5)


# In[62]:

wine_df.groupby('acidity_levels').mean().quality


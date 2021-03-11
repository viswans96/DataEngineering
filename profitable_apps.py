#!/usr/bin/env python
# coding: utf-8

# # Profitable App profiles for App store and Google play

# In[21]:


from csv import reader
open_f = open('googleplaystore.csv')
read_f = reader(open_f)
android = list(read_f)
android_h = android[0]
android = android[1:]

### The App Store data set ###
open_f = open('AppleStore.csv')
read_f = reader(open_f)
ios = list(read_f)
ios_h = ios[0]
ios = ios[1:]


# In[34]:


def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n')
        
    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))


# # Deleting wrong row

# In[23]:


print(len(android))
del android[10472]  # don't run this more than once
print(len(android))


# # Analyzing duplicate entries

# In[24]:


for app in android:
    name = app[0]
    if name == 'Instagram':
        print(app)


# In[26]:


dup_apps = []
uniq_apps = []

for app in android:
    name = app[0]
    if name in unique_apps:
        dup_apps.append(name)
    else:
        uniq_apps.append(name)


# In[27]:


reviews_h = {}

for app in android:
    name = app[0]
    reviews_n = float(app[3])
    
    if name in reviews_h and reviews_h[name] < reviews_n:
        reviews_h[name] = reviews_n
        
    elif name not in reviews_h:
        reviews_h[name] = reviews_n


# # retain the rows with max reviews

# In[28]:


android_clean = []
already_added = []

for app in android:
    name = app[0]
    reviews_n = float(app[3])
    
    if (reviews_h[name] == reviews_n) and (name not in already_added):
        android_clean.append(app)
        already_added.append(name)


# In[29]:


def is_valid(string):
    non_ascii = 0
    
    for char in string:
        if ord(char) > 127:
            non_ascii += 1
    
    if non_ascii > 3:
        return False
    else:
        return True


# In[36]:


print(ios[0])


# # don't retain non english app names 

# In[37]:


android_english = []
ios_english = []

for appl in android_clean:
    name = appl[0]
    if is_valid(name):
        android_english.append(appl)
        
for appl in ios:
    name = appl[1]
    if is_valid(name):
        ios_english.append(appl)
        
explore_data(android_english, 0, 3, True)
print('\n')
explore_data(ios_english, 0, 3, True)


# # isolate free apps

# In[45]:


android_final = []
ios_final = []

for appl in android_english:
    price = appl[7]
    if price == '0':
        android_final.append(appl)
        
for appl in ios_english:
    price = appl[4]
    if price == '0.0':
        ios_final.append(appl)       


# # frequency table showing percentages

# In[46]:


def frequency_table(ds, ind):
    table = {}
    total = 0
    
    for row in ds:
        total += 1
        value = row[ind]
        if value in table:
            table[value] += 1
        else:
            table[value] = 1
    
    table_percents = {}
    for key in table:
        percent = (table[key] / total) * 100
        table_percents[key] = percent 
    
    return table_percents


# In[47]:


def displ_table(ds, ind):
    table = frequency_table(ds, ind)
    table_displ = []
    for key in table:
        key_val_tuple = (table[key], key)
        table_displ.append(key_val_tuple)
        
    table_sorted = sorted(table_displ, reverse = True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])


# # For App store free English Apps, 58 % are games Apps 

# In[49]:


displ_table(ios_final, -5)


#  # For Google play store free English, 18.9 % are family Apps

# In[50]:


displ_table(android_final, 1)


# # avg number of user ratings per app genre on the App Store:

# In[51]:


genres_ios = frequency_table(ios_final, -5)

for genre in genres_ios:
    total = 0
    len_genre = 0
    for app in ios_final:
        genre_app = app[-5]
        if genre_app == genre:            
            n_ratings = float(app[5])
            total += n_ratings
            len_genre += 1
    avg_n_ratings = total / len_genre
    print(genre, ':', avg_n_ratings)


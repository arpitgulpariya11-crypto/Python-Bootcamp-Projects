#!/usr/bin/env python
# coding: utf-8

# # Automatic File Sorter in File Explorer

# In[ ]:


import os, shutil, time   ##os to import operating system ,shutil,time to perform complex oprations 


# In[ ]:


path = r"S:/data-analyst/python_tutorial_file/"   ## r to convert the srt into raw string so it won't mislead by special characters 


# In[ ]:


folder_name = ['png files','jpg files','csv files','text files']

# create new folder with folder_name using range in for loop,

for loop in range(0,4):
    if not os.path.exists(path + folder_name[loop]):
        print( path + folder_name[loop])
        os.makedirs(path + folder_name[loop])


# In[ ]:


# creat a while loop and add timer to relocate each file in every 60 sec in specific folder

while True :

    file_name = os.listdir(path)   ## to se the file type in folder,

    # use if-else statement to categorise each file according to file type abd move them to specific folder.

    for file in file_name:
        if ".csv" in file and not os.path.exists(path + "csv files/" + file):
            shutil.move(path + file, path + "csv files/" + file)
        elif ".png" in file and not os.path.exists(path + "png files/" + file):
            shutil.move(path + file, path + "png files/" + file)
        elif ".jpg" in file and not os.path.exists(path + "jpg files/" + file):
            shutil.move(path + file, path + "jpg files/" + file)
        elif ".txt" in file and not os.path.exists(path + "text files/" + file):
            shutil.move(path + file, path + "text files/" + file)

    time.sleep(60)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





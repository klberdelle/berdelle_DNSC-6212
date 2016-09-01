
# coding: utf-8

# Before you turn this problem in, make sure everything runs as expected. First, **restart the kernel** (in the menubar, select Kernel$\rightarrow$Restart) and then **run all cells** (in the menubar, select Cell$\rightarrow$Run All).
# 
# Make sure you fill in any place that says `YOUR CODE HERE` or "YOUR ANSWER HERE", as well as your name and collaborators below:

# In[1]:

NAME = "Kelly Berdelle"
COLLABORATORS = ""


# ---

# # Exercise 1 - Shell basics
# 
# Work through as much of the Software Carpentry [lesson on the Unix Shell](http://swcarpentry.github.io/shell-novice/) as you can.  Run through the Setup section just below, then open a terminal through Jupyter to run through the exercises.
# 
# After you have completed the first few sections of the tutorial, return to this notebook.  Execute all of the cells, and answer all of the questions.
# 
# 
# ## Setup - getting required files 
# 
# To get started, you'll need to have the required files in your directory.  Use `wget` to get them:

# In[2]:

get_ipython().system('wget http://swcarpentry.github.io/shell-novice/data/shell-novice-data.zip')


# In[3]:

get_ipython().system('unzip -l shell-novice-data.zip')


# In[4]:

get_ipython().system('unzip shell-novice-data.zip')


# *Note*: you only need to do this once per session while using Jupyter on datanotebook.org.  You can open a terminal now and work through the steps, and return to this notebook a little later, and the files will be available either way.  That's because you're working in the same local directory.
# 
# **However**!  If you download this file, close your Jupyter session for the night, then come back tomorrow and open up a new Jupyter session on the server again, you'll need to get those sample files again.  Just execute the cells above to do it.
# 
# Okay, let's get on with the exercise!

# ## Navigating Files and Directories
# 
# As you work through this section of the tutorial, complete the steps here as well, using the `!` shell escape command.  Execute each cell as you go.
# 
# These steps aren't exactly the same as what's in the tutorial, where the file layout is a little different and where they're not using a notebook like we are.  That's okay.  Just consider this practice.

# In[5]:

get_ipython().system('whoami')


# In[6]:

get_ipython().system('pwd')


# In[7]:

get_ipython().system('ls -F')


# In[8]:

get_ipython().system('ls -F')


# In[9]:

get_ipython().system('ls -F /home/klberdelle/data-shell/')


# In[10]:

get_ipython().system('ls -aF')


# In[11]:

get_ipython().system('ls -af .')


# What is the difference between the two previous cells, and what does the single dot mean?

# The first cell includes the current directory, and the single dot indicates current directory.

# In[12]:

get_ipython().system('ls -F ..')


# What do the double dots mean?

# Double dots indicate the higher directory

# In[13]:

get_ipython().system('ls /home/klberdelle/data-shell/north-pacific-gyre/2012-07-03/')


# ## Working with Files and Directories
# 
# The following cells come from the next section of the tutorial.

# In[14]:

get_ipython().system('ls -F')


# In[15]:

get_ipython().system('mkdir thesis')


# In[16]:

import os
assert "thesis" in os.listdir()


# In[17]:

get_ipython().system('ls -F')


# You can't use the nano editor here in Jupyter, so we'll use the `touch` command to create an empty file instead.

# In[18]:

get_ipython().system('touch thesis/draft.txt')


# In[19]:

assert "draft.txt" in os.listdir("thesis")


# In[20]:

get_ipython().system('ls -F thesis')


# Removing files and directories.

# In[21]:

get_ipython().system('rm thesis/draft.txt')


# In[22]:

assert "draft.txt" not in os.listdir("thesis")


# In[23]:

get_ipython().system('rm thesis')


# In[24]:

get_ipython().system('rmdir thesis')


# In[25]:

assert "thesis" not in os.listdir()


# In[26]:

get_ipython().system('ls')


# Renaming and copying files.

# In[27]:

get_ipython().system('touch draft.txt')


# In[28]:

assert "draft.txt" in os.listdir()


# In[29]:

get_ipython().system('mv draft.txt quotes.txt')


# In[30]:

assert "quotes.txt" in os.listdir()
assert "draft.txt" not in os.listdir()


# In[31]:

get_ipython().system('ls')


# In[32]:

get_ipython().system('cp quotes.txt quotations.txt')


# In[33]:

assert "quotes.txt" in os.listdir()
assert "quotations.txt" in os.listdir()


# In[ ]:




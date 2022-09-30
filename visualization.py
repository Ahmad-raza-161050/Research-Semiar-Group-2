import re
import emoji
import nltk
import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools
import nltk
import matplotlib.pyplot as plt
import numpy as np
import random
import ipdb

keywords_list1=["mask", "N95", "surgicalmasks", "FFP2"]
fig = plt.figure()

row = [5, 100, 105, 12]

ax = fig.add_axes([0,0,1,1])
column = keywords_list1
ax.bar(column,row)
plt.show()

colors = ""



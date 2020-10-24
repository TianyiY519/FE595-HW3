#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 19:06:31 2020

@author: tianyiyang
"""

import pandas as pd
from textblob import TextBlob
import sys
sys.path.append('/Users/tianyiyang/Desktop/')
import merge_data
names1=merge_data.names1
purpose1 = merge_data.purpose1
# sentiment analysis
polarity=[TextBlob(x).sentiment[0] for x in purpose1]
subjectivity=[TextBlob(x).sentiment[1] for x in purpose1]

# creat dataframe
data=pd.DataFrame({'names':names1,'purpose':purpose1,'polarity':polarity,'subjectivity':subjectivity})

# best and worst
print(data.sort_values('polarity')[['names','polarity']]) # sort

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 23:14:52 2020

@author: tianyiyang
"""
# This is the total of the HW3's code.
# import packages
import pandas as pd
from textblob import TextBlob
from collections import Counter
# set path
path=r'/Users/tianyiyang/Downloads/'
# 'companies.txt', 'inputs.txt', 'output-1.txt', 'output.txt', 'web_scrape.txt'

# Mengge's data
f = open(path+'companies.txt')
txt=f.read()
f.close()
txt_split=txt.split(sep='\n')
names1=[txt_split[3*x+1].replace('Name: ','') for x in range(0,50)]
purpose1=[txt_split[3*x+2].replace('Purpose: ','') for x in range(0,50)]

# Tianyi Yang's data
f = open(path+'inputs.txt')
txt=f.read()
f.close()
txt_split=txt.split(sep='\n')
names2=[txt_split[2*x].replace('Name: ','') for x in range(0,50)]
purpose2=[txt_split[2*x+1].replace('Purpose: ','') for x in range(0,50)]

# Jiefu Dong's data
f = open(path+'output-1.txt')
txt=f.read()
f.close()
txt_split=txt.split(sep=']\n[')
names3=[txt_split[2*x].replace('[\'Name\', \' ','').replace('\'','').replace('Name,  ','') for x in range(0,50)]
purpose3=[txt_split[2*x+1].replace('[\'Purpose\', \' ','').replace('\'','').replace('Purpose,  ','').replace(']\n','') for x in range(0,50)]

# Han Luo's data
f = open(path+'output.txt')
txt=f.read()
f.close()
txt_split=txt.split(sep=']\n[')
names4=[txt_split[2*x].replace('[\'Name\', \' ','').replace('\'','').replace('Name,  ','') for x in range(0,50)]
purpose4=[txt_split[2*x+1].replace('[\'Purpose\', \' ','').replace('\'','').replace('Purpose,  ','').replace(']\n','') for x in range(0,50)]


# Zhixuan Xia's data
f = open(path+'web_scrape.txt')
txt=f.read()
f.close()
txt_split=txt.split(sep='\n')
names5=[txt_split[3*x].replace('Name: ','') for x in range(0,50)]
purpose5=[txt_split[3*x+1].replace('Purpose: ','') for x in range(0,50)]

# merge them into one file
names1.extend(names2)
names1.extend(names3)
names1.extend(names4)
names1.extend(names5)

purpose1.extend(purpose2)
purpose1.extend(purpose3)
purpose1.extend(purpose4)
purpose1.extend(purpose5)

# sentiment analysis
polarity=[TextBlob(x).sentiment[0] for x in purpose1]
subjectivity=[TextBlob(x).sentiment[1] for x in purpose1]

# creat dataframe
data=pd.DataFrame({'names':names1,'purpose':purpose1,'polarity':polarity,'subjectivity':subjectivity})

# best and worst
print(data.sort_values('polarity')[['names','polarity']]) # sort

# common words
char=''
for txt in purpose1:
    char=char+' '+txt

word_freq=Counter(char.lower().split(' '))
print(word_freq.most_common(10))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 19:22:14 2020

@author: tianyiyang
"""

import sys
sys.path.append('/Users/tianyiyang/Desktop/')
import merge_data
from collections import Counter
names1=merge_data.names1
purpose1 = merge_data.purpose1
# common words
char=''
for txt in purpose1:
    char=char+' '+txt

word_freq=Counter(char.lower().split(' '))
print(word_freq.most_common(10))
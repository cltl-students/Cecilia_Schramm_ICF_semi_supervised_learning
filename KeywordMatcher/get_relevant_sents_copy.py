#!/usr/bin/env python
# coding: utf-8

# In[1]:


# ellemijn's data: /mnt/data/Users/A-PROOF/ellemijn/a-proof-zonmw-main/ANNOTATIONS_INCEPTION/
# jenia's data: /mnt/data/A-Proof/data2/a-proof-zonmw/data/expr_sept/
# sharona's data: /mnt/data/Users/A-PROOF/sharona/homedirs/sharona/Documents/a-proof-zonmw-main/data/for_ml/clf_domains/

# python3 'get_relevant_sents_copy.py'


import pandas as pd
import pickle
import numpy as np
import json
import spacy
import os
import nl_core_news_sm
import pickle
from tqdm import tqdm


# In[3]:

print("checking for duplicates now...")

nlp = spacy.load("nl_core_news_sm")

path1 = "/mnt/data/Users/A-PROOF/Cecilia_S/keyword_matches_notes/keyword_matches_"
path2 = "/index_"
years = ["2017", "2018", "2020", "20-21"]
duplicates = []
data = []

for year in years:
    with open(path1 + year + path2 + year + ".json") as file:
        indexes = json.load(file)
        for category, notes in indexes.items():
            for note in tqdm(notes):
                with open(path1+year+"/"+note, 'r') as infile:
                    text = infile.read().replace('O', '')
                    text = text.replace('\n', '')
                    text = text.replace('  ', ' ')
                    doc = nlp(text)
                    for sent in doc.sents:
                        if sent in duplicates:
                            continue
                        if sent not in duplicates:
                            duplicates.append(sent)
                            if category == "B1300":
                                cat = "ENR"
                            if category == "B140":
                                cat = "ATT"
                            if category == "B152":
                                cat = "STM"
                            if category == "B440":
                                cat = "ADM"
                            if category == "B455":
                                cat = "INS"
                            if category == "B530":
                                cat = "MBW"
                            if category == "D450":
                                cat = "FAC"
                            if category == "D550":
                                cat = "ETN"
                            if category == "D840-D859":
                                cat = "BER"
                            data.append([cat, sent])
                            
all_sents = pd.DataFrame(data, columns=["category", "text"])

print("saving dataframe now...")

all_sents.to_csv("/mnt/data/Users/A-PROOF/Cecilia_S/keyword_matches_notes/all_sents_nodup.csv", index=False)

print("done")




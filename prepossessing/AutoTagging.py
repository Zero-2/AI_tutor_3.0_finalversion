# -*- coding: utf-8 -*-
import pandas as pd
import re, string
import os

def listdir(path, list_name):  # 传入存储的list
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        list_name.append(file_path)
    list_name.pop()

list_name = []
gjpath = r"C:\Users\86137\Desktop\Concepts(9ch)"   #you need to change this address according to the address of your data directory
listdir(gjpath,list_name)
print(list_name)
txt_path = "../prepossessing/tagging_data.txt"
file_txt = open(txt_path,"a+")
for path in list_name:
    gj = pd.read_excel(path, sheet_name=1)
    gjlabel = list(gj)
    for r in range(len(gj)):
        question_Raw = str(gj.loc[r][gjlabel[4]])
        entity_raw = str(gj.loc[r][gjlabel[5]])
        # question_raw_split = re.split(" ",question_Raw)
        question_raw_split=re.findall(r"[\w']+|[.,!?;]",question_Raw)
        entity_raw_split = re.split(" ",entity_raw)
        length1 = len(question_raw_split)
        length2= len(entity_raw_split)
        tagging = []
        for i in range(length1):
            tagging.append("o")
        for i in range(length2):
            for h in range(length1):
                if (i == 0):
                    if entity_raw_split[i].lower() == question_raw_split[h].lower():
                        tagging[h] = "B_entity"
                else:
                    if entity_raw_split[i].lower() == question_raw_split[h].lower():
                        tagging[h] = "I_entity"
        for i in range(length1):
            file_txt.write(question_raw_split[i])
            file_txt.write(" ")
            file_txt.write(tagging[i])
            file_txt.write('\n')
        file_txt.write('\n')
    # print(path)
# -*- coding: utf-8 -*-
from py2neo import Graph, Node, Relationship, NodeMatcher
import pandas as pd
import os

def listdir(path, list_name):  # 传入存储的list
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        list_name.append(file_path)
    # list_name.pop()


list_name = []
gjpath = r"C:\Users\86137\Desktop\Concepts(9ch)" #you need to change this address according to the address of your data directory
listdir(gjpath,list_name)
graph = Graph("http://localhost:7474", auth=("neo4j", "neo4j"))
node_matcher = NodeMatcher(graph)
print(list_name)
for path in list_name:
    gj = pd.read_excel(path)
    gjlabel = list(gj)
    for i in range(len(gj)):
        node1 = node_matcher.match("Nodes").where(name=str(gj.loc[i][gjlabel[3]]).lower()).first()
        node2 = node_matcher.match("Nodes").where(name=str(gj.loc[i][gjlabel[5]]))

        if node2.exists():
            #case 1: has repetition on second node
            continue
        if(node1 == None):
            print("case 2: has repetition on first node")
            concept = Node("Nodes", name = str(gj.loc[i][gjlabel[3]]).lower())
            content = Node("Nodes", name = str(gj.loc[i][gjlabel[5]]))
            graph.create(Relationship(concept, str(gj.loc[i][gjlabel[4]]), content))
        else:
            print("case 3: no repetition on first node")
            content = Node("Nodes", name=str(gj.loc[i][gjlabel[5]]))
            graph.create(Relationship(node1, str(gj.loc[i][gjlabel[4]]), content))

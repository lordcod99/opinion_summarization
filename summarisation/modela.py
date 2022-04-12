import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize 

class Node:

     def __init__(self,name,pos,sid,pid):

        self.name = name
        self.pos = pos
        self.id = [[sid,pid]]
        self.link = []

f = open('f.txt','r')   
v = []

for x in f:
    y = nltk.word_tokenize(x.lower())
    z = nltk.pos_tag(y)
    v.append(z)

f.close()

lp = {}
wp ={}

for x in range(len(v)):
    lp[x+1] = Node(x+1,"PO",x+1,0)
    for y in range(len(v[x])):
        if v[x][y][0] not in wp.keys(): wp[v[x][y][0]] = Node(v[x][y][0],v[x][y][1],x+1,y+1)
        else: wp[v[x][y][0]].id.append([x+1,y+1])
        if y == 0: lp[x+1].link.append(v[x][y][0])
        else: wp[v[x][y-1][0]].link.append(v[x][y][0])

for x in wp: print(wp[x].name)

#lematization 
import nltk
from nltk.stem import WordNetLemmatizer


class Node:

     def __init__(self,name,pos,sid,pid):

        self.name = name
        self.pos = pos
        self.id = [[sid,pid]]
        self.link = []

f = open('file.txt','r')   
v = []

lemma = WordNetLemmatizer()

for x in f:
    y = nltk.word_tokenize(x.lower())
    z = nltk.pos_tag(y)
    size=len(z)
    for i in  range(size):
        l=list(z[i])
        l[0]=lemma.lemmatize(l[0],pos="v")
        z[i]=tuple(l)
    v.append(z)

f.close()

# print(v)

# cc = 0
lp = {}
wp ={}

# for x in v:
#     for y in x: print(y[0])

for x in range(len(v)):
    lp[x+1] = Node(x+1,"PO",x+1,0)
    for y in range(len(v[x])):
        if v[x][y][0] not in wp.keys(): wp[v[x][y][0]] = Node(v[x][y][0],v[x][y][1],x+1,y+1)
        else: wp[v[x][y][0]].id.append([x+1,y+1])
        if y == 0: lp[x+1].link.append(v[x][y][0])
        else: wp[v[x][y-1][0]].link.append(v[x][y][0])

for x in wp: print(wp[x].name,'\t',wp[x].id,'\t',wp[x].link)









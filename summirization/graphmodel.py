# from asyncio.windows_events import NULL
from nltk.tokenize import sent_tokenize, word_tokenize

class info:
    pos = "NULL"
    psi = [] #will have list [sid , pid]
    arc = []

    # def add_psi(self,id):#node):#,tag):
    #     self._psi.append(id)
    # def add_arc(self,node):
    #     self._arc.append(node)
    #     # self._arc.append(node)
    #     # self._pos = tag



class datagraph:

    _graph= dict()          #_graph= dict({"arc":[],"psi":[]}) our data type arc will store
                            #directed nodes psi have positional information 

    def buildGraph(self,data):
        n=len(data)
        for i in range(n):       #interate through secntnace 
            words = word_tokenize(data[i])
            s=len(words)
            for j in range(s): #iterate through words 
                if(words[j] in self._graph):                             #if node existed we add psi
                    # self._graph[words[j]]['psi'].append({'sid':i+1,'pid':j+1})
                    self._graph[words[j]].psi.append([i+1,j+1])
                else:
                    self._graph[words[j]]=info()         #else create new node and add psi
                    self._graph[words[j]].psi.append([i+1,j+1])


                if(j>0):
                    if(words[j] in self._graph[words[j-1]].arc):    # if arc exist between j-1 and j nodes we add new arc 
                      continue
                    else:
                        self._graph[words[j-1]].arc.append(words[j])
        return self._graph

    
    def p(self):
        for key,value in self._graph.items():
            print(key,":",value)




d ="""
The iPhone is a great device.
The iPhone is worth the price
"""
s=sent_tokenize(d)

g=datagraph()

g=g.buildGraph(s)
# g.p()

for key,value in g.items():
            print(key,":",value.pos," ",value.psi," ",value.arc)


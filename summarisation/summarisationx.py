import string
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet



class Node:

     def __init__(self,name,sid,pid):

        self.name = name
        # self.pos = pos
        self.id = [[sid,pid]]
        self.link = []
        # self.count =  count


f = open('file.txt','r')
data = []

for l in f:
    data.append(l)

f.close()


n = len(data)
word_count = {}
totalwc =  0
stopwords = stopwords.words("english")
punc = string.punctuation

for i in punc:
    stopwords.append(i)

max_freq = 1
 
for line in data:
    words = nltk.word_tokenize(line.lower())
    for word in words:
        if word not in stopwords:
            if word not in word_count.keys():
                word_count[word]=1
            else:
                word_count[word]+=1
                max_freq = max(max_freq,word_count[word])


for k in word_count.keys():
    word_count[k]/=max_freq
 


avg_score = 0

for l in range(n):
    words=nltk.word_tokenize(data[l].lower())
    score=0
    for word in words:
        if word not in stopwords:
            score+=word_count[word]
    data[l] = [data[l],score]
    avg_score+=score

avg_score/=n

ss = []

for line in data:
    if line[-1] > avg_score:
        ss.append(line)




ss=sorted(ss,key=lambda a:a[-1],reverse=True)


v = []
for i in range(len(ss)):
    if i<20:
        ss[i].pop()
        words=nltk.word_tokenize(ss[i][0].lower())
        v.append(words)

        
# for s in v:
#     print(s)

wp = {}

for x in range(len(v)):
    # lp[x+1] = Node(x+1,"PO",x+1,0)
    for y in range(len(v[x])):
        if v[x][y] not in wp.keys():
            wp[v[x][y]] = Node(v[x][y],x+1,y+1)
        else: 
            wp[v[x][y]].id.append([x+1,y+1])
            # wp[v[x][y][0]].count+=1
        # if y == 0: lp[x+1].link.append(v[x][y][0])
        # elif v[x][y][0] not in wp[v[x][y-1][0]].link: wp[v[x][y-1][0]].link.append(v[x][y][0])
        if y!=0:
            if v[x][y] not in wp[v[x][y-1]].link: wp[v[x][y-1]].link.append(v[x][y])


word_count= []
for word in wp.keys():
    if word not in stopwords and len(word)>2:
        word_count.append([word,len(wp[word].id)])
        # c+=len(wp[word].id)


word_count =  sorted(word_count,key= lambda a:a[-1],reverse=True)

ven = [",","."]

c=0

rqrd_pos = ['a','n','v','r']
summary = []
for w in word_count:
    print(w)


for word in word_count:
    if word[1]>3:
        word = word[0]
        # print(word)
        p = wp[word].id
        # print(p)
        l = min(2,len(p))
        for i in range(l):
            sid = p[i][0] -1
            pid =  p[i][1] -1
            # print(sid," ",pid)
            line = v[sid]
            str = ""
            for i in range(pid,len(line)):
                str+=(line[i]+" ")
                if line[i] in  ven:
                    break
            summary.append(str)
            c+=1
        if c>5:
            break




# for s in summary:
#     print(s)






    
    













        












   





































# v = []
# # lp = {}
# wp = {}





# alen = 0
# flen = 0
# stopwords = stopwords.words("english")
# # print(stopwords)
# punc = string.punctuation
# for x in f:
#     flen += 1 
    # y = nltk.word_tokenize(x.lower())
#     alen += len(y)
#     z = nltk.pos_tag(y)
#     v.append(z)

# f.close()

# avglen = alen/flen











# for x in range(len(v)):
#     # lp[x+1] = Node(x+1,"PO",x+1,0)
#     for y in range(len(v[x])):
#         if v[x][y][0] not in wp.keys(): 
#             if v[x][y][0] not in stopwords:
#                 wp[v[x][y][0]] = Node(v[x][y][0],v[x][y][1],x+1,y+1,1)
#         else: 
#             wp[v[x][y][0]].id.append([x+1,y+1])
#             wp[v[x][y][0]].count+=1
#         # if y == 0: lp[x+1].link.append(v[x][y][0])
#         # elif v[x][y][0] not in wp[v[x][y-1][0]].link: wp[v[x][y-1][0]].link.append(v[x][y][0])

# # for word, value in wp.items():
# #     print(word,": ",value.count)

# sl=[]

# for key in wp.keys():
#     if key not in stopwords and key not in punc:
#         sl.append([key,wp[key].count])

# sl = sorted(sl,key= lambda a:a[-1],reverse=True)

# for i in sl:
#     print(i)

# look_upw =[]
# # n=len(sl)
# for i in sl:
#     look_upw.append(i[0])
#     # i[1]/=n 

# summmary = []

# dvsn=int(avglen/4)
# vsn = []

# for word,info in wp.items():
#     if word not in stopwords:
#         c=0
#         for pri in info.id:
#             c+=pri[1]
#         if c/len(info.id)<dvsn:
#             vsn.append(word)


# for i in vsn:
#     print(i)


# for start in vsn:
#     snts = [start]
#     info = wp[start]
#     for ngb in info.link:
        


























































































# # scored_paths = []

# # def dfs(wp,sn,ven):
# #     stack = [sn]
# #     vis = [sn]
# #     vsen = []
# #     while stack:
# #         ch = False
# #         for x in wp[stack[-1]].link:
# #             if x in ven:
# #                 if stack not in vsen:
# #                     vsen.append(stack.copy())
# #                     break
# #         for x in wp[stack[-1]].link:
# #             if x not in ven and x not in vis:
# #                 ch = True
# #                 stack.append(x)
# #                 vis.append(x)
# #                 break
# #         if ch == False:
# #             stack.pop()
# #         print(vsen)
# #     return vsen

# pvsen=[]

# # def back(ls,ven):
# #     if ls[-1] in ven:
# #         pvsen.append(ls)
# #     else:
# #         n=ls[-1]
# #         for node in wp[n].link:
# #             if node not in ls:
# #                 back(ls+[node],ven)

    
# def calc_rdncy(paths,wp):
#     n = len(paths)
#     for path in range(n):
#         score =0
#         # P_id=[]
#         s=set()
#         for word in pvsen[path]:
#             id=wp[word].id
#             l = len(id)
#             for i in range(l):
#                 for j in range(l):
#                     v =abs(id[i][1]-id[j][1])
#                     if(v<5 and v>3):
#                         s.add(id[j][0])
#         pvsen[path].append(len(s))







# f = open('file.txt','r')   
# v = []

# alen = 0
# flen = 0

# for x in f:
#     flen += 1 
#     y = nltk.word_tokenize(x.lower())
#     alen += len(y)
#     z = nltk.pos_tag(y)
#     v.append(z)

# f.close()

# avglen = alen/flen

# lp = {}
# wp ={}

# for x in range(len(v)):
#     lp[x+1] = Node(x+1,"PO",x+1,0)
#     for y in range(len(v[x])):
#         if v[x][y][0] not in wp.keys(): wp[v[x][y][0]] = Node(v[x][y][0],v[x][y][1],x+1,y+1,0)
#         else: 
#             wp[v[x][y][0]].id.append([x+1,y+1])
#             wp[v[x][y][0]].count+=1
#         if y == 0: lp[x+1].link.append(v[x][y][0])
#         elif v[x][y][0] not in wp[v[x][y-1][0]].link: wp[v[x][y-1][0]].link.append(v[x][y][0])

# ven = [".",",","but","yet",";",":","?","!"]
# vsn = []

# pvsn = int(avglen/3)

# for x in wp:
#     cc = 0
#     for y in wp[x].id:
#         cc += y[1]
#     if cc/len(wp[x].id) <= pvsn:
#         vsn.append(wp[x].name)

# # for x in ven:
# #     if x in wp.keys():
# #         if wp[x].link:
# #             for y in wp[x].link:
# #                 for z in vsn:
# #                     if y not in wp[z].link and wp[y].pos != wp[z].pos:
# #                         wp[z].link.append(y)

# # vsenx = []
# # vsen = []

# # for x in vsn:
# #     vsenx.append(dfs(wp,x,ven))

# # for x in vsenx:
# #     if x:
# #         for y in x:
#             # print(y)

# # calc_rdncy(wp,s,rdncy)


# # for x in vsn:
# #     back([x],ven)

# #scoring the paths 
# # calc_rdncy(pvsen,wp) 

# # pvsen = sorted(pvsen,key= lambda a:a[-1],reverse=True)


# for x in pvsen:
#     print(x) 

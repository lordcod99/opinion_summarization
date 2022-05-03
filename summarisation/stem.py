import string
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from rouge import Rouge
from nltk.stem import PorterStemmer



class Node:

     def __init__(self,name,sid,pid):

        self.name = name
        # self.pos = pos
        self.id = [[sid,pid]]
        self.link = []
        # self.count =  count


f = open('data.txt','r')
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

# stemming using prostemmer 
pstem = PorterStemmer()

v = []
for i in range(len(ss)):
    if i<20:
        ss[i].pop()
        words=nltk.word_tokenize(ss[i][0].lower())
        for word in words:
            word = pstem.stem(word)
            print(word)
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
# for w in word_count:
#     print(w)


for word in word_count:
    if word[1]>3:
        word = word[0]
        # print(word)
        p = wp[word].id
        # print(p)
        l = min(2,len(p))
        for j in range(l):
            sid = p[j][0] -1
            pid =  p[j][1] -1
            # print(sid," ",pid)
            line = v[sid]
            str = ""
            ll=0
            rqd = 0
            for i in range(pid,len(line)):
                if line[i] in  ven:
                    str+=".\n"
                    break
                str+=(line[i]+" ")
                ll+=1
                if(line[i] not in stopwords):
                    pos = wordnet.synsets(line[i])
                    if pos:
                        pos=pos[0].pos()
                    if(pos == 'n' or pos == 'v' or pos=='a'):
                        rqd+=1
                
            if(ll>2 ):
                check = False
                for i in range(len(summary)):
                    if(summary[i].find(str) != -1): 
                        check = True
                        break
                if(check == False):
                    summary.append(str)
                    c+=1
        if c>5:
            break

for s in summary:
    print(s)


print("\n================= rouge score ======================\n")

sf = open('summary.txt', 'w')
sf.writelines(summary)

sf.close()

score = Rouge().get_scores('summary.txt','reference.txt',avg=True)

for type, values in score.items():
    print(type," ",values)









# #basic model
# import nltk


# class Node:

#      def __init__(self,name,pos,sid,pid):

#         self.name = name
#         self.pos = pos
#         self.id = [[sid,pid]]
#         self.link = []


# ven=['.',',',"but",]

# def is_valid_start(psi):
#     d=4
#     s=0
#     for i in  psi:
#         s+=i[1]
#     s=s/len(psi)
#     if(s<=d):
#         return True
#     else:
#         return False


# def is_valid_end(word):
#     ven=['.',',',"but","yet","?","!","!!","!!!"]
#     if ven.count(word)>0:
#         return True
#     else:
#         return False


# def calc_rdncy(wp,sentence,rdncy):
#     words = nltk.word_tokenize(sentence)
#     id_list=[]
#     for word in words:
#         pass

    
    

# def find_path(wp,word ,info ,score ,path_len ,sentence):
#     rdncy=len(info.id)
#     dr=3
#     if rdncy>= dr:
#         if(is_valid_end(word) or path_len>8):
#             score = score/path_len
#             return [sentence,score]

#         for ngb in info.link:
#             path_len += 1
#             rdncy=calc_rdncy(wp,sentence,rdncy)
#             score += 1
#             sentence=sentence+" "+ngb
#             print(sentence)
#             find_path(wp,ngb,wp[ngb],score,path_len,sentence)



# f = open('file.txt','r')   
# v = []

# for x in f:
#     y = nltk.word_tokenize(x.lower())
#     z = nltk.pos_tag(y)
#     v.append(z)

# f.close()



# # cc = 0
# lp = {}
# wp ={}

# # for x in v:
# #     for y in x: print(y[0])

# for x in range(len(v)):
#     lp[x+1] = Node(x+1,"PO",x+1,0)
#     for y in range(len(v[x])):
#         if v[x][y][0] not in wp.keys(): wp[v[x][y][0]] = Node(v[x][y][0],v[x][y][1],x+1,y+1)
#         else: wp[v[x][y][0]].id.append([x+1,y+1])
#         if y == 0: lp[x+1].link.append(v[x][y][0])
#         elif v[x][y][0] not in wp[v[x][y-1][0]].link : wp[v[x][y-1][0]].link.append(v[x][y][0])
#         # else: wp[v[x][y-1][0]].link.append(v[x][y][0])

# # # for x in wp: print(wp[x].name,'\t',wp[x].id,'\t',wp[x].link)


# # finding best paths

# summary = []

# for word , info in wp.items():
#     if(is_valid_start(info.id)):
#         path_len=1
#         score =0
#         sentence=word
#         summary.append(find_path(wp,word,info,score,path_len,sentence))


# print(summary)




import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize 



class Node:

     def __init__(self,name,pos,sid,pid):

        self.name = name
        self.pos = pos
        self.id = [[sid,pid]]
        self.link = []


def dfs(wp,sn,ven):
    stack = [sn]
    vis = [sn]
    vsen = []
    while stack:
        ch = False
        for x in wp[stack[-1]].link:
            if x in ven:
                if stack not in vsen:
                    vsen.append(stack.copy())
                    break
        for x in wp[stack[-1]].link:
            if x not in ven and x not in vis:
                ch = True
                stack.append(x)
                vis.append(x)
                break
        if ch == False:
            stack.pop()
    return vsen


f = open('file.txt','r')   
v = []

alen = 0
flen = 0

for x in f:
    flen += 1 
    y = nltk.word_tokenize(x.lower())
    alen += len(y)
    z = nltk.pos_tag(y)
    v.append(z)

f.close()

avglen = alen/flen

lp = {}
wp ={}

for x in range(len(v)):
    lp[x+1] = Node(x+1,"PO",x+1,0)
    for y in range(len(v[x])):
        if v[x][y][0] not in wp.keys(): wp[v[x][y][0]] = Node(v[x][y][0],v[x][y][1],x+1,y+1)
        else: wp[v[x][y][0]].id.append([x+1,y+1])
        if y == 0: lp[x+1].link.append(v[x][y][0])
        elif v[x][y][0] not in wp[v[x][y-1][0]].link: wp[v[x][y-1][0]].link.append(v[x][y][0])

# for x in wp: print(wp[x].name)

ven = [".",",","but","yet",";",":","?","!"]
vsn = []

pvsn = int(avglen/3)

for x in wp:
    cc = 0
    for y in wp[x].id:
        cc += y[1]
    if cc/len(wp[x].id) <= pvsn:
        vsn.append(wp[x].name)

# for x in ven:
#     if x in wp.keys():
#         for y in wp[x].link:
#             for z in vsn:
#                 if y not in wp[z].link:
#                     wp[z].link.append(y)

for x in ven:
    if x in wp.keys():
        if wp[x].link:
            for y in wp[x].link:
                for z in vsn:
                    if y not in wp[z].link:
                        wp[z].link.append(y)

vsen = []

for x in vsn:
    vsen.append(dfs(wp,x,ven))

# for x in vsen:
#     if x:
#         for y in x:
#             print(y)

print(wp["has"].link)














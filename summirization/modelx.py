#basic model
# import re
# import socketserver
# import nltk
# from numpy import true_divide


# class Node:

#      def __init__(self,name,pos,sid,pid):

#         self.name = name
#         self.pos = pos
#         self.id = [[sid,pid]]
#         self.link = []


# # ven=['.',',',"but",]

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
#     ven=['.',',',"but","yet"]
#     if ven.count(word)>0:
#         return True
#     else:
#         return False

# def find_path(wp,word ,info ,score ,path_len):
#     sentance = word
#     rdncy=len(info.id)
#     dr=3
#     if rdncy>= dr:
#         if(is_valid_end(word)):
#             return sentance
#     for ngb in info.link:
#         path_len += 1
#         score += 1
#         sentance+=ngb
#         find_path(wp,ngb,wp[ngb],score,path_len)



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
#         else: wp[v[x][y-1][0]].link.append(v[x][y][0])

# # for x in wp: print(wp[x].name,'\t',wp[x].id,'\t',wp[x].link)


# # finding best paths

# summary = []

# for word , info in wp.items():
#     if(is_valid_start(info.id)):
#         path_len=1
#         score =0
#         summary.append(find_path(wp,word,info,score,path_len))













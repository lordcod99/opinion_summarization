# #basic model
# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize, sent_tokenize 


# class Node:

#      def __init__(self,name,pos,sid,pid):

#         self.name = name
#         self.pos = pos
#         self.id = [[sid,pid]]
#         self.link = []



# def lineverf(line):
#     for x in range(len(line)):
#         if x == 0:
#             continue
#         if wp[line[x-1]].pos == wp[line[x]].pos:
#             return False
#     return True


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

# ven=['.',',',"?","!","!!","!!!"]

# def is_valid_end(word):
#     if ven.count(word)>0:
#         return True
#     else:
#         return False


# def calc_rdncy(wp,sentence,rdncy):
#     words = nltk.word_tokenize(sentence)
#     id_list=[]
#     for word in words:
#         l=wp[word].link


    
    

# # def find_path(wp,word ,info ,score ,path_len ,sentence,cand):
# #     rdncy=len(info.id)
# #     dr=3
# #     if rdncy>= dr:
# #         if(is_valid_end(word) or path_len>8):
# #             if(lineverf(cand)):
# #                 score = score/path_len
# #                 return sentence

# #         for ngb in info.link:
# #             path_len += 1
# #             rdncy=calc_rdncy(wp,sentence,rdncy)
# #             score += 1
# #             sentence=sentence+" "+ngb
# #             cand.append(ngb)
# #             print(sentence)
# #             find_path(wp,ngb,wp[ngb],score,path_len,sentence,cand)



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

# vsnn = []

# for x in wp.keys():
#     if wp[x].link:
#         cc = 0
#         for y in wp[x].id:
#             cc += y[1]
#         if cc/len(wp[x].id) <= 3:
#             vsnn.append(wp[x].name)

# for x in ven:
#     if x in wp.keys():
#         if wp[x].link:
#             for y in wp[x].link:
#                 for z in vsnn:
#                     if y not in wp[z].link and wp[y].pos != wp[z].pos:
#                         wp[z].link.append(y)


# # print(vsnn)


# # finding best paths

# summary = []
# cand = []
# i = 1


# for word , info in wp.items():
#     if(is_valid_start(info.id)):
#         path_len=1
#         score=0
#         print(word,":=====")
#         for ngb in wp[word].link:
#             print(ngb)
#             # cndl=[word]
#             # cndl.append(ngb)
#             # if ngb in ven:
#             #     print(i)
#             #     i+=1
#             #     summary.append(cndl)
#             #     break



# # print(summary)
          


        


# # print(summary)










import numpy as np
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
from rouge import FilesRouge



# data = pd.read_csv('articles.csv', encoding='unicode_escape')
# #print(data['article_text'][2])


# sentences_list = []
# for x in data['article_text']:
#     sentences_list.append(sent_tokenize(x))
# sentences_list = sentences_list[8]  #only for first text!!!!!
# #sentences_list = [q for p in sentences_list for q in p]
# #print(sentences_list)

sentences_list = []

with open("data.txt",'r') as f:
    for x in f: sentences_list.append(x)


cleaned_sentences = pd.Series(sentences_list).str.replace("[^a-zA-Z]", " ", regex = True)
cleaned_sentences = [x.lower() for x in cleaned_sentences]
#print(cleaned_sentences)


stop_words = stopwords.words('english')
#print(stop_words)
def rem(x):
    y = " ".join([i for i in x if i not in stop_words])
    return y

cleaned_sentences = [rem(k.split()) for k in cleaned_sentences]
#print(cleaned_sentences)


word_embeddings = dict()
f = open('glove.6B/glove.6B.100d.txt', encoding='utf-8')
for s in f:
    val = s.split()
    word = val[0]
    coeff = np.asarray(val[1:], dtype = 'float32')
    word_embeddings[word] = coeff
f.close()


sentence_vectors = []
for i in cleaned_sentences:
    if len(i) != 0:
        v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()])/(len(i.split())+0.001)
    else:
        v = np.zeros((100,))
    sentence_vectors.append(v)


similarity_matrix = np.zeros([len(sentences_list), len(sentences_list)])
for i in range(len(sentences_list)):
    for j in range(len(sentences_list)):
        if i != j:
            similarity_matrix[i][j] = cosine_similarity(sentence_vectors[i].reshape(1, 100), sentence_vectors[j].reshape(1, 100))[0, 0]
#print(similarity_matrix)


network_graph = nx.from_numpy_array(similarity_matrix)
scores = nx.pagerank(network_graph)

summary = sorted(((scores[i], s) for i, s in enumerate(sentences_list)), reverse=True)


for i in range(5):
    print("{}. {}".format(i+1, summary[i][1]))


li = 0
with open("reference.txt",'r') as f: li = len(f.readlines())

sf = open('summary.txt', 'w')

c=0
for line in summary:
    sf.write(line[1])
    c+=1
    if(c>=li):
        break
sf.close()

print("\n================= rouge score ======================\n")

rouge_s =  FilesRouge()
score = rouge_s.get_scores('summary.txt','reference.txt',avg=True)

for type, values in score.items():
    print(type," ",values)





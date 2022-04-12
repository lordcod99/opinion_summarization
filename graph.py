import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Graph:

     def __init__(self,name,pos,sid,pid,prev):

         self.name = name
         self.pos = pos
         self.id = [[sid,pid]]
         self.link = prev


def crNode(name,sid,pid,prev):
    
    pos = "verb"
    tempNode = Graph(name,pos,sid,pid,prev)
    return tempNode

def linePointer(num):

    passVar = "line" + str(num)
    lnPoint = Graph(passVar,"LP",0,0,"null")
    return lnPoint

def tok(data):

    stop_words = stopwords.words('english')
    stop_words.append(',')
    stop_words.append("'")
    stop_words.append('.')
    words = []
    for s in data:
       w = word_tokenize(s)
       for x in w:
         if x.lower() not in stop_words and x[0] != "'":
           words.append(x)

    return words

lineNum = 0

listNodes = {}
listPointers = {}


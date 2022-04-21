import string
import nltk
from nltk.corpus import stopwords

from nltk.corpus import wordnet

s = wordnet.synsets('is')[0]
print(s.pos())
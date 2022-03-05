# from winreg import HKEY_LOCAL_MACHINE
# import nltk
# from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
import graphmodel
# from nltk.sentiment.vader import SentimentIntensityAnalyzer



text = """
Drivers seat not comfortable, the car itself compared to other models of similar class .
It's very comfortable, remarkably large inside and just an overall great vehicle .
Front seats are very uncomfortable .
I'm 6' tall, and find the driving position pretty comfortable .
However, there are a couple of things that kill it for me 1 terrible driver seat comfort, kills my back 2 lack luster interior design, my Acadia has much better comfort 3 the VCM drives me crazy because the constant change in cylinder use is perceptible enough to be an annoyance .
The seats are extremely uncomfortable .
While the Accord is no Acura it is a close relative in terms of quality and comfort .
 I previously owned a 98 Avalon, and found the seats more comfortable than the Honda .
 I'm very sad ,  I loved my daughter's Civic and the dealer service is fantastic, but even good service can't help the uncomfortable seats .
 Overall performance is good but comfort level is poor .
 The ride is a great balance between handling and comfort .
 Although it is fun to drive and quality seems ok, the leather seats are very uncomfortable, especially on a long drive .
Although not the fastest, most luxurious, or technologically advanced in the very competitive mid, size sedan segment, the Accord strikes the perfect balance of sport, comfort and value, creating a vehicle that feels and acts like a much pricier machine .
 Has lots of features, is comfortable, everything works .
 The two door coupe is very comfortable and roomy and draws plenty of attention .
 The seat is extremely uncomfortable .
 The driver's seat is very uncomfortable .
 The head rest tills forward which pushes the driver's head forward at a very uncomfortable position .
 The front driver seat's lumbar support seemed very uncomfortable at first .
 The car is comfortable and QUIET .
"""

G=graphmodel.datagraph()

sentences = sent_tokenize(text)
G.buildGraph(sentences)
G.p()














# def tok(data):

#     stop_words = stopwords.words('english')
#     stop_words.append(',')
#     stop_words.append("'")
#     stop_words.append('.')
#     words = []
#     for s in data:
#        w=word_tokenize(s)
#        for x in w:
#          if x.lower() not in stop_words and x[0] != "'":
#            words.append(x)

#     return words




# def get_freq(data):
#   freq=dict()
#   for word in data:
#     if word in freq:
#       freq[word] +=1
#     else:
#       freq[word]=1
#   return freq
# sentences = sent_tokenize(text)
# sid = SentimentIntensityAnalyzer()
# pos = []
# neg = []

# for s in sentences:
#   p = sid.polarity_scores(s)['pos']
#   n = sid.polarity_scores(s)['neg']
#   if p>n:
#     pos.append(s)
#   else:
#     neg.append(s)

# pos_words = tok(pos)
# neg_words = tok(neg)

# pos_wrds_freq = get_freq(pos_words)
# neg_wrds_freq = get_freq(neg_words)

# pos_wrds_freq = sorted(pos_wrds_freq.items(),key=lambda w:w[1],reverse = True)
# neg_wrds_freq = sorted(neg_wrds_freq.items(),key=lambda w:w[1],reverse = True)

# print(pos_wrds_freq)
# print("\n========================================================\n")
# print(neg_wrds_freq)

# print(pos_words)
# print("\n========================================================\n")
# print(neg_words)

# print(pos)
# print("\n========================================================\n")
# print(neg)






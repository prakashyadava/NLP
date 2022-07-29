import nltk
from nltk.corpus import stopwords
stopwords.words('english')

entries = nltk.corpus.cmudict.entries()
print(entries[:10])
print(len(entries))

from nltk.corpus import wordnet as wn
print(wn.synsets('motorcar'))
print(wn.synset('car.n.01').lemma_names())

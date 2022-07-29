from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
vect =CountVectorizer(binary=True)
corpus = ["Tessaract is good optical character recognition engine", "significant optical character recognition"]
vect.fit(corpus)

print(vect.transform(corpus).toarray())

vocab = vect.vocabulary_

for key in sorted(vocab.keys()):
  print("{}:{}".format(key, vocab[key]))
vect = TfidfVectorizer(binary = True)

corpus = ["CNN is good optical character recognition", "optical character recognition"]
vect.fit(corpus)

print(vect.transform(["Today is good optical"]).toarray())
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vect.transform(["Tessaract is an optical character recognition engine"]).toarray(),
                               vect.transform(["Optical character recognition"]).toarray())
print(similarity)

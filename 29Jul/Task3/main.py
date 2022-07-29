from sklearn.feature_extraction.text import CountVectorizer

vect =CountVectorizer(binary=True)
corpus = ["Tessaract is good optical character recognition engine", "significant optical character recognition"]
vect.fit(corpus)

print(vect.transform(corpus).toarray())

vocab = vect.vocabulary_

for key in sorted(vocab.keys()):
  print("{}:{}".format(key, vocab[key]))

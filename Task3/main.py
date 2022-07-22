import nltk
from nltk.stem import WordNetLemmatizer
lemma = WordNetLemmatizer()
print(lemma.lemmatize("cacti"))
print(lemma.lemmatize("better",pos="a"))
print(lemma.lemmatize("am",pos="v"))

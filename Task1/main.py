import nltk
from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["program", "programs", "programmer", "programming", "programmers"]
print("--------------------PorterStemmer--------------------")
for w in words:
	print(w, " : ", ps.stem(w))
	
from nltk.stem import LancasterStemmer
Lanc = LancasterStemmer()
print("--------------------LancasterStemmer--------------------")
for w in words:
	print(w, " : ", Lanc.stem(w))

print("--------------------RegexpStemmer--------------------")
from nltk.stem import RegexpStemmer
stemmerregexp=RegexpStemmer('ing')
wd = ["working","happiness","pairing","going","reading"]
for w in wd:
	print(w, " : ", stemmerregexp.stem(w))
	
print("--------------------SnowballStemmer--------------------")
from nltk.stem.snowball import SnowballStemmer
snow_stemmer = SnowballStemmer(language='english')
words2 = ['cared', 'university', 'fairly', 'easily', 'singing',
		 'sings', 'sung', 'singer', 'sportingly']
stem_words = []
for w in words2:
	x = snow_stemmer.stem(w)
	stem_words.append(x)
for e1, e2 in zip(words2, stem_words):
	print(e1 + ' : ' + e2)

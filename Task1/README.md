## Porter Stemmer

The Porter stemming algorithm (or 'Porter stemmer') is a process for removing the commoner morphological and inflexional endings from words in English.

### Example

```
from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["program", "programs", "programmer", "programming", "programmers",'cared', 'university', 'fairly', 'easily', 'singing',
		 'sings', 'sung', 'singer', 'sportingly']
print("--------------------PorterStemmer--------------------")
for w in words:
	print(w, " : ", ps.stem(w))

```

### Output
<img width="807" alt="Screenshot 2022-07-23 at 12 47 53 AM" src="https://user-images.githubusercontent.com/79514008/180510854-6f206627-ee9c-4ce3-a1aa-e88bdea0cd2b.png">


## Lancaster Stemmer
Lancaster Stemmer is the most aggressive stemming algorithm. It has an edge over other stemming techniques because it offers us the functionality to add our own custom rules in this algorithm when we implement this using the NLTK package. This sometimes results in abrupt results.

### Example
```
from nltk.stem import LancasterStemmer
Lanc = LancasterStemmer()
print("--------------------LancasterStemmer--------------------")
for w in words:
	print(w, " : ", Lanc.stem(w))
```
### Output
<img width="841" alt="Screenshot 2022-07-23 at 12 54 26 AM" src="https://user-images.githubusercontent.com/79514008/180513058-80ec70bc-6b6c-4955-bb1d-d17162d67bc1.png">

### RegExp Stemmer
A stemmer that uses regular expressions to identify morphological affixes. Any substrings that match the regular expressions will be removed.

### Example
```
print("--------------------RegexpStemmer--------------------")
from nltk.stem import RegexpStemmer
stemmerregexp=RegexpStemmer('ing')
wd = ["working","happiness","pairing","going","reading"]
for w in wd:
	print(w, " : ", stemmerregexp.stem(w))

```

### Output
<img width="533" alt="Screenshot 2022-07-23 at 12 58 16 AM" src="https://user-images.githubusercontent.com/79514008/180513814-34fbc47d-58cc-48f9-ba26-3585d34da252.png">

### Snowball Stemmer
It is a stemming algorithm which is also known as the Porter2 stemming algorithm as it is a better version of the Porter Stemmer since some issues of it were fixed in this stemmer.

### Example
```
print("--------------------SnowballStemmer--------------------")
from nltk.stem.snowball import SnowballStemmer
snow_stemmer = SnowballStemmer(language='english')

stem_words = []
for w in words:
	x = snow_stemmer.stem(w)
	stem_words.append(x)
for e1, e2 in zip(words, stem_words):
	print(e1 + ' : ' + e2)
```
### Output
<img width="593" alt="Screenshot 2022-07-23 at 1 00 16 AM" src="https://user-images.githubusercontent.com/79514008/180514094-881b8f88-0053-45ed-bb44-05fe30b8992d.png">


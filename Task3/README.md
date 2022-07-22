## Word Net Lemmatizer

Wordnet Lemmatizer with NLTK. Wordnet is an large, freely and publicly available lexical database for the English language aiming to establish structured semantic relationships between words. It offers lemmatization capabilities as well and is one of the earliest and most commonly used lemmatizers

### To use just type
```
import nltk
from nltk.stem import WordNetLemmatizer
lemma = WordNetLemmatizer()
print(lemma.lemmatize("cacti"))
print(lemma.lemmatize("better",pos="a"))
print(lemma.lemmatize("am",pos="v"))
```
### Output
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/79514008/180495869-bcfe2962-1bfa-4035-9537-28ce3b647d7a.png">

## NLTK Pos Tagging

POS Tagging in NLTK is a process to mark up the words in text format for a particular part of a speech based on its definition and context. Some NLTK POS tagging examples are: CC, CD, EX, JJ, MD, NNP, PDT, PRP$, TO, etc. POS tagger is used to assign grammatical information of each word of the sentence.

### To use just type
```
text = "Your Text"
for text in texts:
    sentences = nltk.sent_tokenize(texts)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(words)
        print(tagged)
```
### Output

<img width="1440" alt="image" src="https://user-images.githubusercontent.com/79514008/180498022-67819b12-ce82-45e2-a2a1-6f8924b2d61a.png">

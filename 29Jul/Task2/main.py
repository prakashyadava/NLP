import random
def gender_features(n):
    return {'last_letter':n[-1]}

from nltk.corpus import names
labeled_name = ([(name,'male')for name in names.words('male.txt')]+[(name,'female') for name in names.words('female.txt')])
# print(labeled_name)
featuresets = [(gender_features(n),gender) for(n,gender) in labeled_name]
train_set,test_test = featuresets[500:],featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(classifier.classify(gender_features("Prakash")))

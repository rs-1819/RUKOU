from model import *
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def compare(sentence, paragraph):
    sentence = re.sub(r'[^\w\s]','',sentence)
    paragraph = re.sub(r'[^\w\s]','',paragraph)
    sentence = sentence.lower()
    paragraph = paragraph.lower()
    sentence = word_tokenize(sentence)
    paragraph = word_tokenize(paragraph)
    sentence = [lemmatizer.lemmatize(word) for word in sentence if word not in stop_words]
    paragraph = [lemmatizer.lemmatize(word) for word in paragraph if word not in stop_words]
    score = 0
    for word in sentence:
        if word in paragraph:
            score += 1
            print(word)
        else:
            for syn in wn.synsets(word):
                for l in syn.lemmas():
                    if l.name() in paragraph:
                        print(l.name())
                        score += 1
    return score/len(sentence)




allsum = all_summaries()
allknowledge = all_knowledge()
scores = []
scores2 = []
sentence = ""
#sort results by highest score
for sum in allsum:
    score = compare(sentence, sum)
    if score > 0.49:
        scores.append(str(score) + "|||" + sum + "|||" + sentence)


print()
print()
for ak in allknowledge:
    score = compare(sentence, ak)
    if score > 0.49:
        scores2.append(str(score) + "|||" + ak + "|||" + sentence)


    

dim = 00
    
for result in sorted(scores, reverse=True):
    dim += 1
    print(result)
    if dim == 10:
        break
    print('')

dim = 0

for result in sorted(scores2, reverse=True):
    dim += 1
    print(result)
    if dim == 10:
        print('broke')
        break
    print(dim)

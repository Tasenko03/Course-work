import csv
with open(r"C:\Users\anoua\Downloads\123.txt", encoding='WINDOWS-1251', newline='') as csvfile:
    data = list(csv.reader(csvfile, delimiter=',', quotechar='\t'))
    data = [' '.join(row) for row in data]

with open(r"C:\Users\anoua\Downloads\russian.txt", encoding='utf-8', newline='') as csvfile:
    russian = csv.reader(csvfile, delimiter=',', quotechar=',')
    russian = [' '.join(row) for row in russian]


from nltk.tokenize import word_tokenize
from string import punctuation
from pymorphy2 import MorphAnalyzer
from nltk.corpus import stopwords

morph = MorphAnalyzer()
stopwords_ru = stopwords.words("russian")
d = []

for i in data:
    tokens = []
    words = word_tokenize(i, language="russian")
    for word in words:
            if word not in stopwords_ru and word not in punctuation:
                word = word.strip()
                word = morph.normal_forms(word)[0]
                if word in russian:
                    tokens.append(word)
    print(str(tokens))                       
    d.append(str(tokens))

with open('dict.txt', 'w',  encoding="utf-8") as f:
    for elem in d:
          f.write(str(elem))
          f.write(";")



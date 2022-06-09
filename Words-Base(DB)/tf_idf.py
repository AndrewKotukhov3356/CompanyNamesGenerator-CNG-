#TF-IDF words generator.

from sklearn.feature_extraction.text import TfidfVectorizer
from spacy.lang.ru.stop_words import STOP_WORDS
from pymorphy2 import MorphAnalyzer
from spacy.lang.ru import Russian
from string import punctuation
from pathlib import Path
import pymorphy2
import spacy
import math
import re
import pandas as pd


#Please install "https://github.com/explosion/spacy-models/releases/download/ru_core_news_sm-3.2.0/ru_core_news_sm-3.2.0.tar.gz"
nlp = spacy.load('ru_core_news_sm')
nlp.Defaults.stop_words |= {
    "например",
    "также",
    "тд",
    "–",
    "Туссана",
    "Creta",
    "Hyundai",
    "сплошь",
    "Возможно",
    "оснащена",
    "WD",
    "приветствовать",
    "выглядит",
    "Вдобавок",
    "Сзади",
    "Тоже",
    "появились",
    "стало",
    "изменилась",
    "обзаводятся",
    "Дастера",
    "китайцы",
    "многим",
    "корейского",
    "появятся",
    "безнаддувных",
    "выиграть",
    "Лада",
    "проголосовать",
    "выбрать",
    "одиннадцати",
    "Заполнить",
    "анкету",
    "Голосование",
    "завершится",
    "февраля",
    "Каждый",
    "каждый",
    "изменился",
    "стереотип",
    "стереотипам",
    "изжитым",
    "бензиновым",
    "атмосферникам",
    "гидротрансформаторным",
    "покупателям",
    "ДаKia",
    "Sorento",
    "Выбирай",
    "предлагают",
    "Duster",
    "Haval",
    "Jolion",
    "вовсе",
    "моторнотрансмиссионных",
    "доступен",
    "сочетая",
    "Семиместная",
    "Крете",
    "USBпорт",
    "исчез",
    "очечник",
    "Добавили",
    "Крету",
    "требовалось",
    "четверых",
    "Рослый",
    "Хавейла",
    "Джолион",
    "далеко",
    "увеличился",
    "заставляют",
    "покупателей",
    "посмотреть",
    "превратилась",
    "эпатажника",
    "смотрят",
    "скептически",
    "Индонезии",
    "скопирована",
    "знает",
    "выглядят",
    "светят",
    "слабо",
    "бьет",
    "недалеко",
    "галогеновыми",
    "Включаешь",
    "получаешь",
    "режущую",
    "Вкласса",
    "ждет",
    "удается",
    "изящно",
    "замаскировать",
    "Кретой",
    "царапается",
    "ощупь",
    "царапается",
    "Настолько",
    "превентивно",
    "защищают",
    "млн",
    "постепенно",
    "появляются",
    "турбонаддувом",
    "надежности",
    "претензии",
    "следующего",
    "объемом",
    "ступенчатые",
    "каждом",
    "пьян",
    "оштрафуют",
}


# Here you can input any file, for code to run
st1 = 'tes1'
st2 = 'tes2'
st3 = 'tes3'
st4 = 'st4'
st5 = 'st5'
st6 = 'st6'
st7 = 'st7'
st8 = 'st8'
st9 = 'st9'
st10 = 'st10'
st11 = 'st11'
st12 = 'st12'
st13 = 'st13'
st14 = 'st14'
st15 = 'st15'
st16 = 'st16'
st17 = 'st17'
st18 = 'st18'
st19 = 'st19'
st20 = 'st20'
st21 = 'st21'
st22 = 'st22'
st23 = 'st23'
st24 = 'st24'
st25 = 'st25'
st26 = 'st26'
st27 = 'st27'
st28 = 'st28'
st29 = 'st29'
st30 = 'st30'


# Some commented stuff...
# def tf(word, blob):
#   return (float)(blob.words.count(word)) / (float)(len(blob.words))

# def n_containing(word, bloblist):
#    return (sum(1 for blob in bloblist if word in blob))

# def idf(word, bloblist):
#    return (math.log((len(bloblist)) /(1 + n_containing(word, bloblist))))

# def tfidf(word, blob, bloblist):
#    return (float)((float)(tf(word, blob)) * (float)(idf(word, bloblist)))


def stopword(text):
    marks = '''!()-[]{};?@#$%:'"\\,./^&;*_—≈1234567890»«…'''
    for c in marks:
        text = text.replace(c, '')
    nlp = spacy.load('ru_core_news_sm')
    my_doc = nlp(text)
    morph = pymorphy2.MorphAnalyzer()

    token_list = []
    for token in my_doc:
        token_list.append(token.text)

    filtered_sentence = []

    for word in token_list:
        p = morph.parse(word)[0]
        lexeme = nlp.vocab[p.normal_form]
        if not lexeme.is_stop:
            filtered_sentence.append(p.normal_form)
    with open('listfile.txt', 'w') as filehandle:
        for listitem in filtered_sentence:
            filehandle.write('%s\n' % listitem)
    filehandle = open("listfile.txt").read()
    open("listfile.txt", "w").close()
    return filehandle


def stopword1(text):
    marks = '''!()-[]{};?@#$%:'"\\,./^&;*_—≈1234567890»«…'''
    for c in marks:
        text = text.replace(c, '')
    nlp = spacy.load('ru_core_news_sm')
    my_doc = nlp(text)

    token_list = []
    for token in my_doc:
        token_list.append(token.text)

    filtered_sentence = []

    for word in token_list:
        lexeme = nlp.vocab[word]
        if not lexeme.is_stop:
            filtered_sentence.append(word)
    with open('listfile.txt', 'w') as filehandle:
        for listitem in filtered_sentence:
            filehandle.write('%s\n' % listitem)
    filehandle = open("listfile.txt").read()
    open("listfile.txt", "w").close()
    return filehandle


def fileopen(infile):
    infile = stopword(open('%s.txt' % infile, 'r').read())
    return infile


def document(text):
    text = fileopen(text)
    return text


# Creating a list of texts
bloblist = [
    document(st1),
    document(st2),
    document(st3),
    document(st4),
    document(st5),
    document(st6),
    document(st7),
    document(st8),
    document(st9),
    document(st10),
    document(st11),
    document(st12),
    document(st13),
    document(st14),
    document(st15),
    document(st16),
    document(st17),
    document(st18),
    document(st19),
    document(st20),
    document(st21),
    document(st22),
    document(st23),
    document(st24),
    document(st25),
    document(st26),
    document(st27),
    document(st28),
    document(st29),
    document(st30)]


fout = open("output.txt", "w")
tfIdfVectorizer = TfidfVectorizer(use_idf=True)
tfIdfVectorizer.fit(bloblist)
tfIdf = tfIdfVectorizer.transform([bloblist[0]])
df = pd.DataFrame(
    tfIdf.T.todense(),
    index=tfIdfVectorizer.get_feature_names_out(),
    columns=["TF-IDF"])
df = df.sort_values('TF-IDF', ascending=False)
df = df[(df > 0).all(axis=1)]
print(list(df.index), file=fout)

n = open("nouns.txt", "w")  # removing parts of speech
infile = stopword(open("output.txt", "r").read())
infile = re.sub("[^\\w]", " ", infile).split()
words = infile
morph = MorphAnalyzer()
items = [(str(morph.parse(w)[0].tag.POS), w) for w in words]
for word, score in items[:]:
    if word == 'NOUN':
        print((score), file=n)

a = open("adjf.txt", "w")
for word, score in items[:]:
    if word == 'ADJF':
        print((score), file=a)

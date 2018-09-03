#import for synonyms and antonyms
from nltk import word_tokenize
from nltk.corpus import wordnet
from nltk.corpus import words
from nltk.tokenize import sent_tokenize, word_tokenize

#import for bag of word
import numpy as np
#For the regular expression
import re

#import for word processing
import textblob
from textblob import TextBlob
from textblob import Word ,WordList
# from textblob import wordnet

#set to string 
from ast import literal_eval
#From src dependency 
from sentencecounter import no_sentences,getline

import os
def getsysets(word):
    syns = wordnet.synsets(word)  #wordnet from ntlk.corpus  will not work with textblob
    #print(syns[0].name()) 
    #print(syns[0].lemmas()[0].name())  #get synsets names 
    #print(syns[0].definition())  #defination 
    #print(syns[0].examples())    #example


# getsysets("good")


def getsynonyms(word):
    synonyms = []
    # antonyms = []
 
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
            # if l.antonyms():
            #     antonyms.append(l.antonyms()[0].name())
 
    #print(set(synonyms))
    return(set(synonyms))
    # print(set(antonyms))


# getsynonyms_and_antonyms("good")


def extract_words(sentence):
    ignore_words = ['a']
    words = re.sub("[^\w]", " ",  sentence).split() #nltk.word_tokenize(sentence)
    words_cleaned = [w.lower() for w in words if w not in ignore_words]
    return words_cleaned    


def tokenize_sentences(sentences):
    words = []
    for sentence in sentences:
        w = extract_words(sentence)
        words.extend(w)
        
    words = sorted(list(set(words)))
    return words

def bagofwords(sentence, words):
    sentence_words = extract_words(sentence)
    # frequency word count
    bag = np.zeros(len(words))
    for sw in sentence_words:
        for i,word in enumerate(words):
            if word == sw: 
                bag[i] += 1
                
    return np.array(bag)

def tokenizer(sentences):
    token = word_tokenize(sentences)
    print (sent_tokenize(sentences))
    print (token)

# sentences = "Machine learning is great","Natural Language Processing is a complex field","Natural Language Processing is used in machine learning"
# vocabulary = tokenize_sentences(sentences)
# print (vocabulary)
# tokenizer(sentences)

def createposfile(filename,word):
    # filename = input("Enter destination file name in string format :")
    f = open(filename,'w')
    f.writelines(word)

def createnegfile(filename,word):
    # filename = input("Enter destination file name in string format :")
    f = open(filename,'w')
    f.writelines(word)


def searchword(word, sourcename,destinationfile):
    if word in open(+sourcename).read():
            createposfile(destinationfile,word)
    elif word in open(-sourcename).read():
            createposfile(destinationfile,word)     

    else:
        synonyms = getsynonyms(word)
        checksynonyms= set(literal_eval(synonyms))
        searchword(checksynonyms,sourcename,destinationfile)

# getsynonyms("good")

for word in getline():
    searchword(word,'a.txt','b.txt')

searchword("good","a.txt","bbbbbb.txt")
def paragraph(sourcefile):
    f = open(sourcefile,'r')
    readlines = f.readlines()
    print (readlines)


# searchword('a','a.txt','bb.txt')


#for sentence processing

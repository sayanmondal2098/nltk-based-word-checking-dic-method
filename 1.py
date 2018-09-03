import re
import textblob
import os
import sys

from textblob import TextBlob
from textblob import Word
from sentencecounter import no_sentences


number_of_sentence = print (no_sentences())



paragraph = "ITP is a two-year graduate program located in the Tisch School of the Arts.  Perhaps the best way to describe us is as a Center for the Recently Possible."
blob = TextBlob(paragraph)




#  for np in blob.noun_phrases:
#      print (np)

# for noun , pos in blob.pos_tags:
#      print (noun, pos);


## FIND ALL ASSOCIATED WORD


# print (bank.synsets)
# for sentencs in 

# for word in blob.sentences[0].words:
#     a = (Word(word)).synsets
#     print ((word) ,a )

for i in range(no_sentences()):
    for word in blob.sentences[i].words:
        a = (Word(word)).synsets
        print ((word) ,a )
#     #  bank = word

# synsets = Word("bank").synsets
# for synset in synsets:
#     print (synset.defination())



import naturalprocessingwordnet
import re
from sentencecounter import gettempwords,getallline,getline

print ("## IT'S STARTING OF ONLYFILE READWRITE SCRIPT ##")
def createnegfile(filename,word):
    # filename = input("Enter destination file name in string format :")
    f = open(filename,'a')
    f.writelines(word +"\n")

def searchword(word, sourcename):
    if word in open('list of negative words.txt').read():
            createnegfile('destinationnegfile.txt',word)
    elif word in open('list of positive words.txt').read():
            createnegfile('destinationposfile.txt',word)  
print (gettempwords())
print (gettempwords().__format__)
print (gettempwords().__getitem__)
print (len(gettempwords()))
for i in range(0,(len(gettempwords()))):
    print (gettempwords()[i])


print ("Ent of For loop")
#print the word in sorted words
print (sorted(gettempwords()))

#print the array size
print(gettempwords().__sizeof__())
print ("the 2nd word is :"+ gettempwords()[0])
# # words = ['abort','aborted','abnormal','abound','abundant','accessable']

# for word in gettempwords():
#     searchword(word,'a.txt')



   
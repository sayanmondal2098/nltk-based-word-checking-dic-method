import naturalprocessingwordnet
from sentencecounter import gettempwords,filename,getline

def createnegfile(filename,word):
    # filename = input("Enter destination file name in string format :")
    f = open(filename,'a')
    f.writelines(word +"\n")



def searchwordneg(word, sourcename):
        if word in open('list of negative words.txt').read():
                createnegfile('destinationnegfile.txt',word)
        else:
                for item in naturalprocessingwordnet.getsynonyms(word):
                        if item in open('list of negative words.txt').read():
                                createnegfile('destinationnegfile.txt', word)

def searchwordpos(word, sourcename):
        if word in open('list of positive words.txt').read():
                createnegfile('destinationposfile.txt',word) 
        else:
                for item in naturalprocessingwordnet.getsynonyms(word):
                        if item in open('list of positive words.txt').read():
                                createnegfile('destinationposfile.txt', word) 



for word in gettempwords():
    searchwordneg(word, filename)
    searchwordpos(word, filename)
print('*'*50)
for i in range(0,(gettempwords().__len__())):
    searchwordneg(sorted(gettempwords())[i],filename)
    searchwordpos(sorted(gettempwords())[i],filename)



# print('*'*50)
# for i in range(0,5):
#     print(sorted(gettempwords())[i])
   

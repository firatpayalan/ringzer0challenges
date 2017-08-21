'''
simple caesar decryption
caesar encryption based on rotating operation.
function use n and encryptedText parameter.
n means rotation index, encryptedText is simple caesar encrypted text
decryption formula is
D(x) = (x - n) % 26
26 is the number of letters in british alphabet
x is a encryptedText
n is a rotation value.
Created on 21 Agu 2017
@author: FIRAT
'''
import string
letters = string.ascii_letters
def caesar_decryption(n,encryptedText):
    predictedText=''
    lengthOfEncryptedText = len(encryptedText)
    for index,letter in enumerate(encryptedText):
        currentIndex = letters.index(letter)
        predictedIndex = (currentIndex - n) % 26
        predictedLetter = letters[predictedIndex]
        predictedText = predictedText+predictedLetter
    return predictedText

for i in range(26):
    print('CASE = '+str(i))
    print(caesar_decryption(i,'SYNTPrfneVfPbbyOhgAbgFrpher'))
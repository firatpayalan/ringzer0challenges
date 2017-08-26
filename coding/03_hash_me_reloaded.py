'''
Created on 26 Aðu 2017

@author: FIRAT
'''
import hashlib
import httplib2
import time
import binascii
#SHA512 encryption
def encryptSHA512(value):
    s = hashlib.sha512(value.encode())
    return s.hexdigest()


# used httplib2 module in python environment.
# pip install httplib2
# https://pypi.python.org/pypi/httplib2/0.7.2
http = httplib2.Http()
# setting session cookie
headers = {'Cookie':'PHPSESSID=lmtskujia0uacdl7dh1atqfeu4'}

# challenge requires submittion within 2 seconds.
# 'time' module is used for this objective
start = int(round(time.time() * 1000))
response,content = http.request("https://ringzer0team.com/challenges/14","GET",headers=headers);
print(content)

# bit string size is 8192. bitArray function makes string slicing per bytes.
bitArray = lambda x, n: [x[i:i+n] for i in range(0, len(x), n)]
#decimalValueArray is converting ascii code of each byte
decimalValueArray = lambda x: [int(x[i],base=2) for i in range(0,len(x))]
#ascii codes are converted to character value and added to list.
encodedString = lambda x: [''.join(chr(x[i])) for i in range(0,len(x))]



# 'split' and 'replace' methods are suitable to extract 'message'
toBeHashed = str(content).split("<hr />")[1].split("<div class=")[2].split("<br />")[1].replace("\\r\\n\\t\\t","")
binaryArray = bitArray(toBeHashed,8)
decArray = decimalValueArray(binaryArray)
#list -> string conversion
#message has converted to string value and ready to be encrypted.
preparedForHash = ''.join(encodedString(decArray))
hashedTo512 = encryptSHA512(preparedForHash)


response,content = http.request("https://ringzer0team.com/challenges/14/"+hashedTo512,"POST",headers=headers)

# content is important. Page will be returning a FLAG-* value within a div element. Obtain from 'content' and submit it bottom left of the page.
#<div class="alert alert-info">FLAG-*</div>
print(content)
end = int(round(time.time() * 1000))
print(end-start)
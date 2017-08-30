'''
Created on 31 Agu 2017

@author: euphratesy
'''
import httplib2
import time

http = httplib2.Http()
#just for session connection
headers = {'Cookie':'PHPSESSID=79mjdjul8ornam9mosa7umpva4'}
#this is the site that decode SHA1 encoded hashing text
decodeLink = "http://hashtoolkit.com/reverse-hash?hash="
start = int(round(time.time() * 1000))
#request for hashed text
response,content = http.request("https://ringzer0team.com/challenges/56","GET",headers=headers);
#print(content)
#string operation to extract hashed text
hashedText = str(content).split("<div class=\"message\">")[1].split("<br />")[1].replace("\\r\\n\\t\\t","");
#print("HASHED TEXT = "+hashedText)
#for decoding
response,content = http.request(decodeLink+hashedText,"GET",headers=headers);
#extract decoded information from site
decodedValue=str(content).split("<code>")[2].split("</code>")[0]
print(decodedValue)
#obtain flag :)
response,content = http.request("https://ringzer0team.com/challenges/56/"+decodedValue,"GET",headers=headers);
end = int(round(time.time() * 1000))
print(content)
#measurement in ms
print(end-start)

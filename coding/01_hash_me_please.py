#euphratesy - 20.08.2017 14:38
import hashlib
import httplib2
import time
#SHA512 encryption
def encryptSHA512(value):
    s = hashlib.sha512(value.encode())
    return s.hexdigest()


# used httplib2 module in python environment.
# pip install httplib2
# https://pypi.python.org/pypi/httplib2/0.7.2
http = httplib2.Http()
# setting session cookie
headers = {'Cookie':'PHPSESSID=jujb8hibk6ederfu172njrcc70'}

# challenge requires submittion within 2 seconds.
# 'time' module is used for this objective
start = int(round(time.time() * 1000))
response,content = http.request("https://ringzer0team.com/challenges/13","GET",headers=headers);
# 'split' and 'replace' methods are suitable to extract 'message'
toBeHashed = str(content).split("<hr />")[1].split("<div class=")[2].split("<br />")[1].replace("\\r\\n\\t\\t","")
hashedTo512 = encryptSHA512(toBeHashed)

response,content = http.request("https://ringzer0team.com/challenges/13/"+hashedTo512,"GET",headers=headers)

# content is important. Page will be returning a FLAG-* value within a div element. Obtain from 'content' and submit it bottom left of the page.
#<div class="alert alert-info">FLAG-*</div>
#print(content)
end = int(round(time.time() * 1000))
# print(end-start)
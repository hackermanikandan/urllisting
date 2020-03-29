import requests

site = input("Enter youer site name > ")

mylist = open('wordlist.txt','r+')

try:

    for x in mylist:
    
        x = x.strip()

        r = requests.get('http://'+site+'/'+x)

        if r.ok:
            print('http://'+site+'/'+x)
except:
    exit()

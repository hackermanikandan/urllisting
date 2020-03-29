import requests

site = input("Enter youer site name > ")

new = open('urls.txt','w')

mylist = open('wordlist.txt','r+')

try:

    for x in mylist:
    
        x = x.strip()

        r = requests.get('http://'+site+'/'+x)

        if r.ok:
            
            print('http://'+site+'/'+x)
            
            new.write('http://'+site+'/'+x+'\n')
            
except KeyboardInterrupt:
    
    exit()

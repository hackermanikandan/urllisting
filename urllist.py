import requests
domain = raw_input("Enter youer domain name > ")
out_file = open('urls.txt','w')
wordlist = open('wordlist.txt','r+')
for one_line in wordlist:
    one_line = one_line.strip()
    domain_name = ('http://{}/{}'.format(domain,one_line))
    try:
        req = requests.get(domain_name,timeout=1)
        if req.ok:
            print('[+] 200 :'+req.url)
            out_file.write(req.url+'\n')
        else:
            print('[-] 404 :'+domain_name)
    except KeyboardInterrupt:
        exit()
    except requests.exceptions.Timeout: 
        print("[-] Domain timeout! ({})".format(req.url))
    except requests.exceptions.TooManyRedirects:
        print("[-] Domain has too many redirects! ({})".format(req.url))
    except requests.exceptions.ConnectionError:
        print("[-] Domain Connection Error! ({})".format(req.url))

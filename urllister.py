import requests
import sys


banner = """
            _ _ _     _            
 _   _ _ __| | (_)___| |_ ___ _ __ 
| | | | '__| | | / __| __/ _ \ '__|
| |_| | |  | | | \__ \ ||  __/ |   
 \__,_|_|  |_|_|_|___/\__\___|_|   
                                   
                          by mr.prohack
"""
using = "urllister.py [dir or dns] [domain name] [wordlist]\nex: urllister.py dir google.com wordlist.txt"

if len(sys.argv) <= 1:   
    print(banner)
    print(using)
    exit()

def request(domain_name):
    try:
        #host_ip = socket.gethostbyname(domain_name)
        req = requests.get(domain_name,timeout=2)
        if req.ok:
            print('[+] 200 :'+req.url)
            out_file.write(req.url+'\n')
        else:
            print('[-] 404 :'+domain_name)
    except KeyboardInterrupt:
        exit()
    except requests.exceptions.Timeout: 
        print("[-] Domain request timeout! :{}".format(domain_name))
    except requests.exceptions.TooManyRedirects:
        print("[-] Domain has too many redirects! :{}".format(domain_name))
    except requests.exceptions.ConnectionError:
        print("[-] Domain Connection Error! :{}".format(domain_name))

def url(wordlist,domain):
    for one_line in wordlist:
                one_line = one_line.strip()
                domain_name = ('http://{}/{}'.format(domain,one_line))
                request(domain_name)
def domainlist(wordlist,domain):
    for one_line in wordlist:
                one_line = one_line.strip()
                domain_name = ('http://{}.{}'.format(one_line,domain))
                request(domain_name)
                print(new)

def main():
    print(banner)
    domain = sys.argv[2]  
    out_file = open('urls.txt','w')
    try:
        if len(sys.argv[3]) != None:
            word = sys.argv[3]
    except:
        word = 'wordlist.txt'
        print('use default wordlist\n')
    wordlist = open(word,'r+')
    if sys.argv[1] == 'dir':
        url(wordlist,domain)
    elif sys.argv[1] == 'dns':
        domainlist(wordlist,domain)
    else:
        print(using)


if __name__ == "__main__":
    main()

import requests
import sys
import socket


banner = """
            _ _ _     _            
 _   _ _ __| | (_)___| |_ ___ _ __ 
| | | | '__| | | / __| __/ _ \ '__|
| |_| | |  | | | \__ \ ||  __/ |   
 \__,_|_|  |_|_|_|___/\__\___|_|   
                                   
                          by mr.prohack
"""
using = "urllister.py [dir or dns or dnsip] [domain name] [wordlist]\nex: urllister.py dir google.com wordlist.txt"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) <= 1:   
    print(banner)
    print(using)
    exit()

def request(domain_name,out_file):
    try:
        req = requests.get(domain_name,timeout=2)
        if req.ok:
            if sys.argv[1] == 'dnsip':
                url1 = ((req.url).find("//"))
                url1 = (req.url[url1+2:])
                url2 = url1.find('/')
                domain = (url1[:url2])
                host_ip = socket.gethostbyname(domain)
                print('[+] 200 :'+req.url+'  ip :'+host_ip)
                out_file.write(req.url+'       ip :'+host_ip+'\n')
            else:
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

def url(wordlist,domain,out_file):
    for one_line in wordlist:
                one_line = one_line.strip()
                domain_name = ('http://{}/{}'.format(domain,one_line))
                request(domain_name,out_file)

def domainlist(wordlist,domain,out_file):
    for one_line in wordlist:
                one_line = one_line.strip()
                domain_name = ('http://{}.{}'.format(one_line,domain))
                request(domain_name,out_file)

def dnsip(wordlist,domain,out_file):
    domainlist(wordlist,domain,out_file)


def main():
    print(banner)
    try:
        domain = sys.argv[2]  
    except IndexError:
        print('input files mising')
    out_file = open('live_urls.txt','w')
    try:
        if len(sys.argv[3]) != None:
            word = sys.argv[3]
    except:
        word = 'wordlist.txt'
    try: 
        if sys.argv[2] == None:   
            print('use default wordlist\n')
        wordlist = open(word,'r+')
        if sys.argv[1] == 'dir':
            url(wordlist,domain,out_file)
        elif sys.argv[1] == 'dns':
            domainlist(wordlist,domain,out_file)
        elif sys.argv[1] == 'dnsip':
            dnsip(wordlist,domain,out_file)
        else:
            print(using)
    except:
        exit()

if __name__ == "__main__":
    main()

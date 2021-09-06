import requests
from requests.exceptions import ConnectionError

try:
    request = requests.get('http://pudim.com.br/')
except ConnectionError:
     print("\033[0;30;41m Erro!! Web site NÂO está online\033[0m")  
     print ()
else:
    print("\033[0;30;42m Web site está online\033[0m")
    
##########################          
#o mesmo exercicio em modo Guanabara
import urllib
import urllib.request

try:
    site=urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print("\033[0;30;41m Erro!! Web site NÂO está online\033[0m")  
else:
    print("\033[0;30;42m Web site está online\033[0m")
    print (site.read())                                     #ler o código do site inteiro


    

lista2 = []
for i in range(2):
	lista2.append([])
	for j in range(3):
		lista2[i].append(0)	
print (lista2)
from time import sleep
sleep(2)   
print("hello world")
import socket
import os


client = socket.socket()
ip = input('IP: ').strip()
porta = int(input('Digite uma porta: '))
client.settimeout(0.5)
codigo_das_conexoes = client.connect_ex((ip, porta))
# banner = client.recv(1024)  # 1024 bytes
if codigo_das_conexoes == 0:
    dicionario = dict()
    dicionario['Ip'] = ip
    dicionario['Porta aberta'] = porta
    # dicionario['Nome do serviço'] = banner
    logs = open('logs.txt', 'a')
    logs.write(str(dicionario))
    logs.write('\n')
    logs.close()
else:
    print(f'Porta {porta} fechada.')

print('[!] Script finalizado. Digite qualquer  tecla para fechar a janela.')
os.system('pause')

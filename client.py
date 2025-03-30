from socket  import *
from constCS import * 

while True:
    conta = str(input('digite uma equação de soma, subtração, multiplicação ou divisão a ser realizada ou digite sair para parar o programa'))
    if conta == 'sair':
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((HOST, PORT)) # connect to server (block until accepted)
        s.send(str.encode(conta)) # send equation to be solved by the server
        data = s.recv(1024)     # receive the response
        print (bytes.decode(data))            # print the result
        s.close()               # close the connection
        break

    else:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((HOST, PORT)) # connect to server (block until accepted)
        s.send(str.encode(conta)) # send equation to be solved by the server
        data = s.recv(1024)     # receive the response
        print (bytes.decode(data))            # print the result
        s.close()               # close the connection

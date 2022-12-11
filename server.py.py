import threading
import socket
host='127.0.0.1'
port=99999
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients=[]
nicknames=[]



#sending message to everyone function
def broadcast(message):
    for client in clients:
        client.send(message)


#handling connection
def handle(client):
    while True:
        try:
            message=client.recv(1024)
            broadcast(message)
        except:
            
            
        
           index = clients.index(client)
           clients.remove(client)
           client.close()
           nickname=nicknames[index]
           broadcast(f'{nickname} left the chat!'.encode('ascii'))
           nicknames.remove(nickname)
           break

#getting client object and address
def receive():
    while True:
        client,address=server.accept()
        print(f'connected with {address}')

        client.send('NICK'.encode('ascii'))
        nickname=client.recv(1024).decode(('ascii'))
        nicknames.append(nickname)
        clients.append(client)

        print(f'nickname of the client is {nickname}')
        broadcast(f'{nickname}joined the chat!'.encode('ascii'))
        client.send('connected to the server'.encode('ascii'))

        #threading
        threat=threading.Thread(target=handle, args=(client,))
        thread.start()
receive()








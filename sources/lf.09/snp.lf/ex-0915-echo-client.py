# (C) 2025 K.Reincke: proTirone snippet [CC-BY-4.0]
# in broad terms inspired by https://realpython.com/python-sockets/

import socket, time

server_address = "127.0.0.1"  # echo server's hostname or IP address
server_port = 65432           # port used by the echo server
client_message="Hello, world"
delay = 10 # interuption for reviweing the server status

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"calling for a socket with dynamic client port")
    time.sleep(delay)
    s.connect((server_address, server_port))
    print(f"got a socket")
    time.sleep(delay)
    print(f"sending {client_message} to {server_address}:{server_port}")
    #s.sendall(b"Hello, world")
    s.sendall(client_message.encode(encoding="utf-8"))
    time.sleep(delay)
    data = s.recv(1024)

print(f"Received back: {data!r}")
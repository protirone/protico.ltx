# (C) 2025 K.Reincke: proTirone snippet [CC-BY-4.0]
# in broad terms following https://realpython.com/python-sockets/

import socket

server_address = "127.0.0.1"  # echo server's hostname or IP address
server_port = 65432  # port used by the echo server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((server_address, server_port))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received back: {data!r}")
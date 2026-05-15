# (C) 2025 K.Reincke: proTirone snippet [CC-BY-4.0]
# in broad terms inspired by https://realpython.com/python-sockets/

import socket, time

server_address = "127.0.0.1"  # echo server's hostname or IP address
server_port = 65432           # port used by the echo server
zzz = 10                    # sleeping time for reviewing tcp status

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  print(f"calling for a dynamic socket with port"); time.sleep(zzz)
  s.connect((server_address, server_port))
  print(f"got a socket"); time.sleep(zzz)
  
  print(f"sending 'Hello Server' to {server_address}:{server_port}")
  s.sendall(b"Hello Server"); time.sleep(zzz)
  data = s.recv(1024)

print(f"Received back: {data!r}")
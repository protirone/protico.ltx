# (C) 2025 K.Reincke: proTirone snippet [CC-BY-4.0]
# in broad terms following https://realpython.com/python-sockets/
import socket

server_addr = "127.0.0.1"  # loopback interface address (localhost)
# wkp: 0 - 1023 | rp: 1024 - 49151 | dp: 49152 – 65535 | wkp echo: 7
server_port = 65432 # better using a 'handcrafted' dynamic port ;-)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((server_addr, server_port))
  s.listen()
  print(f"acting on/for {server_addr}:{server_port}")
  while True:                      
    conn, addr = s.accept()        # waiting for next request
    print(f"requested by {addr}")
    while True:
      data = conn.recv(1024)
      if not data: break
      conn.sendall(data)
    print(f"served response")
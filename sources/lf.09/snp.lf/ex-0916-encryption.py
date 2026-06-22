# (C) 2025 K.Reincke: proTirone snippet [CC-BY-4.0]
msg="Der Teufel trägt Prada";key=75
key=123

def crypt(bar,key):
  cft=bytearray();i=0
  while i<len(bar):cft.append(bar[i]^key);i+=1
  return cft

def print_hex_array(bar):
  i=0
  while i<len(bar):print(f"{hex(bar[i])}",end="");i+=1
  print("")

cfr=crypt(bytearray(msg,'utf-8'),key) # string 2 bytearry
decfr=crypt(cfr,key).decode() # bytearry 2 string

print(f"recieved:/{msg}/")
print("encoded:",end="");print_hex_array(cfr)
print(f"encoded:/{cfr}/")
print(f"decoded:/{decfr}/")
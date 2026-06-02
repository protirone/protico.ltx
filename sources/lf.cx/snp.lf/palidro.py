# (C) 2025 K.Reincke: proTirone snippet [CC-BY-4.0]



def diy(string,char):
    return f"{char}{string}{char}"

print(diy(diy("",'b'),'a'))


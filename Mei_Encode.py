
from base64 import b32encode

# chat command
# !dec b32: 


#lm = "Thems the facts"
lm = input("insert text:")
m = lm.__hash__()

# print(m)

p = b32encode(lm.encode())
print("!dec b32:"+str(p).replace("b","").replace("'",""))

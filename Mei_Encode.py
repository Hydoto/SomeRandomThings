
from base64 import b64encode


# stream: www.twitch.tv/meisaka
# chat command
# !dec b64: 



#lm = "Thems the facts"
lm = input("insert text:")
m = lm.__hash__()

# print(m)

p = b64encode(lm.encode())
print("!dec b64:"+str(p).replace("b","").replace("'",""))

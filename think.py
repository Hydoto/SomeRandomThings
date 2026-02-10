from math import ceil
from random import randint

meep = randint(0,8888888)
meep = meep / 8.4
lo = ceil(meep + 10000.6050)
print("hello world ",lo)

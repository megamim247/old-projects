from random import randint as rnt
while True:
    rtn=str(bin(rnt(10**1199,10**20)))
    rtn=rtn.split('b')
    print(rtn[1])

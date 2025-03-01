from pwn import *
r=remote("mercury.picoctf.net",20266)
print(data , sep="\n")
KEY_LEN = 50000
chunkmax=5000
c= unhex("5b1e564b6e415c0e394e0401384b08553a4e5c597b6d4a5c5a684d50013d6e4b")
count=KEY_LEN-len(c)
with log.progress('Causing wrap-around') as p:
    while count > 0:
        p.status(f"{count} bytes left")
        chunk_size = min(chunkmax, count)
        r.sendlineafter("What data would you like to encrypt? ", "a" * chunk_size)
        
        count -= chunk_size
r.sendlineafter("What data would you like to encrypt? ",c)
recvc=r.recvlinesS(2)
print(unhex(recvc[1]))

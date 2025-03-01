c= "5b1e564b6e415c0e394e0401384b08553a4e5c597b6d4a5c5a684d50013d6e4b"
def list2(original):
    new=[]
    original=list(original)
    x=""
    for n in range(0,len(original),2):
        x=""
        x+=original[n]
        x+=original[n+1]
        new.append(x)
    return new
#num of key = limited
data=list("11111111111111111111111111111111")
cipher="6d490657516d4954096d495250046d4952576d4957086d4908506d4909056d49"
cipher=list2(cipher)
k=list(map(lambda p,r: "{:02x}".format(int(r,16)^int(p,16)),data, cipher))
print("".join(k))
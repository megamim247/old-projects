ui="pico"
key=[60,2,3,4]
print(list(map(lambda p, k: "{}".format(ord(p) ^ k), list(ui), key)))
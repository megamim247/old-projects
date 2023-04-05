import unicodedata 
 
print(f'Unicode version {unicodedata.unidata_version}') 
 
exclude = frozenset(['Cn', 'Co', 'Cs']) 
 
for cp in range(0x110000): 
    category = unicodedata.category(chr(cp)) 
    if category in exclude: 
        continue 
    print(f'{cp:04X}\t{category}')

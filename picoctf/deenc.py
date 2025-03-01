flag="灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ"
flag2="pcCF1_isis3do__68c0"


print(''.join([''.join(chr(ord(flag[i])>>8)+\
                       chr(int(ord(flag[i])\
                               -(int(ord(flag[i])>>8)<<8)\
                           )\
                            ) for i in range(0, len(flag), 1))]))

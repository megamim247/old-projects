#setup:
import os
renthn=False
list2=[]
def writfil(x):
    with open('!uneditable.py','a')as file:
        for n in x:
            file.write(n+'\n')
def getpseud():
    list1=[]
    with open(filename) as file:
        for line in file:
            a1=line.rsplit('\n')
            list1.append(a1[0])
    return list1
def listjoin(list0):
    x=''
    n2=-1
    for n in list0:
        n2=n2+1
        x+=list0[n2]
    return x
#main:
filename=str(input('filename:'))
list1=getpseud()
for nx2 in list1:
    print(nx2)
print('\n\n')
for n in list1:
    #clean:
    indnum=0
    n=n.replace('~', '=').replace('\t', '        ')
    if renthn==True:
        n=n.replace('then','')
        renthn=False
    n=n.rsplit(' ')
    while (n[0]==''):
        del  n[0]
        indnum=indnum+1
    #functions:
    #print:
    if n[0]=='print':
        del n[0]
        n='print('+listjoin(n)+')'
    if n[0]=='PRINT':
        n[0]=n[0].lower()
        n.append(n[1])
        n[1]='('
        n.append(')')
    #input:
    if n[0].lower()=='input':
        n=n[1]+'=input(\'input:\')'
    #conditionals:
    #if
    if n[0].lower()=='if':
        renthn=True
        n[0]='if '
        n.append(':')
    #loops:
    #for loop:
    if (n[0]=='for') and (len(n)==6):
        n='for '+n[1] +' in range('+str(n[3])+','+str(n[5].replace(':',''))+'):'
    elif (n[0]=='for') and (len(n)==5):
        n='for '+n[1].replace('=','') +' in range('+str(n[2].replace('=',''))+','+str(n[4].replace(':',''))+'):'
    if (n[0]=='FOR') and (len(n)==6):
        n='for '+n[1] +' in range('+str(n[3])+','+str(n[5].replace(':',''))+'):'
    elif (n[0]=='FOR') and (len(n)==5):
        n='for '+n[1].replace('=','') +' in range('+str(n[2].replace('=',''))+','+str(n[4].replace(':',''))+'):'
    #while loop:
    if n[0].lower()=='while':
        del n[0]
        n='while '+str(listjoin(n)).replace('do','').replace(':','').replace('DO','')+':'
    #indents:
    n=listjoin(n)
    n=n.replace('next','').replace('NEXT','').replace('ENDWHILE','').replace('endwhile','').replace('endif','').replace('ENDIF','')
    if indnum>3:
        for nx in range(indnum):
            n=' '+n
    #enter into list:
    list2.append(n)
for nx2 in list2:
    print(nx2)
writfil(list2)
os.system('!uneditable.py')

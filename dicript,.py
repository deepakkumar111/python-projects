f=open(r'C:\Users\Hp\Desktop\encript.txt','r')
e=''
d=f.read()
f.close()
for i in range(0,len(d)):
    if(d[i]==' '):
        e=e+(d[i])
    else:
        e=e+chr(ord(d[i])-1)
print(e)
f=open(r'C:\Users\Hp\Desktop\dcript.txt','w')
f.write(e)
f.close()

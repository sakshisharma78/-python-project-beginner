import random
st='abcdefghijklmnopqrstuvwxyz'
p='#@$&!?*'
c='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ls=[]
l=[]
lk=[]
for i in st:
    l.extend(i)
for j in p:
    ls.extend(j)
for k in c:
    lk.extend(k)
while(True):
    n=random.randrange(1111,9999)
    s=random.choice(l)
    v=random.choice(l)
    t=random.choice(ls)
    a=random.choice(lk)
    u=random.choice(lk)
    f=random.randrange(111,999)
    n=str(n)
    s=str(s)
    t=str(t)
    a=str(a)
    f=str(f)
    u=str(u)
    v=str(v)
    out=n+a+s+t+v+u+f
    print(out)
    input('please  click enter to the next passward') 

f = open ('text.txt', 'r')
k=0
m=0
a=[]
s=''
for i in f:
    if i!=' ':
        if i!=',' and i!='!' and i!='?' and i!='.' and i!=';' and i!=':' and i!='(' and i!=')':
            k+=1
    elif i==' ':
        m=i
        for j in range (m-k, m):
            #if j!=',' and j!='!' and j!='?' and j!='.' and j!=';' and j!=':' and j!='(' and j!=')' and j!='"': #можно добавить другие знаки препинания
                #s+=i
            if j==m-1:
                s.lower()
                a.append(s)
                s=0

f.close()
print(a)
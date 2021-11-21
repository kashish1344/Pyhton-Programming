a=0
for i in range(1,5):
    for j in range(10-i):
        print(' ',end='')
    for k in range(1,i+1):
        a+=1
        print(a,end=' ')
    print()

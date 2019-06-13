a = ['B','R','R','G','R','R','B']
i = 0
j = len(a)-1
k = len(a)-1

while i<k:
    if a[k]=='R':
        temp = a[k]
        a[k] = a[i]
        a[i] = temp
        i+=1
    elif a[k]=='G':
        k-=1
    elif a[k] == 'B':
        temp = a[k]
        a[k] = a[j]
        a[j] = temp
        k-=1
        j-=1

print(a)
 

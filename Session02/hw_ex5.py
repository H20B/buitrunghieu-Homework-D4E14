n = int(input('Nhap n: '))
mul =1
for i in range(1,n+1):
    for j in range(1,n+1):
         mul = i*j
         print(mul, end = '\t')
    print() 
    
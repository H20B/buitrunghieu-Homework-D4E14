n = int(input('Nhap n: '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i+j) % 2 == 0:
            print('1', end = ' ')
        else:
            print('0', end = ' ')
    print()            
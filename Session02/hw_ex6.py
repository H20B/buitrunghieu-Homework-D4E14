for i in range(1,11):
    for j in range(1,11):
        if (j+i) % 2 == 0:
            print('1', end=' ')
        else:
            print('0',end=' ') 
    print()    

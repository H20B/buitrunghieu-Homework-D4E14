size_sheep = [5, 7 , 300, 90, 24, 50, 75]
num=1
print(f'Hello my name is Hieu and these are my sheep sizes \n{size_sheep} \n')
while num <= 3 :

# Kích thước cừu tăng sau 1 tháng
    print(f'Month {num} ')
    for i in range(len(size_sheep)):
        size_sheep[i] += 50
    print(f'One month has passed, now is here my flock \n{size_sheep}') 
# Tìm kiếm con cừu lớn nhất
    print(f"Now my biggest sheep has size {max(size_sheep)} let's shear it ")
# Đưa về mặc định là 8 sau khi bỏ số lớn nhất
    id = size_sheep.index(max(size_sheep))   
    size_sheep[id] = 8
    print(f'After shearing, here is my flock \n{size_sheep} \n')
    num += 1

        


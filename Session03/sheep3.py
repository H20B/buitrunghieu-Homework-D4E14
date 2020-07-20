size_sheep = [5, 7 , 300, 90, 24, 50, 75]
num=1
print(f'Hello my name is Hieu and these are my sheep sizes \n{size_sheep} \n')

def find_maxsize(): 
    print(f"Now my biggest sheep has size {max(size_sheep)} let's shear it ")
def return_defaultsize():
    id = size_sheep.index(max(size_sheep))   
    size_sheep[id] = 8
    print(f'After shearing, here is my flock \n{size_sheep} \n')
def grow_sheep():
    for i in range(len(size_sheep)):
        size_sheep[i] += 50    
    print(f'One month has passed, now is here my flock \n{size_sheep}') 

while num < 3:
    print(f'Month {num}')
    grow_sheep()
    find_maxsize()
    return_defaultsize()
    num += 1
print('Month 3')
grow_sheep()
sUm = sum(size_sheep)
print('My flock has size in total: ', sUm)
new_sUm = sUm * 2
print(f"I would get {sUm} * 2 $ = {new_sUm} $   ")


from random import shuffle
word = 'lovingyou'
list_w = list(word)
shuffle(list_w)
for i in range(len(list_w)):
    print(list_w[i], end =' ' )
answer = input('\nYour answer: ')
if answer == word:
    print('Hura') 
else:
    print(':(')       
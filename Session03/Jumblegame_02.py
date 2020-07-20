import random
from random import shuffle
list_word = ['love', 'like', 'hate']
word = random.choice(list_word)
word1 = list(word)
shuffle(word1)
for i in range(len(word1)):
    print(word1[i], end =' ' )
answer = input('\nYour answer: ')
if answer == word:
    print('Hura') 
else:
    print(':(')         





#print('Hello world')
#print('hello again')
import random,os,sys
num = random.randint(0,9)
clear = lambda: os.system('cls')
x = int(input('enter any number from 0 to 9'))
clear()
if x == num:
    print('you guessed the correct number',x)
else :
    print('better luck next time')

clear()
s = input('do you want to play again \ntype yes or no')
if s == 'yes' :
    os.system('practise 1.py')
elif s == 'no' :
    exit()


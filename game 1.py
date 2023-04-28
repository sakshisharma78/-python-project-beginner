while(True):
    import random
    n=input("enter your name")
    b=input('enter your choice')
    ls=['rock','papar','scissor']
    c=random.choice(ls)
    if ((c=='scissor' and b=='papar')or(c=='rock'and b=='scissor')or(c=='papar'and b=='rock')):
        print('computer win the game!')
    elif ((c=='papar' and b=='scissor') or (c=='scissor' and b=='rock') or (c=='rock' and b== 'papar')):
        print (n,'win the game!')
    else:
        print('match is withdraw')
    print('you wants to play again??')
    w=input()
    if w=='no':
        break
print('thank you, have a good day!')
 
        
        

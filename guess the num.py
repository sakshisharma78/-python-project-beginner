while(True):
    print('enter the level you want to play')
    print('easy')
    print('intermediate')
    print('hard')
    a=input('enter the level')
    if a=='easy':
        import random
        rd=random.randrange(1,20)
        n=input('enter your name')
        while(True):
            num=int(input("guess the num"))
            if num>rd:
                print("too large")
            elif num<rd:
                print("too small")
            elif num==rd:
                print("right")
           
                print(n,'you win the game')
                break
        else:
             print("you loose the game!")
        print('you want to play again')
        w=input()
        if w=='no':
            break
    elif a=='intermediate':
        import random
        c=10
        rd=random.randrange(1,50)
        n=input('enter your name')
        while(c):
            num=int(input("guess the num"))
            if num>rd:
                print("too large")
            elif num<rd:
                print("too small")
            elif num==rd:
                print("right")
           
                print(n,'you win the game')
                break
            c-=1
        else:
            print("you loose the game!")
            print('you want to play again')
            w=input()
            if w=='no':
               break
         
    elif a=='hard':
        import random
        c=4
        rd=random.randrange(1,100)
        n=input('enter your name')
        while(c):
            num=int(input("guess the num"))
            if num>rd:
                print("too large")
            elif num<rd:
                print("too small")
            elif num==rd:
                print("right")
           
                print(n,'you win the game')
                break
            c-=1
        else:
            print("you loose the game!")
            print('you want to play again')
            w=input()
            if w=='no':
               break
          
print('thank you,have a good day !')
         

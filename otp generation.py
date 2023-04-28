import random
n=int(input('enter your width of otp'))
val=random.random()
otp=str(val)[-n:]
print(otp)

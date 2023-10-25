import random

com = random.randint(1,3)
user = int(input('1 : 가위, 2 : 바위, 3 : 보'))

if com == 1 :
    com='가위'
elif com == 2 :
    com = '바위'
else :
    com ='보'

if user == 1 :
    user = '가위'
elif user == 2 :
    user = '바위'
else :
    user = '보'

print('com(%s) : user(%s)' %(com, user))

if com == user :
    print('Draw')
elif com == '바위' and user == '가위' :
    print('Com Wins!')
elif com == '가위' and user == '바위' :
    print('User Wins!')
elif com == '보' and user == '가위' :
    print('User Wins!')
elif com == '가위' and user == '보' :
    print('Com Wins!')
elif com == '바위' and user == '보' :
    print('User Wins!')
else :
    print('Com WIns!')
    
        

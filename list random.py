from random import *
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = (choices(a, [2, 2, 2, 2, 2, 2, 1, 2, 2, 2], k= 3))
print(b)
if b[0] == 7 and b[1]== 7 and b[2]== 7 :
    print('Lucky!')

elif b.count(7) == 2 :
    print('Good')

else :
    print('So so')
    

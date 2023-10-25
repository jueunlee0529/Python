##import random
##
##com = random.randint(1,2)
##user = int(input('odd : 1, even : 2\n'))
##
##print('COM(%d) : USER(%d)' % (com, user))
##if com == user :
##    print('CORRECT')
##else :
##    print('INCORRECT')

import random

com = random.randint(1,2)
user = int(input('odd : 1, even : 2\n'))
if user == 1 :
        user = 'odd'
else :
        user = 'even'
if com = 1 :
        com = 'odd'
else :
        com = 'even' 
print('com(%s) : user(%s)' %(com, user))

if com == user :
        print('Correct')
else :
    print('Incorrect')

cnt = 0
n = int(input("정수 입력 :  "))
while n > 0 :
    cnt += 1
    n //=10
print("자릿수 : %d" % cnt)

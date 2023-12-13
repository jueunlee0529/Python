def f(n) :
    for i in range(1, n+1):
        print("")
        for j in range(1, n+1) :
            print("%2d" %(i*j), end = ' ')

n = int(input("정수 입력 : "))
f(n)

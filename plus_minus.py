def func_abs(n) :

    if n > 0 :
        return n
    elif n < 0 :
        return n * -1
    else :
        return "zero"

n = int(input("정수 입력: "))
print(func_abs(n))

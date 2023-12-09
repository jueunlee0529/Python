def get_sum(n) :
    s = 0
    for i in range(1, n+1) :
        s += i
    return s

n = int(input())
print("1부터 %d까지의 합은 %d입니다." % (n, get_sum(n)))

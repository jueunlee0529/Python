def get_sum(a, b) :
    s = 0
    for i in range(a, b+1) :
        s += i
    return s

a = int(input())
b = int(input())

print("%d 부터 %d 까지의 합은 %d" % (a, b, get_sum(a, b)))

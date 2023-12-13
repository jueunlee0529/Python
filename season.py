def month(m) :
    if 2 < m < 6 :
        print("Spring")
    elif 5 < m < 9 :
        print("Summer")
    elif 8 < m < 12 :
        print("Fall")
    else :
        print("Winter")

m = int(input())
month(m)

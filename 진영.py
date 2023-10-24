L = int(input("L 판매 개수 : "))
M = int(input("M 판매 개수 : "))
S = int(input("S 판매 개수 : "))

# sum = 총 매출 저장 변수
sum = 2500 * L
sum += 1000 * M
sum += 500 * S

print("오늘의 총 매출은 %d원입니다." % sum)

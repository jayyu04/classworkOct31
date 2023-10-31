starCount = int(input("請輸入星星數目："))
9
halfLineNumber = 0
a = starCount

while True:
    if a <= 1:
        break
    a = a - 2
    halfLineNumber = halfLineNumber + 1

for i in range(halfLineNumber):
    print(" " * ((starCount - a) // 2) + "*" * a )
    a = a+2

print("*" * starCount)

for i in range(halfLineNumber):
    if a < 1:
        break
    a = a-2
    print(" " * ((starCount - a) // 2) + "*" * a )


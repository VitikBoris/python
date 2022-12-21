a = int(input())
s = 1
mn = a
mx = 0
while a != 0:
    digit = a % 10
    if mn > digit:
        mn = digit
    if mx < digit:
        mx = digit
    a = a // 10
    print(digit)
    s = s * digit
print('max',mx)
print('min',mn)
print(s)
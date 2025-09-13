t = (5, 2, 9, 1, 7)
# Output → Max = 9, Min = 1

print(max(t))
num1 = float('-inf')
for num in t:
    if num > num1:
        num1 = num

print(num1)
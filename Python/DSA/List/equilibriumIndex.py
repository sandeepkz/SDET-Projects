# Input  → [1, 3, 5, 2, 2]
# Output → 2
# Explanation: index=2 → left sum=1+3=4, right sum=2+2=4

inp = [1, 3, 5, 2, 2]
inp2 = list(reversed(inp))
ls = rs = 0
for i in range(len(inp)):
    ls += inp[i]
    rs += inp2[i]
    if ls == rs:
        print(i+1)
        break
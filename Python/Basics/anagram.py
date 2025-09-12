txt1 = "Heart"
txt2 = "Earth"

for txt in txt1.lower():
    if txt not in txt2.lower():
        print("Not-Anagram")
        break
else:
    print("Anagram")

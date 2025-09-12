with open('test.txt', 'r') as fr:
    content = fr.readlines()
    print("Original:", content)

    # Reverse the list
    content = list(reversed(content))
    print("Reversed:", content)

    # Write back reversed content
    with open('test.txt', 'w') as fw:
        for line in content:
            fw.write(line)

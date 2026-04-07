words = input().split()

for i in range(len(words)):
    for j in range(len(words[i])):
        if not words[i][j].isalpha():
            words[i] = words[i].replace(words[i][j], '')

print(words)
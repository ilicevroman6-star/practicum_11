text = []
string = ' '

while string != '':
    string = input()

    if string != '':
        text.append(string)

text_new = []

for i in range(len(text)):
    text[i] = text[i].split()
    text_new.extend(text[i])

for i in range(len(text_new)):
    text_new[i] = text_new[i].lower()

    for j in range(len(text_new[i])):
        if not text_new[i][j].isalpha():
            text_new[i] = text_new[i].replace(text_new[i][j], '')

text_new = sorted(text_new, key=lambda x: text_new.count(x), reverse=True)

for word in text_new:
    if text_new.count(word) > 1:
        text_new.remove(word)

for word in text_new:
    print(word)
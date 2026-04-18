def with_holes(string: str) -> int:
    '''
    string is a word to search for special letters in it
    '''
    
    cnt = 0

    for char in string:
        if char in special_letters:
            cnt += 1

    return cnt


def without_holes(string: str) -> int:
    '''
    string is a word to search for all non-special letters in it.
    '''
    
    cnt = 0

    for char in string:
        if char not in special_letters:
            cnt += 1

    return cnt


if __name__ == '__main__':
    special_letters = 'a', 'b', 'd', 'e', 'g', 'o', 'p', 'q'
    words = input().split()

    new_words = []

    for word in words:
        if with_holes(word) > 1:
            new_words.append(word)

    print('Количество букв с отверстиями:', with_holes(letters))
    print('Количество букв без отверстий:', without_holes(letters))
    print(new_words)

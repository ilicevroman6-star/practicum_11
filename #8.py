def sorting(string: str) -> str:
    symbols = []

    for char in string:
        symbols.append(char)

    symbols.sort()

    return ''.join(symbols)

if __name__ == '__main__':
    print(sorting(input()))
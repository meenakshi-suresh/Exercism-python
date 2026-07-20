def is_valid(isbn):
    if not isbn.isalnum():
        isbn = isbn.replace('-','')

    if len(isbn) != 10:
        return False

    total = 0

    for index in range(len(isbn) - 1, -1, -1):
        if isbn[index] == 'X':
            if index != 9:
                return False
            value = 10
        elif isbn[index].isdigit():
            value = int(isbn[index])
        else:
            return False
        total += (index + 1) * value

    return total % 11 == 0


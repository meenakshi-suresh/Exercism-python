def is_armstrong_number(number):
    num = number
    sum = 0
    number_length = len(str(number))

    while num != 0:
        digit = num % 10
        sum += digit ** number_length
        num = num // 10
    if sum == number:
        return True
    return False
    
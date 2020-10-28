def add_digits(num):
    sum = 0
    while num > 0:
        dig = num % 10
        sum += dig
        num = int((num - dig) / 10)
    print(sum)
    return sum



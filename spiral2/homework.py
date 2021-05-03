def spiralize(size, n=1):
    x = n
    y = 2
    current_value = n
    reset = 0
    while current_value < pow(size, 2) + n - 1:
        current_value += y
        x += current_value
        reset += 1
        if reset == 4:
            y += 2
            reset = 0
    return current_value

print(spiralize(501,15))

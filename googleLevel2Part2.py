def answer(x, y):
    # Start of the row at height y
    start = 1 + (y*(y - 1) // 2)
    # Take x - 1 steps over
    steps = x - 1
    # Increased by 1 each time, starting at y + 1
    change = y + 1
    for i in range(steps):
        start += change
        change += 1
    return str(start)

print(answer(3,5))

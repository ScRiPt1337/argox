x = 5000
for i in range(14):
    if i >= 1 or i >= 2:
        x = x + 5000
    task = [ports for ports in range(x - 5000, x)]
    print(task)
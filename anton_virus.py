n = int(input())
for i in range(1, n + 1):
    s = input()
    pos = 0
    for char in s:
        if pos < 5 and char == "anton"[pos]:
            pos += 1
    if pos == 5:
        print(i, end=" ")
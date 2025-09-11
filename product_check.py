n = int(input())

lst = [int(input()) for i in range(n)]
res = int(input())

flag ="НЕТ"
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] * lst[j] == res:
            flag = "ДА"
            break
print(flag)

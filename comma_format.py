n = input()
result = ""
for i, digit in enumerate(reversed(n)):
    if i > 0 and i % 3 == 0:
        result = "," + result
    result = digit + result
print(result)
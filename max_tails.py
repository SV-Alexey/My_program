s = input()
max_count = 0
current_count = 0

for char in s:
    if char == 'Р':
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        current_count = 0

print(max_count)
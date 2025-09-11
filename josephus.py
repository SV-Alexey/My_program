n = int(input())
k = int(input())
people = list(range(1, n + 1))
pos = 0
while len(people) > 1:
    pos = (pos + k - 1) % len(people)
    people.pop(pos)
print(people[0])
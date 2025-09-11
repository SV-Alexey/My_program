word = input()
text = word + " запретил букву"
letters = sorted(set(text.replace(" ", "")))

for letter in letters:
    if letter in text:
        print(text + " " + letter)
        text = text.replace(letter, "")
        text = " ".join(text.split())
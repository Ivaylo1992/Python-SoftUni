text = list(input())
text.sort()

characters_counter = {}

for char in text:
    if not characters_counter.get(char):
        characters_counter[char] = 0

    characters_counter[char] += 1

for char, occurrences in characters_counter.items():
    print(f"{char}: {occurrences} time/s")

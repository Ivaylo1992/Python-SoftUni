def concatenate(*args, **kwargs):
    def concatenate_strings(strings: tuple) -> str:
        return ''.join(strings)

    def mutate_string(current_string: str, old: str, new: str) -> str:
        return current_string.replace(old, new)

    string = concatenate_strings(args)

    for old_str, new_str in kwargs.items():
        if old_str in string:
            string = mutate_string(string, old_str, new_str)

    return string

print(concatenate(
    "Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"
))

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
def even_odd(*args) -> list:
    info = list(args)
    command = info.pop()
    numbers = info

    def find_evens(nums: list[int]) -> list[int]:
        return list(filter(lambda x: x % 2 == 0, nums))

    def find_odds(nums: list[int]) -> list[int]:
        return list(filter(lambda x: x % 2 != 0, nums))

    actions_mapper = {
        'even': find_evens,
        'odd': find_odds
    }

    return actions_mapper[command](numbers)



print(even_odd(1, 2, 3, 4, 5, 6, "odd"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

def even_odd_filter(**kwargs):
    def find_evens(nums: list[int]) -> list[int]:
        return list(filter(lambda x: x % 2 == 0, nums))

    def find_odds(nums: list[int]) -> list[int]:
        return list(filter(lambda x: x % 2 != 0, nums))

    actions_mapper = {
        'even': find_evens,
        'odd': find_odds
    }

    result = {}

    for command, numbers in kwargs.items():
        result[command] = actions_mapper[command](numbers)

    return dict(sorted(result.items(), key=lambda x: -len(x[0])))


print(even_odd_filter(

odd=[2, 2, 30, 44, 10, 5],

))
def sorting_cheeses(**kwargs):
    sorted_cheeses = dict(sorted(kwargs.items(), key=lambda x: (-len(x[1]), x)))

    for key in sorted_cheeses:
        sorted_cheeses[key] = sorted(sorted_cheeses.get(key), reverse=True)

    result = []

    for cheese, cheese_info in sorted_cheeses.items():
        result.append(cheese)
        for info in cheese_info:
            result.append(str(info))

    return '\n'.join(result)


print(sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
      ))
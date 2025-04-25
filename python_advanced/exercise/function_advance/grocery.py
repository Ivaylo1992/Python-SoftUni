def grocery_store(**kwargs):
    sorted_products =  sorted(kwargs.items(), key=lambda kv: (-kv[1], -len(kv[0]), kv[0]))

    result = [f'{info[0]}: {info[1]}' for info in sorted_products]

    return '\n'.join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=20,
    pasta=20,
    eggs=20,
    carrot=20,
))
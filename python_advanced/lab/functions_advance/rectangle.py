def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    def area():
        return f'Rectangle area: {length * width}'

    def perimeter():
        return f'Rectangle perimeter: {2 * (length + width)}'

    calculated_area = area()
    calculated_perimeter = perimeter()

    return f'{calculated_area}\n{calculated_perimeter}'

print(rectangle('2', 10))
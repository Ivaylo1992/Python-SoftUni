class Integer:
    def __init__(self, value: int) -> None:
        self.value = value

    @classmethod
    def from_float(cls, value):
        if not isinstance(value, float):
            return "value is not a float"

        new_value = int(value)
        return cls(new_value)

    @classmethod
    def from_roman(cls, value: str) -> "Integer":
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        new_value = 0

        for i in range(len(value)):
            el = value[i]
            if roman_values.get(el, None) and i + 1 >= len(value):
                new_value += roman_values[el]
            elif i + 1 < len(value) and \
                    roman_values.get(value[i+1], None) > roman_values.get(el, None):
                new_value -= roman_values[el]
            else:
                new_value += roman_values[el]

        return cls(new_value)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str) or not value.isdigit():
            return "wrong type"

        new_value = int(value)
        return cls(new_value)


first_num = Integer(10)
print(first_num.value)
second_num = Integer.from_roman("MCMXCIV")
print(second_num.value)
print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
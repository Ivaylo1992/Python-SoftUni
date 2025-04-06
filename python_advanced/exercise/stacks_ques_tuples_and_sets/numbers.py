from collections import deque


def add_element(sequence:set, sequence_to_add: set) -> set:
    sequence.update(sequence_to_add)
    return sequence


def remove_element(sequence: set, elements_to_remove: set) -> set:
    for el in elements_to_remove:
        if el in sequence:
            sequence.remove(el)
    return sequence


first_sequence = set(input().split())
second_sequence = set(input().split())

iterations = int(input())

functions_mapper = {
    'Add First': add_element,
    'Add Second': add_element,
    'Remove First': remove_element,
    'Remove Second': remove_element,
    'Check Subset': lambda x, y: x.issubset(y),
}

for _ in range(iterations):
    command = deque(input().split(' '))

    action = f'{command.popleft()} {command.popleft()}'
    nums = set(command)

    if 'First' in action:
        functions_mapper[action](first_sequence, nums)
    elif 'Second' in action:
        functions_mapper[action](second_sequence, nums)
    else:
        print(functions_mapper[action](second_sequence, first_sequence))

print(', '.join(first_sequence))
print(', '.join(second_sequence))

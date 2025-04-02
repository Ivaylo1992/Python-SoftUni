from collections import deque

nums = deque()
operations = int(input())

def add_number(collection: deque, num):
    collection.append(num)

    return collection

def delete_number(collection: deque) -> deque:
    if collection:
        collection.pop()
    return collection

def get_max_num(collection: deque) -> None:
    if collection:
        print(max(collection))

def get_min_num(collection: deque)-> None:
    if collection:
        print(min(collection))

def reverse_stack(collection: deque) -> deque:
    new_collection = deque()
    iterations = len(collection)

    [new_collection.append(collection.pop()) for _ in range(iterations)]

    return new_collection

operation_mapper = {
    '1': add_number,
    '2': delete_number,
    '3': get_max_num,
    '4': get_min_num,
}

for _ in range(operations):
    operation = input().split()

    if len(operation) == 2:
        num_to_add = int(operation[1])
        operation_mapper[operation[0]](nums, num_to_add)
    else:
        operation_mapper[operation[0]](nums)

print(', '.join([str(num) for num in reverse_stack(nums)]))
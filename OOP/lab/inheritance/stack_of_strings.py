class Stack(list):
    def __init__(self):
        super().__init__()
        self.data = []

    def pop(self, index=None):
        if not self.is_empty():
            return self.data.pop()
        return None

    def is_empty(self):
        return len(self.data) == 0

    def top(self):
        return self.data[-1]

    def push(self, element):
        self.data.append(element)

    def __str__(self):
        reversed_data = self.data[::-1]
        result = f'[{", ".join([el for el in reversed_data])}]'

        return result

stack = Stack()
stack.push("apple")
stack.push("carrot")
print(stack.data)
print(stack.pop())
# test zero
import unittest


# class StackTests(unittest.TestCase):
#     def test_zero(self):
#         stack = Stack()
#         stack.push("apple")
#         stack.push("carrot")
#         self.assertEqual(str(stack), '[carrot, apple]')
#         self.assertEqual(stack.pop(), 'carrot')
#         self.assertEqual(stack.top(), 'apple')
#         stack.push("cucumber")
#         self.assertEqual(str(stack), '[cucumber, apple]')
#         self.assertEqual(stack.is_empty(), False)
#
#
# if __name__ == '__main__':
#     unittest.main()
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def testStack():
    s = Stack()
    print(s.is_empty())
    s.push(4)
    print(s.peek())
    print(s.size())


def reverse_list(lst):
    result = []
    s = Stack()
    for e in lst:
        s.push(e)
    while not s.is_empty():
        e = s.pop()
        result.append(e)

    return result


def test_reverse_list():
    lst = [1, 2, 3, 4, 5, 6]
    result = reverse_list(lst)
    print(result)


def decimal_to_binary(n):
    s = Stack()
    while n > 0:
        rem = n % 2
        s.push(rem)
        n = n // 2

    result = ""
    while not s.is_empty():
        result += str(s.pop())

    return result


testStack()
test_reverse_list()
print(decimal_to_binary(256))

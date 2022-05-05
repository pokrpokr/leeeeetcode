from typing import List
def insert_sort(array: List):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while array[j] > array[i]:
            pass
    pass

def test():
    return [lambda y: i * y for i in range(4)]

def super_test(l):
    def inner(func):
        return func
    return inner


if __name__ == "__main__":
    print([m(50) for m in test()])
    
from itertools import chain

nested_list = [
	['a', 'b', 'c',[1, 2, None]],
	['d', 'e', [1, ['A', 'A', [True, True, True], 'A'], 2, None],'f', 'h', False],
	[1, 2, None]
]

class FlatIterator:

    def __init__(self, _list):
        self.index = -1
        self.list = _list
        # print(f'{self.list = }')
        # print(f'{self = }')

    def join_list(self):
        flag = True
        while flag:
            l, flag  = [], False
            for i in self.list:
                if isinstance(i, list):
                    l.extend(i)
                    flag = True
                else:
                    l.append(i)
            self.list = l
        return self.list

    def __iter__(self):
        return self

    def __next__(self):
        self.join_list()
        self.index += 1
        if self.index == len(self.list):
            raise StopIteration

        return self.list[self.index]


a = FlatIterator(nested_list)
for item in a:
    print(item)
print('-'*30)

# 2 Написать генератор (просто взял метод из класса)
def flat_generator(my_list):
    flag = True
    while flag:
        l, flag = [], False
        for i in my_list:
            if isinstance(i, list):
                l.extend(i)
                flag = True
            else:
                l.append(i)
        my_list = l
    for i in my_list:
        yield i

for item in  flat_generator(nested_list):
    print(item)


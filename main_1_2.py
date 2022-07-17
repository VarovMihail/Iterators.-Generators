nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]
]
# 1 Написать итератор
class FlatIterator:

    def __init__(self, _list):
        self.index = -1
        self.list = sum(_list,[])

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.list):
            raise StopIteration
        return self.list[self.index]

for item in FlatIterator(nested_list):
    print(item)

# а комперхеншн, выражение вернет плоский список
flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

# # 2 Написать генератор, который принимает список списков, и возвращает их плоское представление.
def flat_generator(my_list):
    for i in sum(my_list,[]):
        yield i

for item in  flat_generator(nested_list):
    print(item)








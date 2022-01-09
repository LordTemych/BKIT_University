from gen_random import gen_random

class Unique(object):

    def __init__(self, items, **kwargs):

        self.items = items

        if kwargs:
            seen, result = set(), []
            for item in self.items:
                if type(item) == str:
                    if str(item.lower()) not in seen:
                        seen.add(item.lower())
                        result.append(item)
                else:
                    if item not in seen:
                        seen.add(item)
                        result.append(item)
        else:
            result = list(set(self.items))

        self.items = result



    def __next__(self):
        self.items += 1
        return (self.items)

    def __iter__(self):
        return (el for el in self.items)


data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
print(data1)
'''for i in Unique(data, ignore_case=True):
    print(i)'''
un1 = Unique(data1)
for i1 in un1:
    print(i1, end=' ')
print('\n')

data2 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
print(data2)
un2 = Unique(data2)
for i2 in un2:
    print(i2, end=' ')
print('\n', end='')

un3 = Unique(data2, ignore_case=True)
for i2 in un3:
    print(i2, end=' ')
print('\n')
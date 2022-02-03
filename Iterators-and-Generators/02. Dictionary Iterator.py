class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys = list(self.dictionary.keys())
        self.keys_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.keys_idx >= len(self.keys):
            raise StopIteration
        key = self.keys[self.keys_idx]
        value = self.dictionary[key]
        self.keys_idx += 1
        return key, value


# d = {'x': 1, 'y': 2}
# print(list(d.keys()))


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

"--------------------------------------------------------------------------------------------"
# with deque
from collections import deque


class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys = deque(self.dictionary.keys())

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.keys) == 0:
            raise StopIteration
        key = self.keys.popleft()
        value = self.dictionary[key]
        return key, value


# d = {'x': 1, 'y': 2}
# print(list(d.keys()))


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

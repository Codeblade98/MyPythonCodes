from typing import List


class SuperList(List):
    def __len__(self):
        return 1000

sl1 = SuperList([1,2,3,4,5])
print(SuperList())
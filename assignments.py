class MaxSizeList(object):

    def __init__(self, count: int):
        self.count = count
        self.my_list = []

    def push(self, word: str):
        self.my_list.append(word)
        if len(self.my_list) > self.count:
            self.my_list.pop(0)

    def get_list(self) -> [str]:
        return self.my_list
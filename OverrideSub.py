class MyList(list):
    """implement the subtracion of list"""
    """[1, 2, 3] - [2, 1, 5] = [3]"""
    def __sub__(self, b):
        copy = self[:]
        for element in copy:
            if element in b:
                self.remove(element)
        return self
print MyList([1,2,3]) - MyList([2,1,5])
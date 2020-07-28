class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        A=max(self.__elements)
        b=min(self.__elements)
        self.maximumDifference = A-b

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

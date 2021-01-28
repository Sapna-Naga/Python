# Iterator:

# to create own iterator:
class TopTen:
              def __int__(self):
                             self.num=1
              def __iter__(self):
                             return self
              def __next__(self):
                             if self.num<=10:
                                           val=self.num
                                           self.num+=1
                                           return val
                             else:
                                           raise StopIteration

values=TopTen()

print(next(values)) # even with this, the value will be printed once and will not repeat.

for i in values:
              print(i)

# Generators:

# to create generator:
def topten():
              yield 1
              yield 2
              yield 3
              yield 4

values = topten()

print(values.__next__())
print(values.__next())

for i in values:
              print(i)
              
# Top 10 perfect square numbers:
def topten():
              n=1
              while n<=10:
                             sq=n*n
                             yield sq
                             n+=1
              
values = topten()

for i in values:
              print(i)  # when we want to work one value at a time, we use generator.

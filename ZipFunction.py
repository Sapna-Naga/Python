# Zip function in Python:

names=("Navin","Kiran","Priya)
comps=("Dell","Apple","MS")

zipped = list(zip(names,comps))
print(zipped)

# Instead of list we can use set:-> If we use set - there will be no duplicates.

zipped = set(zip(names,comps))
print(zipped)

# using iterator:
zipped = zip(names,comps)

for (a,b) in zipped:
    print(a,b)

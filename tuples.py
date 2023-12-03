
mytuple = tuple(('Dave', 42, True))
anothertuple = (1, 4, 2, 8, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))
# cannot change the data in a tuple but can add to it
newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one, two, *hey) = anothertuple # unpacking a tuple
print(one)
print(two)
print(hey)

(one, *two, hey) = anothertuple # put the remainder in two instead of hey
print(one)
print(two)
print(hey)

print(anothertuple.count(2)) # count the number of 2's in the tuple


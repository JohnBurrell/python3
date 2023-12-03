# Dictinaries

band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Access items
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list key/value pairs as tuples
print(band.items())

# does key exist
print("guitar" in band)
print("triangle" in band)

# change values/ input new pairs
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

# remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

# remove last item
print(band.popitem()) # a tuple
print(band)

# delete an item
band["drums"] = "Bonham"
del band["drums"]
print(band)

# empty a dictionary
band2.clear() # leaves an empty dict
print(band2)
# delete it
del band2

# copy dictionaries

# band2 = band # only creates a reference,i.e. same location in memory
# print("bad copy")
# print(band2)
# print(band)
# band2["drums"] = "Dave"
# print(band) # now drums is in band as well

band2 = band.copy()
band2["drums"] = "Dave"
print("good copy")
print(band)
print(band2)
# or use the dict() constructor
band3 = dict(band)
print(band3)

# nested dictionaries
# i.e the value in the dict can be another dict
member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]["name"])

# Sets

nums = {1, 2, 3, 4}
nums2 = set((1,2,3,4))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# no duplicates allowed
nums = {1,2,2,3}
print(nums)

# True is equiv 1, False is equiv 0
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# check if value is in the set
print(2 in nums)
# but you can't refer to an element in the set with an index position

# add a new element to a set
nums.add(8)
print(nums)

# can add elements from one set to another
morenums = {5,6,7}
nums.update(morenums)
print(nums)

# you can use update with lists, tuples and dictionaries

# merge two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}
mynewset = one.union(two)
print(mynewset)

# keep only the duplicates
one = {1, 2, 3, 4, 5}
two = {3, 4, 5, 6, 7, 8}
one.intersection_update(two)
print(one)

# keep everything except the duplicates
one = {1, 2, 3, 4, 5}
two = {3, 4, 5, 6, 7, 8}
one.symmetric_difference_update(two)
print(one)

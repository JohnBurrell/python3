
users = ['Dave', 'John', 'Sarah']

data = ["Dave", 42, True]

emptylist = []

print("Dave" in emptylist)

print(users[0])
print(users[-2])

print(users.index('Sarah'))

print(users[0:2])
print(users[1:])
print(users[-3:-1]) # same as 0:2 since there are only 3 items

print(len(data))
# append
users.append('Elsa')
print(users)

users += ['Jason'] # without [] the list is 'J', 'a', 's' etc
print(users)
# extend with another list
users.extend(['Robert', 'Jimmy'])
print(users)
users.extend(data) # adds the data list to the end of users

users.insert(0, 'Bob')
print(users)

users[2:2] = ['Eddie', 'Alex'] # adds Eddie and Alex starting at position 2
print(users)

users[1:3] = ['Robert', 'JPJ'] # replace Dave and Eddie by Robert and JPJ
print (users)

users.remove('Bob')
print(users)

print(users.pop()) # remove True from the end
print(users)

del users[0] # delete Robert from the front of the list
print(users)

# delete an entire list
#del data
#print(data) # raises a NameError
# instead, if you cleared data you would have an empty list
data.clear()
print(data)

users.remove(42) # can't sort with mixed int and str data
print(users)

users[1:2] = ['dave'] # add a lowercase dave
users.sort()
print(users)
# sort would put dave at the end. To include dave in the correct alphabetical position, use lower

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)
nums.sort()
print(nums)
nums.reverse()
print(nums)
nums = [4, 42, 78, 1, 5]
#nums.sort(reverse=True) # changes the original nums list
#print(nums)
print(sorted(nums, reverse=True))
print(nums) # the original list stays the same

# how to create a copy of nums
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
print(mycopy)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Neil", True]) # use the constructor to create a list
print(mylist)
friends = ["John","Kevin", "Karen", "Jim", "Peter", "John"]
lucky_numbers = [4, 5, 4, 8, 9, 6, 2, 22, 5, 4, 8]
print(friends[1])
print(friends[-1])
print(friends[-3])
print(friends[1:])
print(friends[:1])
print(friends[0:3])
# combine multiple lists together
friends.extend(lucky_numbers)
# List Function:
#  f1.extend( f2 ) - adds two lists
#  f1.insert( index, f1)- inserts an elements
#  f1.remove(value) - removes the element
#  f1.pop() - removes last element off the list
#  f1.count(value)- counter
#  f1.reverse() - reverses the original order of the list
#  f2=f1.copy() - will copy one list to another
# instert into a list at a specific position:
# friends.insert(0, lucky_numbers[2])
# you can remove elemet with remove
# friends.remove("John")
# friends.remove(friends[0])
# delete all elements
# friends.clear()
# find position with index
# print(friends.index("John"))
# print(friends.count("John"))
# put in alphabetical order
friends.sort()
# copy
friends2 = friends.copy()
print(friends)
lucky_numbers.sort()
lucky_numbers.reverse()
print(friends2)


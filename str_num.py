# string
phrase = "GTT test"
print(phrase.lower().islower())
print(phrase.upper().isupper())
print(phrase.lower() + " is cool")
print(len(phrase))
print(phrase.lower() + " is cool")
print(phrase.lower() + " is cool")
print(phrase[0])
print(phrase.index("test"))
print(phrase.replace("test", "tests"))

# numbers
# any
print(-2.54)
# reminder
print(10 % 3)
# save in var
my_num = -7
print(my_num)
# to string
print(str(my_num) + " is my fav num")
# abs absolute value
print(abs(my_num))
# pow koren
print(pow(4, 28))
# max returns the highest number
print(max(5, 8, 0, 99, 12))
# min returns the highest number
print(min(5, 8, 0, 99, 12))
# round the numbers
print(round(6.5))
print(round(6.51))

# Other examples would have to use some external code (module) that needs to be imported via IMPORT
from math import *

# floor() would remove the dişimle point
print(floor(2.5))
# ceil() rounds the number up no matter what value is placed after the disimle point 1 or 9
print(ceil(5.1))
# sqrt() would do sqare root
print(sqrt(36))



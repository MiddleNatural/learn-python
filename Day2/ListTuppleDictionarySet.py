# List is a collection which is ordered and changeable. ALLOW DUPLICATEs members.
# Tuple is a collection which is ordered and UNCHAMGEABLE. Allows duplicate members.
#   extract the values back into variables. This is called "UNPACKING"
# Set is a collection which is unordered, unchangeable*, and unindexed. NO DUPLICATE members.
#   unchangeable*: you CANNOT CHANGE its items, but you can ADD new items (or delete item).
#   unindexed: CANNOT ACCESS by indexes 
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
#   store data values in KEY:VALUE pairs.

#LIST
# list = ["apple", "banana", "cherry"]
#TUPLE
# tuple = ("apple", "banana", "cherry)
# (green, yellow, red) = fruits
# tuple2 = ("apple2", "banana2", "cherr2)
# tuple3 = tuple + tuple2
#SET
# -> Uniom: all items from BOTH sets
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1 | set2
# -> Intersection: contains the items that are PRESENT IN BOTH set
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.intersection(set2)
# -> Difference: contain only the items from the first set that are NOT PRESENT IN THE OTHER set.
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.difference(set2)
# -> Symmetric Differences: keep only the elements that are NOT PRESENT IN BOTH sets
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 ^ set2
#DICTIONARY
# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
lst = ["ala", "bala", "porto", "cala", "ala", "bala", "ala"]


# .count() și .index() sunt comune tuturor sequences
lst.count("ala")  # --> 3
lst.count("bala") # --> 2

lst.index("ala")  # --> 0
lst.index("bala") # --> 1
# cu argument opțional start:
lst.index("ala", 1)  # --> 4

#lst.index("does not exist")
# raises ValueError

#.append() # one item
#.extend() # more items

#.pop() # remove and return last (or one) item
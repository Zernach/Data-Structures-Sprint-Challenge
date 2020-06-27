import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = list(f.read().split("\n"))  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = list(f.read().split("\n"))  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

for name in names_1:
    if name in names_2:
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

"""
STRETCH
* Say your code from `names.py` is to run on an embedded computer 
with very limited RAM. Because of this, memory is extremely constrained 
and you are only allowed to store names in arrays (i.e. Python lists). 
How would you go about optimizing the code under these conditions? 
Try it out and compare your solution to the original runtime. 
(If this solution is less efficient than your original solution, 
include both and label the strech solution with a comment)
"""
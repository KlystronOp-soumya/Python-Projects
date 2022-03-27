# Python program to demonstrate
# iterator module


import itertools
import operator
import time
from itertools import combinations, combinations_with_replacement, permutations, product

# Defining lists
L1 = [1, 2, 3]
L2 = [2, 3, 4]

# Starting time before map
# function
t1 = time.time()

# Calculating result
a, b, c = map(operator.mul, L1, L2)

# Ending time after map
# function
t2 = time.time()

# Time taken by map function
print("Result:", a, b, c)
print("Time taken by map function: %.6f" %(t2 - t1))

# Starting time before naive
# method
t1 = time.time()

# Calculating result using for loop
print("Result:", end = " ")
for i in range(3):
	print(L1[i] * L2[i], end = " ")
	
# Ending time after naive
# method
t2 = time.time()
print("\nTime taken by for loop: %.6f" %(t2 - t1))

#Cartesian product of the iterables
print("Cartesian product of the two lists is: ",product(L1,L2))
print("Cartesian product of the  list L1 for 3 times is: ",product(L1,repeat=3))

# for in loop
for i in itertools.count(5, 5):
    if i == 35:
        break
    else:
        print(i, end =" ")
count=0
for i in itertools.cycle('AB'):
    if count > 7:
        break
    else:
        print(i, end = " ")
        count += 1
l = ['Geeks', 'for', 'Geeks']
   
# defining iterator
iterators = itertools.cycle(l)
   
# for in loop
for i in range(6):
       
    # Using next function
    print(next(iterators), end = " ")

print ("Printing the numbers repeatedly : ") 
print (list(itertools.repeat(25, 4)))

print ("All the permutations of the given list is:") 
print (list(permutations([1, 'geeks'], 2)))
print()
  #Terminating iterators
print ("All the permutations of the given string is:") 
print (list(permutations('AB')))
print()
   
print ("All the permutations of the given container is:") 
print(list(permutations(range(3), 2)))

print ("All the combination of list in sorted order(without replacement) is:") 
print(list(combinations(['A', 2], 2)))
print()
   
print ("All the combination of string in sorted order(without replacement) is:")
print(list(combinations('AB', 2)))
print()
   
print ("All the combination of list in sorted order(without replacement) is:")
print(list(combinations(range(2), 1)))

print ("All the combination of string in sorted order(with replacement) is:")
print(list(combinations_with_replacement("AB", 2)))
print()
   
print ("All the combination of list in sorted order(with replacement) is:")
print(list(combinations_with_replacement([1, 2], 2)))
print()
   
print ("All the combination of container in sorted order(with replacement) is:")
print(list(combinations_with_replacement(range(2), 1)))

# initializing list 1
li1 = [1, 4, 5, 7]
   
# using accumulate()
# prints the successive summation of elements
print ("The sum after each iteration is : ", end ="")
print (list(itertools.accumulate(li1)))
   
# using accumulate()
# prints the successive multiplication of elements
print ("The product after each iteration is : ", end ="")
print (list(itertools.accumulate(li1, operator.mul)))
   
# using accumulate()
# prints the successive summation of elements
print ("The sum after each iteration is : ", end ="")
print (list(itertools.accumulate(li1)))
   
# using accumulate()
# prints the successive multiplication of elements
print ("The product after each iteration is : ", end ="")
print (list(itertools.accumulate(li1, operator.mul)))

"""
Chains all the iterators one after another
"""
# initializing list 1
li1 = [1, 4, 5, 7]
   
# initializing list 2
li2 = [1, 6, 5, 9]
   
# initializing list 3
li3 = [8, 10, 5, 4]
 
# using chain() to print all elements of lists
print ("All values in mentioned chain are : ", end ="")
print (list(itertools.chain(li1, li2, li3)))

"""
This iterator selectively picks the values to print from the passed container according to the 
boolean list value passed as other arguments.
 The arguments corresponding to boolean true are printed else all are skipped.
"""

print ("The compressed values in string are : ", end ="")
print (list(itertools.compress('SOUMYADEEP', [1,0,0,0,0,0,1,1,1,1])))

"""
This iterator starts printing the characters only after the func. in argument returns false for the first time
"""
# initializing list 
li = [2, 4, 5, 7, 8]
   
# using dropwhile() to start displaying after condition is false
print ("The values after condition returns false : ", end ="")
print (list(itertools.dropwhile(lambda x : x % 2 == 0, li)))

"""
this iterator prints only values that return false for the passed function.
"""
# initializing list 
li = [2, 4, 5, 7, 8]
 
# using filterfalse() to print false values
print ("The values that return false to function are : ", end ="")
print (list(itertools.filterfalse(lambda x : x % 2 == 0, li)))

"""
This iterator selectively prints the values mentioned in its iterable container passed as argument. 
This iterator takes 4 arguments, iterable container, starting pos., ending position and step.

"""
# initializing list 
li = [2, 4, 5, 7, 8, 10, 20]
     
# using islice() to slice the list acc. to need
# starts printing from 2nd index till 6th skipping 2
print ("The sliced list values are : ", end ="")
print (list(itertools.islice(li, 1, 6, 2)))

"""
This iterator takes a function and tuple list as argument and returns 
the value according to the function from each tuple of the list.
"""
# initializing tuple list
li = [ (1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10, 1) ]
   
# using starmap() for selection value acc. to function
# selects min of all tuple values
print ("The values acc. to function are : ", end ="")
print (list(itertools.starmap(min, li))) #reuturns minimum from each tuple

"""
This iterator is the opposite of dropwhile(), it prints the values till the function returns false for 1st time.
or takes the value when it is true
"""
# initializing list 
li = [2, 4, 6, 7, 8, 10, 20]
   
# using takewhile() to print values till condition is false.
print ("The list values till 1st false value are : ", end ="")
print (list(itertools.takewhile(lambda x : x % 2 == 0, li )))

"""
This iterator splits the container into a number of iterators mentioned in the argument.
"""
# initializing list 
li = [2, 4, 6, 7, 8, 10, 20]
   
# storing list in iterator
iti = iter(li) 
   
# using tee() to make a list of iterators
# makes list of 3 iterators having same values.
it = itertools.tee(iti, 3)
   
# printing the values of iterators
print ("The iterators are : ")
for i in range (0, 3):
    print (list(it[i]))

"""
his iterator prints the values of iterables alternatively in sequence. 
If one of the iterables is printed fully, the remaining values are filled by the values assigned to fillvalue.
"""
# using zip_longest() to combine two iterables.
print ("The combined values of iterables is  : ")
print (*(itertools.zip_longest('GesoGes', 'ekfrek', fillvalue ='_' )))
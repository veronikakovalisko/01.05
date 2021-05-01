"""
Task 1
The greatest number
Write a Python program to get the largest number
from a list of random numbers with the length of 10
Constraints: use only while loop and random module to generate n"""
import random
if __name__ == '__main__':
    randlist = []
    x = 0
    while x < 10:
        n = random.randint(1, 30)
        randlist.append(n)
        x += 1
    print(randlist)
    mx = randlist[0]
    b = 0
    while b < 10:
        if mx < randlist[b]:
            mx = randlist[b]
        b += 1
    print(mx)
"""
Task 2
Exclusive common numbers.
Generate 2 lists with the length of 10 with random integers from 1 to 10,
and make a third list containing the common integers between the 2 initial lists without any duplicates.
Constraints: use only while loop and random module to generate numbers
"""
if __name__ == '__main__':
    n = 0
    list1 = []
    list2 = []
    while n < 10:
        x1 = random.randint(1, 10)
        list1.append(x1)
        x2 = random.randint(1, 10)
        list2.append(x2)
        n += 1
    print(list1, "\n", list2)
    list3 = []
    n = 0
    while n < 10:
        if list1[n] in list2 and (list1[n] in list3) == False:
            list3.append(list1[n])
        n += 1
    print(list3)
"""
Task 3

Extracting numbers.
Make a list that contains all integers from 1 to 100, 
then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.
Constraint: use only while loop for iteration
"""
if __name__ == '__main__':
    list = []
    n = 0
    while n < 100:
        x = random.randint(1, 100)
        list.append(x)
        n += 1
    n = 0
    list7 = []
    while n < 100:
        if list[n] % 7 == 0 and (list[n] % 5 == 0) == False:
            list7.append(list[n])
        if list7.count(list[n]) > 1:
           list7.remove(list[n])
        n += 1
    print(list7)

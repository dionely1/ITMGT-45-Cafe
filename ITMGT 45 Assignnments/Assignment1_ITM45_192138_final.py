#!/usr/bin/env python
# coding: utf-8

# In[28]:


'''Assignment 1
This assignment covers your basic profiency with
    Python. It engages your ability to transform
    data without affecting anything outside the program.
This assignment places heavy emphasis on basic Python constructs.
'''

def make_change(amount):
    '''Item 6.
    Make Change. 5 points.
    
    Return the combination of coins needed to make change for the given amount,
        which is given in centavos.
    For this item:
        1. You can return 1 peso, 25 centavos, 10 centavos, 5 centavos, and 1 centavo coins.
        2. Use the minimum number of coins possible.
    Parameters
    ----------
    amount: int
        the amount, in centavos, to make change for.
    Returns
    -------
    str
        the string representation of the change to be given.
        Format it like this:
            "1P:{amount}/25C:{amount}/10C:{amount}/5C:{amount}/1C:{amount}"
    '''
    # Write your code below this line

amount=int(input('the amount, in centavos, to make change for'))
print(amount//100, "1P")
amount = amount%100
print(amount//25, "25C")
amount = amount%25
print(amount//10, "10C")
amount = amount%10
print(amount//5, "5C")
amount = amount%5
print(amount//1, "1C")


# In[3]:


def factorial(x):
    '''Item 1. 
    Factorial. 1 point.
    
    Returns the factorial of an integer.
    An integer's factorial is the product of the integer and all
        integers below it.
    Parameters
    ----------
    x: int
        the integer whose factorial to return
    Returns
    -------
    integer
        the factorial of the argument
    '''
    # Write your code below this line

num= int(input("the integer whose factorial to return"))
fact=1
if num == 0:
    print("1")
elif num<0:
    print("Does not exist")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("The factorial is",fact)


# In[29]:


def classify_grade(number_grade):
    '''Item 2.
    Classify Grade. 2 points.
    
    Returns the letter grade equivalent of a number grade.
    For this item, use these letter grade buckets:
        A: 92-100
        B+: 86-91.9
        B: 80-85.9
        C+: 74-79.9
        C: 67-73.9
        D: 60-66.9
        F: 0-59.9
    Parameters
    ----------
    number_grade: float
        the number grade to convert into a letter grade.
    Returns
    -------
    str
        the letter grade equivalent of the number grade.
    '''
    # Write your code below this line

grade= str(input("The number to convert"))

if str(100) <=grade >= str(92):
    print("A")
elif str(91.9)<=grade>=str(86):
    print("B+")
elif str(85.9)<=grade>=str(80):
    print("B")
elif str(79.9)<=grade>=str(74):
    print("C+")
elif str(73.9)<=grade>=str(67):
    print("C")
elif str(66.9)<=grade>=str(60):
    print("D")
elif str(59.9)<=grade>=str(0):
    print("F")


# In[38]:


def average_weight(item_quantity_1, item_weight_1, item_quantity_2, item_weight_2):
    '''Item 3.
    Average Weight. 3 points.
    
    You have purchased two bags of items. 
    The first bag contains one type of item, and the second bag contains another type.
    Return the weighted average weight of the items.
        
    Parameters
    ----------
    item_quantity_1: int
        the quantity of items in the first bag.
    item_weight_1: float
        the weight of each individual item in the first bag.
    item_quantity_2: int
        the quantity of items in the second bag.
    item_weight_2: float
        the weight of each individual item in the second bag.
    Returns
    -------
    float
        the weighted average weight of one item.
    '''
    # Write your code below this line
item_quantity_1= int(input("quantity of bag"))
item_weight_1= int(input("weight of bag"))
item_quantity_2= int(input("quantity of bag"))
item_weight_2= int(input("weight of bag"))

weight_bag1= int(item_quantity_1*item_weight_1)
print(weight_bag1)
weight_bag2= int(item_quantity_2*item_weight_2)
print(weight_bag2)

sum_grade= weight_bag1+weight_bag2
sum_weights= item_weight_1+item_quantity_2

weightedave=(sum_grade/sum_weights)
print("The weighted average is", weightedave)


# In[6]:


def string_sum(string):
    '''Item 4.
    String Sum. 3 points.
    
    Returns the sum of the digits provided in a string.
    For this item:
        1. Sum the digits contained in the string.
        2. Ignore any non-digit characters contained in the string.
    Parameters
    ----------
    string: str
        a string that can contain any character.
    Returns
    -------
    int
        the sum of the digits contained in the string.
    '''
    # Write your code below this line

string = input("please put number valuess with commas in between each number")
def sum_string(str1):
    sum_digit = 0
    for x in str1:
        if x.isdigit():
            y = int(x)
            sum_digit =sum_digit + y
            
    return sum_digit
print(sum_string(string))


# In[13]:


def distance(x_1, y_1, x_2, y_2):
    '''Item 5.
    Distance. 3 points.
    Returns the distance between two points.
    To get the distance between two points:
        1. Get the difference between the two x-coordinates
        2. Get the difference between the two y-coordinates
        3. Sum the previous two values
        4. Return the square root of the sum
    You may want to import the `math` library for this number.
    Parameters
    ----------
    x_1: float
        the first x-coordinate
    y_1: float
        the first y-coordinate
    x_2: float
        the second x-coordinate
    y_2: float
        the second y-coordinate
    Returns
    -------
    float
        the distance between the two coordinates
    '''
    # Write your code below this line

import math

x_1 = float(input("first x-coordinate"))
y_1 = float(input("first y-coordinate"))
x_2 = float(input("second x-coordinate"))
y_2 = float(input("second y-coordinate"))

diff_x = x_2-x_1
diff_y = y_2-y_1
sum_of_xy = diff_x + diff_y

print(math.sqrt(sum_of_xy))


# In[7]:





# In[ ]:





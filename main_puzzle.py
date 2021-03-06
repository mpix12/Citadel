#!/usr/bin/python3
'''
         10
    8         12
 7     9   11    13
                    15
'''
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

n = node(10)
n.insert(8)
n.insert(7)
n.insert(9)
n.insert(15)
n.insert(11)
n.insert(12)
n.insert(13)
n.print_tree()


'''
check if two trees are identical
'''
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def tree_identical(t1, t2):
    if t1 is None and t2 is None:
        return True

    if t1 is not None and t2 is not None:
        return ((t1.data == t2.data) and tree_identical(t1.left, t2.left) and tree_identical(t1.right, t2.right))

    return False

def tree_mirror(t1,t2):
    if t1 is None or t2 is None:
        return False

    if t1 is not None and t2 is not None:
        return ((t1.data == t2.data) and tree_mirror(t1.left,t2.right) and tree_mirror(t1.right, t2.left))


n1 = node(10)
n2 = node(10)
n1.left = node (8)
n2.right = node(8)
n1.right = node(6)
n2.left = node(6)
print(tree_mirror(n1,n2))


from itertools import permutations
from itertools import combinations

#1.GCD --Python 2.7: gcd was part of fraction nodule, in python 3 it moved to math module.

from math import gcd
print(gcd(18, 24))
print(gcd(24, 18))

def my_gcd(a,b):
    if a == 0 and b == 0:
        return 0
    if a == 0:
        return b
    if b == 0:
        return a
    while b:
        a, b = b, a%b
    return a

print(my_gcd(18, 24))
print(my_gcd(24, 18))

#2. String or number palindrome
def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    return False

print(is_palindrome(1221))
print(is_palindrome("aaabbbaaa"))
print(is_palindrome("aaabbb"))

#.3 prime number
def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

print(is_prime(4))
print(is_prime(7))

#.4 Fabonnecci series - 1 1 2 3 5 7 12

def fab_series(num):
    a, b = 0, 1
    fab_series = []
    while(b < num):
        fab_series.append(b)
        a, b = b, a+b
    return  fab_series

print(fab_series(50))

#.5 Armstrong number: 153 == 1**3 + 5**3 + 3**3

def is_armstrong(num):
    orig_num = num
    arm_num = 0
    while num:
        arm_num = arm_num + (num%10) ** 3
        num = num // 10
    if orig_num == arm_num:
        return True
    return False

print(is_armstrong(153))
print(is_armstrong(154))

#.6 Leap year

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    if year % 400 == 0:
        return True
    return False

print(is_leap_year(1900))
print(is_leap_year(2000))

#7. Factorial of number:
def calc_factorial(num):
    fact_num = 1
    for x in range(1, num):
        fact_num = fact_num + fact_num * x
    return fact_num

print(calc_factorial(6))

#8. Find Nth largest from a list

from heapq import nlargest
lst = range(1, 11)
def get_n_largest(n, lst):
    return nlargest(n, lst)[-1]

print(get_n_largest(4, lst))

#9. Combinations of list element whose sum equals to another list element

def get_sum_pair(lst):
    for x in range(1, len(lst)):
        print(x, [y for y in combinations(lst, 2) if y[0]+y[1] == x])

get_sum_pair(range(1, 11))

#10. Find all possible substrings

def get_all_substring(s):
    sub_str_list = []
    for x in range(0, len(s)+1):
        for y in range(x+1, len(s)+1):
            sub_str_list.append(s[x:y])
    return sub_str_list

print(get_all_substring('abcd'))

#11. Find all string combinations

def get_string_combinations(s):
    combo_list = []
    combo_list.append(s)
    for x in range(1, len(s)+1):
        combo_list.extend(["".join(x) for x in combinations(s, len(s)-x)])
    combo_list.pop()
    return combo_list

print(get_string_combinations('abcd'))

#12. String permutations

def get_string_permutations(s):
    return ["".join(x) for x in permutations(s, len(s))]

print(get_string_permutations('abcd'))

#13. String anagram

def is_string_anagram(s1, s2):
    if s1 in ["".join(x) for x in permutations(s2, len(s2))]:
        return True
    return False

print(is_string_anagram('abc', 'cba'))
print(is_string_anagram('abc', 'aabc'))

#14. First repeated and non-repeated character in a string

def get_first_repeated_non_repeated_char(s):
    return [x for x in s if s.count(x) > 1][0], [x for x in s if s.count(x) == 1][0]

print(get_first_repeated_non_repeated_char('aabbccddeefghii'))

#15. Remove duplicates from a list
print(list(set(['aaa','bbb','aaa'])))

#16. Word counter in a string/line
def get_word_counter(s):
    lst = s.split(" ")
    unique_lst = set(lst)

    for x in unique_lst:
        print(x, lst.count(x))
from collections import Counter
print(Counter("abcdefghiabcdefabckkk"))
get_word_counter("abc def ghi abc def abc kkk")

#17. Matching characters in two strings
def get_matching_chars(s1, s2):
    return set(s1) & set(s2)

print(get_matching_chars('abcdef','def'))

#.18. Check string contains special characters

import re
def is_string_has_special_characters(s):
    regex = re.compile('@#')
    if regex.search(s) == None:
        return True
    else:
        return False

print(is_string_has_special_characters('abcdefghi'))
print(is_string_has_special_characters('abcdefghi#'))

#19. Class
class Employee(object):
    def __init__(self, name, id, sal):
        self.name = name
        self.id = id
        self.sal = sal

    def get_emp_name(self):
        return self.name

class Manager(Employee):
    def __init__(self, name, id, sal, mgr_id):
        Employee.__init__(self, name, id, sal)
        self.mgr_id = mgr_id

    def get_mgr_details(self):
        return self.id, self.mgr_id

obj = Manager('abc', 123, 15000, 456)
print(obj.get_mgr_details())



'''
Simple moving average: 1,2,3,4,5,6,7,8,9,10
[(1+2+3)/3, (2+3+4)/3, ...(8+9+10)/3]
[[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10]]
'''

def calc_simple_moving_avg(lst, size):
    return [sum(lst[x-1:x+size-1])/size for x in lst if x<=len(lst)-size+1]

print(calc_simple_moving_avg(list(range(1,11)), 3))

'''
Nth fab number
'''
def fab_num(num):
    cnt = 1
    a,b = 1,1
    while cnt < num:
        a,b=b,a+b
        cnt = cnt +1
    return a

print(fab_num(5))

'''
For the years 1901 to 2000, count the total number of Sundays that fell on the first of a month.  
'''

from datetime import date

def count_sundays_on_first_day_of_a_month(date_start, date_end):
    sunday_count = 0
    for x in range(date_start.toordinal(), date_end.toordinal()):
        xd = date.fromordinal(x)
        if xd.day == 1 and xd.weekday()==6:
            sunday_count=sunday_count+1
    return sunday_count

print(count_sundays_on_first_day_of_a_month(date(1900, 1, 1), date(2000, 12, 31)))

'''
Roman equivalent fro 1 to 100
[I II III. IV. V VI VII VIII. IX. X]
[1,4,5,9,10] in reverse order, either a list of tuples or OrderedDict from collections
'''
def convert_to_roman(num):
    roman_list=[(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
    roman = ""
    while num > 0:
        for i, r in roman_list:
            if num >= i:
                roman = roman + r
                num = num - i
    return roman

print(convert_to_roman(11))

'''
How would you write a program to move inside a square spiral? 
Start at the upper left corner of the square and walk its edges clockwise.
Just before re-approaching the upper left corner, spiral into the square instead, 
ultimately arriving at the center of the square.
i.e. print a matrix in spiral form
'''

import numpy as np
arr = np.arange(1, 17).reshape(4, 4)

#zip(*arr) -- list(zip(*arr)) -- list(zip(*arr))[::-1]
def rotate_matrix(arr):
    return list(zip(*arr))[::-1]


def print_matrix_in_spiral_order(mat):
    top = left = 0
    bottom = len(mat)-1
    right = len(mat[0])-1

    while True:
        if left > right:
            break

        #print top
        for x in range(left, right+1):
            print(mat[top][x], end=' ')
        top = top + 1

        if top > bottom:
            break

        #print right
        for x in range(top, bottom + 1):
            print(mat[x][right], end=' ')
        right = right - 1

        if left > right:
            break

        #print bottom
        for x in range(right, left - 1, -1):
            print(mat[bottom][x], end=' ')
        bottom = bottom - 1

        if top > bottom:
            break

        #print left
        for x in range(bottom, top - 1, - 1):
            print(mat[x][left], end=' ')
        left = left + 1

mat=np.arange(1,26).reshape(5,5)
print(mat)
print(print_matrix_in_spiral_order(mat))


'''
2) Order a list of words appearing in a file by number of letters but maintain original order ("stable sorting") of words with same length
3) Implement a stack class with methods to do some specific operations mentioned in the question.

1) Given a series of prices, find the one buy/sell trade pair which gives the maximum profit
2) Modification of 1. For the same prices, find the maximum profit possible with any number of buy/sell allowed (at each step/price, you can buy, sell or do nothing, no short sell allowed)  
'''

'''
Maximum difference between two elements such that larger element appears after the smaller number:
example: 2 and 10.
'''

def find_max_profit(lst):
    lowest_val=lst[0]
    profit=0

    print("initial lowest:", lowest_val)
    print("initial profit:", profit)
    for x in range(1, len(lst)):
        print("x, val:", x, lst[x])
        if lst[x] >= lowest_val:
            print("profit=", profit, "+", (lst[x] - lowest_val))
            profit = profit + (lst[x] - lowest_val)
            print("profit is = ", profit)
            lowest_val = lst[x]
        else:
            lowest_val = lst[x]
            print("lowest_val:", lowest_val)
    print("--------")
    print("lowest_val:", lowest_val)
    print("profit:", profit)


print("------")
lst = [45, 24, 35, 31, 40, 38, 11]
print("lst:", lst)
find_max_profit(lst)


#Check python list for monotonicity (strictly increasing or strictly decreasing)

def is_strictly_increasing(zip_lst):
    return all(x>=y for x,y in zip_lst)

def is_strictly_decreasing(zip_lst):
    return all(x<=y for x,y in zip_lst)

def is_monotonic(lst):
    zip_list = zip(lst, lst[1:])
    if is_strictly_decreasing(zip_list) and is_strictly_increasing(zip_list):
        return True
    else:
        return False

lst = [1, 3, 5, 7, 9, 9.5, 11]
lst1 = [1, 3, 2, 7, 9, 9.5, 11]
lst2 = [1, 3, 5, 7, 9, 9.5, 11, 11]
print(lst)
print(is_monotonic(lst2))

'''
merge overlapping intervals:
(1,3),(3,5),(5,8) -- (1,8)
'''

def merge_overlap(lst):
    lst.sort()
    for n,t in enumerate(lst[1:]):
        prev_max= lst[n][1]
        if prev_max>=t[0] and prev_max<=t[0]:
            continue
    return (lst[0][0], lst[n+1][1])


lst = [(1,3),(3,5),(0,12),(5,9)]
print(merge_overlap(lst))
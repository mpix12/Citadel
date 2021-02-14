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


#Check python list for monotonicity

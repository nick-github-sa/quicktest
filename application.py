# class Robot:
#     def introduce_self(self):
#         print("My name is " + self.name)
#         print("I am the color " + self.color)
#         print("I weigh " + str(self.weight))

# r1 = Robot()
# r1.name = "Tom"
# r1.color = "Red"
# r1.weight = 30

# r2 = Robot()
# r2.name = "Tom"
# r2.color = "Red"
# r2.weight = 30

# print(r1.introduce_self())
# print(r2.introduce_self())
        
# '''
# Question 10
# Write a function def add_commas(numbers) that will add commas to an integer and return it as a string.
# For example add_commas(1000000) will return 1,000,000 Do it first without using string fomratting
# or f strings.
# Are you sure?
# '''
# new_number = 1000000000

# def add_commas(number):

#     str_number = str(number)

#     str_number = str_number[::-1]
#     comma = ','
#     new_str = ''
#     for i, num in enumerate(str_number):
#         if i != 0 and (i % 3) == 0:
#             new_str = new_str + comma
#         new_str = new_str + num

#     return new_str[::-1]

# print(add_commas(new_number))

# i = 3
# if i != 0 and (i % 3) == 0:
#     print("True")
# else:
#     print("False")

# test_number = "67890"

# for i, num in enumerate(test_number):
#     print(i, num)

# '''
# Question 11
# Write a function that will convert an integer into binary.

# '''
# number = 12345

# def integer_binary(integer):
#     return f'The integer number {integer} is {integer:08b}'

# print(integer_binary(number))

# '''
# Question 12
# Write a function that calculates the sum of all integers up to n. Use the iterative method
# and the formula and compare the results. (sum of n integers given by S = (n(n+1))/2)

# '''
# from numpy import append


# number = 20

# def check_sums(number):
#     sum_1 = 0
#     for i,v in enumerate(range(number+1)):
#         sum_1 = sum_1 + v
#     sum_2 = (number * (number + 1))/2

#     return sum_1, sum_2

# print(check_sums(test))

# sum_1 = 0
# for i,v in enumerate(range(number+1)):
#         sum_1 = sum_1 + v
#         print(i,v)
# print(sum_1)

# b = 0
# for i in range(21):
#     b = b + i
# print(b)


# '''
# Question 13
# Go back over the TwoSum problem we covered earlier in the course. Ensure you understand it.

# '''

# list_new = [2,5,3,7,4]

# d = {}

# for i in range(len(list_new)):
#     d[i] = list_new[i]

# print(d)

# def two_sum(nums, target):
#     d = {}

#     for i in range(len(nums)):
#         if target - nums[i] in d:
#             print(d)
#             return [d[target-nums[i]],i]

#         d[nums[i]] = i

#     return -1

# print(two_sum(list_new, 10))



# from turtle import clear
# from urllib import response
# import requests

# URL = "https://www.py4e.com/code3/words.txt"

# response = requests.get(URL)
# open("words.txt", "wb").write(response.content)


# def makedict():

#     with open('words.txt') as file:
#         words = [i.strip().lower() for i in file.read().split()]
#         dictionary = dict(zip(words[:-1], words[1:])) 
#         return 'boring' in dictionary

# print(makedict())


# list_new = [2,5,3,7,4]


# def two_sums(list_add,target):
#     dictionary = {}
#     for i in range(len(list_add)):
#         if target - list_add[i] in dictionary:
#             print(dictionary)
#             return [dictionary[target-list_add[i]],i]
        
#         dictionary[list_add[i]] = i

#     return -1

# print(two_sums(list_new,10))

# test = [2,3,4,5,6,7,88,6,5,44]

# def linear_search(item, my_list):
#     i = 0
#     found = False
    
#     while i < len(my_list) and found == False:
#         print(i)
#         if my_list[i] == item:
#             found = True

#         else:
#             i += 1

#     return found

# print(linear_search(7, test))





# numbers = [2,5,3,2,1,2,3,4,1,2,3,2,5]


# def two_sum(new_num, target):

#     dictionary = {}

#     for i in range(len(new_num)):
#         if target - new_num[i] in dictionary:
#             return [dictionary[target - new_num[i]],i]
#         dictionary[new_num[i]] = i

#     return -1

# print(two_sum(numbers, 10))


# print(two_sum(numbers, 10))


# numbers = [2,3,6,7]


# def two_sum(target, new_nums):
#     tionary = {}
#     for i in range(len(new_nums)):
#         if target - new_nums[i] in tionary:
#             return [tionary[target - new_nums[i]],i]
        
#         tionary[new_nums[i]] = i
    
#     return -1

# print(two_sum(10, numbers))

# '''
# Question 15
# Write a function that takes a positive integer n and converts it into hours and minutes.
# 45 would return 0h:45mins 135 would return 2h:15mins

# '''
# import time

# n = 45

# print(time.strftime('%H:%M:%S', time.gmtime(n)))

# print(f'{time.gmtime(n).tm_min}h:{time.gmtime(n).tm_sec}mins')

# def time_check(n_new):
#     hours = n_new // 60
#     mins = n_new % 60
#     return f'{str(hours)}h:{str(mins)}mins'

# print(time_check(n))

# '''
# Question 16
# Write a function to determine whether all numbers in a list are unique.

# '''
# test_list = [2,3,4,5,6,7,8,8]


# def check_list(numbers):
#     test_num = set(numbers)
#     if len(test_num) == len(numbers):
#         return True
#     else:
#         return False

# print(check_list(test_list))

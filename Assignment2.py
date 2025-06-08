# #Check a number is prime or not using function
# # num = 10
# # def func(num):
# #     count = 0
# #     for i in range(1,(num//2+1)):
# #         if num % i == 0:
# #             count+=1
# #     print(count)
# #     if count<=1:
# #         print(num," is prime")
# #     else:
# #         print(num,"is not prime")
# # func(num)

# #function to calculate area of a rectangle
# # def cal_area(height,width):
# #     area = height*width
# #     return area
# # width= int(input("Enter width of rectangle:"))
# # height= int(input("Enter height of rectangle:"))
# # print("Area of the rectangle with height",height,"and width",width,"is :",cal_area(height,width))

# #function to find maximum of three numbers
# # def max_cal(a,b,c):
# #     if a>b and a>c:
# #         print(a,"is maximum")
# #     elif b>a and b>c:
# #         print(b,"is maximum")
# #     else:
# #         print(c,"is maximum")
# # max_cal(1,2,3)

# #function to reverse a string
# def reverse(string):
#     for i in range(len(string)-1,-1,-1):
#         print(string[i],end="")
# string = str(input("Enter a string:"))
# reverse(string)

#Count number of vowels in a string using function
# def vowels(string):
#     count=0
#     for i in string:
#         if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
#             count += 1
#     return count
# number_of_vowels=vowels("Arpita Sahoo is a student")
# print(number_of_vowels)

#Function to check string is palindrome or not
# def reverse(string):
#     string_new = ""  
#     for i in range(len(string) - 1, -1, -1):
#         string_new += string[i]
#     return string_new
# def is_palindrome(string):
#     reversed_str = reverse(string)
#     if string == reversed_str:
#         print("Palindrome")
#     else:
#         print("Not a palindrome")
# is_palindrome("madam")
# is_palindrome("Arpita")

#function to calculate sum of a list of numbers
# def sum(my_list):
#     sum=0
#     for i in my_list:
#         sum+=i
#     return sum
# my_list=[10,20,30,21,35]
# print(sum(my_list))

#Create a function to print fibonacci
# def fibonacci(n):
#     a=0
#     b=1
#     print(a,b,end=" ")
#     for i in range(n):
#         c = a+b
#         a=b
#         b=c
#         print(c,end=" ")
# fibonacci(5)

#function to convert celsius to farenheite
# def cal_far(celsius):
#     far = celsius * 9//5 + 32
#     return far
# print(cal_far(34.5))

#function to find minimum in a list
# def minimum(my_list):
#     min = my_list[0]
#     for i in my_list:
#         if i < min:
#             min = i
#     return min
# my_list=[20,30,10,3,100]
# print("Minimum number in the list is",minimum(my_list))

# #functiom to find frequency of a character in a string
# def char_frequency(string, char):
#     count = 0
#     for c in string:
#         if c == char:
#             count += 1
#     return count
# text = "hello world"
# character = "o"
# print(f"Frequency of '{character}' in '{text}':", char_frequency(text, character))

#function to check a number is perfect number or not
#def perfect_num(number):
#     sum=0
#     for i in range(1,number):
#         if (number%i)==0:
#             sum+=i
#     if sum==number:
#         return sum
#     else:
#         return 
# print(perfect_num(496))

#function to find sum of digits of A number
# def sum_of_digits(number):
#     sum = 0
#     while number>0:
#         n = number%10
#         sum = sum + n
#         number = number // 10
#     return sum
# print(sum_of_digits(9871))

#function that takes a string and returns a dictionary of character frequency
# def takes_string(string):
#     freq={}
#     for i in string:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     return freq
# print(takes_string("Hellow world"))

#function that returns average of a list of numbers
# def avg_num(my_list):
#     sum = 0
#     for i in my_list:
#         sum+=i
#     average = sum/len(my_list)
#     return average
# my_list=[1,2,3,4,5]
# print(avg_num(my_list))

#function that accepts number and print its multiplication table'
# def mul_table(number):
#     for i in range(1,11):
#         print(number, "*",i,"=",number*i)
# mul_table(5)

#function that accepts a list and returns it in reverse
# def rev_list(my_list):
#     new_list = []
#     for i in range(len(my_list) - 1, -1, -1):
#         new_list.append(my_list[i])
#     return new_list

# print(rev_list([2, 3, 4, 5, 6, 7]))

#18-function to find second largest number in a list
# def second_largest(nums):
#     unique_nums = list(set(nums))
#     if len(unique_nums) < 2:
#         return None
#     unique_nums.sort(reverse=True)
#     return unique_nums[1]
# print(second_largest([1,2,6,8,3]))

#19-function that accepts list of integers and returns the even ones
# def even_nums(my_list):
#     for i in my_list:
#         if i%2==0:
#             print(i)
# even_nums([2,3,4,5,6,7,8,9,0])

#20-function to check if all characters in a string are unique or not
# def uniqueness(string):
#     seen = []
#     repeated = []

#     for char in string:
#         if char in seen:
#             if char not in repeated:
#                 repeated.append(char)
#         else:
#             seen.append(char)

#     for char in repeated:
#         print(char, "is repeated")
# uniqueness("Arpita sahoo")

#21-function to calculate gcd of two numbers
# def gcd(num1,num2):
#     while num2!=0:
#         num1,num2 = num2, num1%num2
#     return num1
# print(gcd(48,18))

#22-function to find lcm of two numbers
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# def lcm(a, b):
#     return abs(a * b) // gcd(a, b)
# print(lcm(8,9))

#23-create func to remove duplicates from list
# def rem_dup(my_list):
#     uni_list=[]
#     for i in my_list:
#         if i not in uni_list:
#             uni_list.append(i)
#     return uni_list
# print(rem_dup([1,2,3,4,5,6,2,3,10]))
        
#24-recursive func to compute factorial
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1  
#     return n * factorial(n - 1)

# print(factorial(5)) 

#25-func to check armstrong
# def is_armstrong(num):
#     original_num = num
#     sum = 0
#     digits = 0

#     temp = num
#     while temp > 0:
#         digits += 1
#         temp = temp // 10

#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** digits
#         temp = temp // 10

#     if sum == original_num:
#         return True
#     else:
#         return False
# print(is_armstrong(153))   
# print(is_armstrong(123))   

#26-func to return prime numbers upto n
# def return_prime(n):
#     for i in range(2,n):
#         is_prime =True
#         for m in range(2,(i//2)+1):
#             if i%m==0:
#                 is_prime = False
#         if is_prime:
#             print(i)
# return_prime(10)

#27-func to accept a string and return the longest word
def return_longest_word(string1):
    words = string1.split() 
    longest_word = ""
    
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    
    print("The longest word is:", longest_word)
    print("Length:", len(longest_word))
return_longest_word("Arpita Sahoo is a student")

# 28 - Function to compute the power of a number
def power(base, exp):
    return base ** exp

# 29 - Function that flattens a nested list
def flatten(nested_list):
    result = []
    for i in nested_list:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result

# 30 - Function to check if a list is sorted or not
def is_sorted(lst):
    return lst == sorted(lst)

# 31 - Function to merge two sorted lists
def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)

# 32 - Function to find most frequent element in the list
def most_frequent(lst):
    return max(set(lst), key=lst.count)

# 33 - Function to return the median of the list
def find_median(lst):
    lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    return (lst[mid] if n % 2 != 0 else (lst[mid - 1] + lst[mid]) / 2)

# 34 - Function to find intersection of two lists
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

# 35 - Function to accept variable number of arguments and return product
def product(*args):
    result = 1
    for num in args:
        result *= num
    return result

# 36 - Function to return list of tuple(element , index) from a list
def element_index_tuples(lst):
    return list(enumerate(lst))

# 37 - Function to accept string and return the dictionary of word count
def word_count(sentence):
    words = sentence.split()
    return {word: words.count(word) for word in set(words)}

# 38 - Function to check if a sentence is pangram
def is_pangram(sentence):
    return set("abcdefghijklmnopqrstuvwxyz") <= set(sentence.lower())

# 39 - Function to accept a list and a value and return the index of the value
def find_index(lst, value):
    return lst.index(value) if value in lst else -1

# 40 - Function to calculate the number of uppercase and lowercase letters in a string
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return {"uppercase": upper, "lowercase": lower}

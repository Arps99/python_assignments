# #Numbers from 1 to 10
# for i in range(1,11):
#  print(i)

# #Even numbers from 1 to 20
# for i in range(1,21):
#     if i%2 == 0:
#         print(i)

# #check num is positive or negative or zero
# num = int(input("Enter a number"))
# if num==0:
#     print("It's a zero")
# elif num<0:
#     print("It's negative")
# else:
#     print("It's positive")

# #Addition
# num1 = 10
# num2 = 30
# print(num1+num2)

# #multiplication table of  a number
# num = int(input("Enter a number"))
# for i in range(1,11):
#     print(num ,"*" , i ,"=",num*i)

# #find largest among two numbers
# num1 = 20
# num2 = 3
# if num1>num2:
#     print(num1," is greater")
# else:
#     print(num2," is greater")

# #while loop to print numbers from 5 to 1
# num = 5
# while num>=1:
#     print(num)
#     num-=1

# #print all characters in  a string
# string1 = str(input("Enter a string : "))
# for i in range(0,len(string1)):
#     print(string1[i])

# #logical operator to check a number is between 10  and 50
# num1 = 400
# if num1>10 and num1<50:
#     print("It's between 10 and 50")
# else:
#     print("It's not in between 10 and 50")

# #sum of first 10 natural numbers
# sum = 0
# for i in range(0,11):
#     sum = sum + i
# print(sum)

# #print odd or even numbers for 1 to 10
# for i in range(0,11):
#     if i%2==0:
#         print(i," is an even number")
#     else:
#         print(i," is an odd number") 

# #use break to stop loop when number is 5
# for i in range(0,10):
#     if i==5:
#         break
#     print(i)

# #print 1 to 10 and use continue to stop printing 5
# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)

# #print all elements in a list using loop
# my_list = [10, 20, 30, 40, 50]

# for item in my_list:
#     print(item)

# #check a number is divisible by both 3 and 5 or not
# num1 = 40
# if num1%5==0 and num1%3==0:
#     print(num1,"is divisible by both 3 and 5")
# else:
#     print(num1,"is not divisible by both")

# #square of numbers from 1 to 5
# for i in range(1,6):
#     print(i,"'s square is ",i*i)

# #ASCII values of characters in a string
# string1 = str(input("Enter a string : "))
# for i in range(0,len(string1)):
#     print(string1[i],"'s ASCII value is ",ord(string1[i]))

# #countdown from 10 to 1 using while
# i = 10
# while i>=1:
#     print(i)
#     i-=1

# #check a number is divisible by 2 or 3
# num1 = 27
# if num1%2==0 or num1%3==0:
#     print(num1,"is divisible by 2 or 3")
# else:
#     print(num1,"is not divisible by 2 0r 3")

# #print sum of digits of a number
# num1 = 23457
# sum = 0
# while num1>1:
#     temp = num1%10
#     sum = sum +temp
#     num1 = num1//10
# print(int(sum))

# #swap two numbers using third variable
# a = 10
# b = 20
# print("Before swapping")
# print("A is ",a)
# print("B is ",b)
# c=a
# a=b
# b=c
# print("After swapping")
# print("A is ",a)
# print("B is ",b)

# #numbers from 1 to 100 that are divisible by7
# for i in range(1,100):
#     if i%7==0:
#         print(i,"is divisible by 7")

# #Find factorial of a number
# def factorial(num):
#     if num==1:
#         return 1
#     else:
#         return num * factorial(num-1)
# print(factorial(5))

# #count vowels in a string
# string1 = str(input("Enter a string:"))
# count = 0
# for i in string1:
#     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
#         count += 1
# print(count)

# #Reverse a number using loop
# num1 = 2457
# rev =0
# while num1>0:
#     temp = num1%10
#     rev = rev *10 +temp
#     num1 = num1//10
# print(rev)

# #Find the maximum in the list
# my_list = [100,200,3000,40000,50]
# max = my_list[0]
# for i in my_list:
#     if i>max:
#         max=i
# print(max,"is maximum in the list")

# #check a number is prime or not using loop
# num = 10
# count = 0
# for i in range(1,(num//2+1)):
#     if num % i == 0:
#         count+=1
# print(count)
# if count<=1:
#     print(num," is prime")
# else:
#     print(num,"is not prime")

# #sum of even numbers in a list
# my_list = [23,1,22,30,2]
# sum =0
# for i in my_list:
#     if i%2==0:
#         sum+=i
# print(sum)

# #print number pattern using nested loop
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print(" ")
    
#count frequency of digits in a number
# num =1223334444
# digit_count = [0]*10
# while num>0:
#     digit = num %10
#     digit_count[digit]+=1
#     num = num//10
# for i in range(10):
#     if digit_count[i]>0:
#         print("Digit",i,"appears",digit_count[i],"times.")

#GCD of 2 numbers using loop
# num1=75
# num2=25
# for i in range(1,min(num1,num2)+1):
#     if num1%i==0 and num2%i==0:
#         GCD=i
# print(GCD)

#check if a number is palindrome or not
# Num1 = int(input("Enter a number:"))
# temp = Num1
# rev = 0
# while Num1>0:
#     digit = Num1%10
#     rev = rev *10 + digit
#     Num1=Num1//10
# if temp==rev:
#     print("Palindrome!")
# else:
#     print("Not a palindrome")

#Count words in a sentence
# string = str(input("Enter a string : "))
# count = 1
# for i in string:
#     if i ==" ":
#         count+=1
# print("Number of words is:",count)

#find common elements in 2 lists
# my_list = [20,30,21,10,50]
# your_list=[21,20,30,11,80]
# for i in my_list:
#     for j in your_list:
#         if i==j:
#             print(i,"is common in both the lists.")

#use elif to grade students based on score
# score = int(input("Enter score :"))
# if score>=90:
#     print("Grade A1")
# elif score>=80 and score <90:
#     print("Grade A2")
# elif score >=70 and score<80:
#     print("Grade B1")
# elif score>=60 and score<70:
#     print("Grade B2")
# elif score>=50 and score<60:
#     print("Grade C1")
# else:
#     print("You failed")

#print a right angled triangle using *
# for i in range(1,6):
#     print("*"*i)

#check a year is leap or not
# year = int(input("Enter an year to check :"))
# if year%4==0 and year%100!=0 or year%400==0:
#     print("Leap year")
# else:
#     print("Not a leap year")

#print fibonacci using loop
# a=0
# b=1
# print(a,b,end=" ")
# for i in range(10):
#     c = a+b
#     a=b
#     b=c
#     print(c,end=" ")

#count uppercase and lowercase letters in a string
# string = str(input("Enter a string:"))
# uppercase,lowercase=0,0
# for i in string:
#     if ord(i)>=65 and ord(i)<=90:
#         uppercase+=1
#     elif ord(i)>=97 and ord(i)<=122:
#         lowercase+=1
# print("Number of uppercase letters :",uppercase)
# print("Number of lowercase letters:",lowercase)

#print numbers from 100 to 1 using loop
# num = 100
# while num>=1:
#     print(num)
#     num-=1
#Question: What type of loop should we use?
#You need to write a loop that takes the numbers in a given list named num_list:
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

#Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together. If there are more than 5 odd numbers, you should stop at the fifth. If there are fewer than 5 odd numbers, add all of the odd numbers.

#Would you use a while or a for loop to write this code?
''' I am using a for loop'''


## Please use this space to test and run your code


odd_val =[]
for i in num_list:
    if i % 2 != 0:
        #print(i)
        odd_val.append(i)

print (odd_val)

final = sum(odd_val[:5])

print (f'the total summation of first 5 odd numbers is {final}')
        





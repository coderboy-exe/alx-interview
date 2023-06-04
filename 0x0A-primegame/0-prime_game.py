#!/usr/bin/python3
""" Prime game algo """


#def isWinner(x, nums):
    #arr = []

    #nimber = 0  # or grundy number  
    #for i in nums:
    #    nimber ^= nums[i % len(nums)];

   # return "Ben" if nimber > 0 else "Maria"

def calculate_highest_power_of_two(n):
    power_of_two = n
    while power_of_two & (power_of_two - 1) != 0:
        power_of_two = power_of_two & (power_of_two - 1)
    return power_of_two

def isWinner(x, nums):
    nimber = 0  # or grundy number

    for n in nums:
        if n % 2 == 0:
            nimber ^= 0
        else:
            highest_power_of_two = calculate_highest_power_of_two(n)
            nimber ^= highest_power_of_two

    return "Ben" if nimber > 0 else "Maria"


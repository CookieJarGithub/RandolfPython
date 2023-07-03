"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible with no remainder by all of the numbers from 1 to 20?
"""

def isevenly_divisible(num):
    if num == 0:
        return False
    
    for factor in range(1, 21):
        if num % factor != 0:
            return False
    
    return True

# brute force lmao
num = 0
while num < 1000000000:
    if isevenly_divisible(num):
        break
    num += 2520

print(num)
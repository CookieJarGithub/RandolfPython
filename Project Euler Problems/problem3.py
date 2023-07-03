"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

prime_factors = []

def lowest_prime_factor(num):
    curr_factor = 2

    # divides number by a factor starting from 2 going up.
    # function gets the lowest prime factor at each iteration
    while num % curr_factor != 0:
        curr_factor += 1
        if curr_factor == num:
            prime_factors.append(curr_factor)
            break
    else:
        prime_factors.append(curr_factor)
        lowest_prime_factor(num / curr_factor)

lowest_prime_factor(600851475143)
print(max(prime_factors))
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.</p>
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def list_digits(num):
    all_but_last, last = num, 0
    digits = []

    if num < 10:
        digits.append(num)
    else:
        # runs through every digit appending it to digits[] every time 
        while all_but_last >= 10:
            last = all_but_last % 10
            all_but_last = all_but_last // 10
            digits.insert(0, last)
        digits.insert(0, all_but_last)
    
    return digits

def ispalindrome(num):
    # checks if digits of a number is equal to digits of that number reversed
    return list_digits(num) == list(reversed(list_digits(num)))

print(ispalindrome(903))
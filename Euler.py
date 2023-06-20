1)
result = sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])
print(result)
2)
a, b = 1, 2
result = 0
while a <= 4000000:
    if a % 2 == 0:
        result += a
    a, b = b, a + b
print(result)
3)
import math

def largest_prime_factor(n):
    while n % 2 == 0:
        n = n // 2
    if n == 1:
        return 2
    factor = 3
    while factor <= math.isqrt(n):
        if n % factor == 0:
            n = n // factor
        else:
            factor += 2
    return n

result = largest_prime_factor(600851475143)
print(result)
4)
result = max(i * j for i in range(100, 1000) for j in range(100, 1000) if str(i * j) == str(i * j)[::-1])
print(result)
5)
from math import gcd
from functools import reduce

def lcm(a, b):
    return a * b // gcd(a, b)

result = reduce(lcm, range(1, 21))
print(result)
6)
n = 100
sum_of_squares = sum(i ** 2 for i in range(1, n + 1))
square_of_sum = sum(range(1, n + 1)) ** 2
result = square_of_sum - sum_of_squares
print(result)
7)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

count = 0
num = 2
while count < 10001:
    if is_prime(num):
        count += 1
    num += 1
result = num - 1
print(result)
8)
num_str = """<insert 1000-digit number here>"""
adjacent_digits = 13
result = 0
for i in range(len(num_str) - adjacent_digits):
    product = 1
    for j in range(adjacent_digits):
        product *= int(num_str[i + j])
    result = max(result, product)
print(result)
9)
for a in range(1, 1000):
    for b in range(a, 1000):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2:
            result = a * b * c
            break
print(result)
10)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

result = sum(i for i in range(2, 2000000) if is_prime(i))
print(result)
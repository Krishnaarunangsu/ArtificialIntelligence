#  Write a program to generate a list of all prime numbers less than 20.
# Before starting it is important to note what a prime number is.
# A prime number has to be a positive integer
# Divisible by exactly 2 integers (1 and itself)
# 1 is not a prime number


# Initialize a list
primes: list = list()
for possiblePrime in range(2, 21):

    # Assume number is prime until shown it is not.
    isPrime = True
    for num in range(2, possiblePrime):
        if possiblePrime % num == 0:
            isPrime = False

    if isPrime:
        primes.append(possiblePrime)

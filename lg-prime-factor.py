# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# function to return all the prime factors of a positive integer
def prime_factors(n):
    factors = list()
    divider = 2

    while n > 1:
        while n % divider == 0:
            factors.append(divider)
            n /= divider
        divider = divider + 1

    return factors


pfs = prime_factors(600851475143)
print pfs
lpfs = max(pfs)
print lpfs

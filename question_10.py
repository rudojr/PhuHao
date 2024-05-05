def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def unique_prime_factors_product(n):
    factors = prime_factors(n)
    unique_factors = set(factors)
    product = 1
    for factor in unique_factors:
        product *= factor
    return product

number = int(input("Input"))

result = unique_prime_factors_product(number)

print("Output:", result)

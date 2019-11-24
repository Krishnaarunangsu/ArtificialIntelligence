def nonprimes(k):
    print(k)
    if k > 0:
        yield 1
    primes = set()
    n = 2
    print(f'K:{k}')
    while k > 1:
        for prime in primes:
            print(f'Prime:{prime}')
            if n % prime == 0:
                yield n
                k -= 1
                break
        else:
            primes.add(n)
        n += 1


for n in nonprimes(1):
    print(n)


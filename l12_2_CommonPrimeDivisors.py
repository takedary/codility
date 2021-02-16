from functools import reduce
import math


def gcd(a, b):
  if a < b:
    a, b = b, a

  if a % b == 0:
    return b
  return gcd(b, a % b)

def has_super_primefactors(a, b):
  """
  return True if prime factor set of a is a superset of that of b
  e.g.
    True if
      a = 30 = 2^1 x 3^1 x 5^1 and
      b = 18 = 2^1 x 3^2
    True if
      a = 18 = 2^1 x 3^2 and
      b = 24 = 2^3 x 3^1
    False if
      a = 27 = 3^3 and
      b = 24 = 2^3 x 3^1
  """
  #print('has_super_primefactors', f'{(a, b) = }')
  if a % b == 0:
    return True

  g = gcd(a, b)
  if g == 1:
    return False
  return has_super_primefactors(g, b//g)

def solution(A, B):
  def the_same(a, b):
    #print('the_same', f'{(a, b) = }')
    if a == b:
      return True
    if min(a, b) == 1:
      return False

    g = gcd(a, b)
    if g == 1:
      return False
    return has_super_primefactors(g, a//g) and has_super_primefactors(g, b//g)

  return sum(the_same(a, b) for a, b in zip(A, B))

def another_solution(A, B):
  return sum(has_super_primefactors(a, b) and has_super_primefactors(b, a)
             for a, b in zip(A, B))


def slow_solution(A, B):
  def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
      if n % i == 0:
        return False
    return True

  def arrayf(n):
    f = [0] * (n + 1)
    for i in range(2, int(math.sqrt(n)) + 1):
      if f[i] == 0:
        for j in range(i * i, n + 1, i):
          if f[j] == 0:
            f[j] = i
    return f

  def dictf(n):
    f = {}
    for i in range(2, int(math.sqrt(n)) + 1):
      if i in f:
        continue
      for j in range(i * i, n + 1, i):
        _ = f.setdefault(j, i)
    return f

  maxn = max(A + B)
  f = dictf(maxn)

  def factorize(n):
    primefactors = set()
    if n == 1:
      return primefactors
    while n in f:
      primefactors.add(f[n])
      n //= f[n]
    primefactors.add(n)
    return primefactors

  def the_same(a, b):
    """
    1. factorize smaller one
    2. another one /= prod of the factor set of 1
    3. factorize 2
    4. return result of 3 is in res 1
    """
    a, b = (a, b) if a > b else (b, a)
    #print(f'{(a, b) = }')
    if b == 1:
      return a == 1

    factors_b = factorize(b)
    #print(f'{factors_b = }')
    bb = reduce(lambda x, y: x * y, factors_b)
    if a % bb != 0:
      return False

    remained_factors_a = factorize(a // bb)
    #print(f'{remained_factors_a = }')
    return remained_factors_a.issubset(factors_b)

  return sum(the_same(a, b) for a, b in zip(A, B))


if __name__ == '__main__':
  from random import randrange

  cases = [
      ([15], [75]),
      ([10], [30]),
      ([3], [5]),
      ([126], [36]),
      ([126], [30]),
      ([2, 1, 2], [1, 2, 2]),
      ([2147483647], [2147483646]),
  ]
  for c in cases:
    print('\n', c)
    #print(f'{slow_solution(*c) = }')
    print(f'{solution(*c) = }')
    print(f'{another_solution(*c) = }')
    print(f'{solution1(*c) = }')

  cases = []
  for _ in range(6000):
    Z = randrange(1, 100)
    a = [randrange(1, 100) for _ in range(Z)]
    b = [randrange(1, 100) for _ in range(Z)]
    cases.append((a, b))

  for c in cases:
    if solution(*c) == another_solution(*c) == solution1(*c) == slow_solution(*c):
      continue
    print(f'{c = }')

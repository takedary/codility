def solution(A):
  dp = [A[0]]
  for i, a in enumerate(A[1:], 1):
    dp.append(max(dp[j] for j in range(i-6, i) if j >= 0) + a)
  return dp[-1]


def solution_recur(A):
  dp = {0: A[0]}
  def recur(i):
    try:
      return dp[i]
    except KeyError:
      pass

    dp[i] = max(recur(j) for j in range(i-6, i) if j >= 0) + A[i]
    return dp[i]

  return recur(len(A)-1)


if __name__ == '__main__':
  from random import randrange

  cases = [
      ([1, 1],),
      ([1, -2, 0, 9, -1, -2],),
  ]
  for _ in range(5):
    cases.append(([randrange(-5, 5) for _ in range(randrange(2, 14))],))

  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')

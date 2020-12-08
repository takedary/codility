from collections import Counter


def solution(A):
  N = len(A)
  c = Counter(A)
  leader, count = c.most_common(1)[0]
  if 2 * count <= N:
    return 0

  n_els = 0
  count_left = 0
  for i, a in enumerate(A, start=1):
    if a == leader:
      count_left += 1
    if 2 * count_left > i and 2 * (count-count_left) > N - i:
      n_els += 1
  return n_els


if __name__ == '__main__':
  cases = [
      [4, 3, 4, 4, 4, 2],
      [0],
      [0, 1],
      [1, 2, 3, 4, 5]
  ]
  for c in cases:
    print(c, solution(c))

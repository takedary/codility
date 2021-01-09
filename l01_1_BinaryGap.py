def solution(N):
  while N % 2 == 0:
    N >>= 1

  zeros = max_zeros = 0
  while N > 0:
    if N % 2 == 0:
      zeros += 1
    else:
      max_zeros = max(max_zeros, zeros)
      zeros = 0
    N >>= 1

  return max_zeros


def shorter_solution(N):
  return max(len(z) for z in bin(N)[2:].strip('0').split('1'))


if __name__ == '__main__':
  cases = [
      (1,),
      (2,),
      (3,),
      (4,),
      (5,),
      (6,),
      (7,),
      (8,),
      (9,),
      (15,),
      (20,),
      (32,),
      (529,),
      (1041,),
  ]
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
    print(f'{shorter_solution(*c) = }')

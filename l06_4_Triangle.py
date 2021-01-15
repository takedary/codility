def solution(A):
  N = len(A)
  if N < 3:
    return 0

  A.sort()
  return int(any(A[i] + A[i+1] > A[i+2] for i in range(N-2)))

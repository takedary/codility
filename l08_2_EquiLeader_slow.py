from collections import Counter


def solution(A):
  if len(A) == 1:
    return 0

  N = len(A)
  cnt_l, cnt_r = Counter(A[0:1]), Counter(A[1:]) # counter

  cands_l, leader_exists_l = [A[0]], True # candidates

  max_count = cnt_r.most_common(1)[0][1]
  cands_r = [k for k, v in cnt_r.items() if v == max_count]
  leader_exists_r = 2 * max_count > N - 1

  num_el = int(leader_exists_l and leader_exists_r
               and cands_l == cands_r)
  print('l', cands_l, leader_exists_l)
  print('r', cands_r, leader_exists_r)

  for a, size_l, size_r in zip(
      A[1:-1], range(2, N), range(N-2, 0, -1)):
    cnt_l.update([a])
    cnt_r.subtract([a])

    # update leader_l
    if leader_exists_l:
      if (a not in cands_l
          and 2 * cnt_l[cands_l[0]] <= size_l):
        leader_exists_l = False
        if cnt_l[a] == cnt_l[cands_l[0]]:
          cands_l.append(a)
    elif a in cands_l:
      cands_l = [a]
      leader_exists_l = 2 * cnt_l[a] > size_l
    elif cnt_l[a] == cnt_l[cands_l[0]]:
      cands_l.append(a)

    # update leader_r
    if leader_exists_r:
      if (size_r % 2 == 0
          and a in cands_r
          and 2 * cnt_r[a] == size_r):
        leader_exists_r = False

        ss = set()
        for k, v in cnt_r.items():
          if v > 0 and k != a:
            ss.add(k)
          if len(ss) > 1:
            break
        else:
          cands_r.append(ss.pop())
    elif a in cands_r:
      if len(cands_r) == 1:
        cands_r = [k for k, v in cnt_r.items() if v == cnt_r[a]]
      else:
        cands_r.remove(a)
        leader_exists_r = 2 * cnt_r[cands_r[0]] > size_r
    elif len(cands_r) == 1:
      leader_exists_r = 2 * cnt_r[cands_r[0]] > size_r

    print('l', cands_l, leader_exists_l)
    print('r', cands_r, leader_exists_r)
    num_el += (leader_exists_l and leader_exists_r
               and cands_l == cands_r)
  return num_el


if __name__ == '__main__':
  cases = [
      [4, 3, 4, 4, 4, 2],
      [0],
      [0, 1],
      [1, 2, 3, 4, 5]
  ]
  for c in cases:
    print(c, solution(c))

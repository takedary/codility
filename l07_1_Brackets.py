def solution(S):
  pairs = {'(': ')', '{': '}', '[': ']'}

  st = []
  for s in S:
    if s in pairs:
      st.append(s)
    else:
      try:
        top = st.pop()
      except IndexError:
        return 0
      else:
        if pairs[top] != s:
          return 0
  return 0 if st else 1


if __name__ == '__main__':
  cases = [
      ('',),
      ('(',),
      (')',),
      ('()',),
      (')(',),
      ('()(',),
      ('()()',),
      ('[()()]',),
      ('([]{})[()()]',),
  ]
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')

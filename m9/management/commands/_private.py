from itertools import permutations
import numpy as np

A,B,C = 0,1,2

CARPET = (
  ((A,A,C,C),(B,A,C,A),(C,A,C,B),(A,B,A,C),(B,B,A,A),(C,B,A,B),(A,C,B,C),(B,C,B,A),(C,C,B,B)),
  ((A,B,B,C),(B,B,B,A),(C,B,B,B),(A,C,C,C),(B,C,C,A),(C,C,C,B),(A,A,A,C),(B,A,A,A),(C,A,A,B)),
  ((A,C,A,C),(B,C,A,A),(C,C,A,B),(A,A,B,C),(B,A,B,A),(C,A,B,B),(A,B,C,C),(B,B,C,A),(C,B,C,B)),
  ((B,A,C,B),(C,A,C,C),(A,A,C,A),(B,B,A,B),(C,B,A,C),(A,B,A,A),(B,C,B,B),(C,C,B,C),(A,C,B,A)),
  ((B,B,B,B),(C,B,B,C),(A,B,B,A),(B,C,C,B),(C,C,C,C),(A,C,C,A),(B,A,A,B),(C,A,A,C),(A,A,A,A)),
  ((B,C,A,B),(C,C,A,C),(A,C,A,A),(B,A,B,B),(C,A,B,C),(A,A,B,A),(B,B,C,B),(C,B,C,C),(A,B,C,A)),
  ((C,A,C,A),(A,A,C,B),(B,A,C,C),(C,B,A,A),(A,B,A,B),(B,B,A,C),(C,C,B,A),(A,C,B,B),(B,C,B,C)),
  ((C,B,B,A),(A,B,B,B),(B,B,B,C),(C,C,C,A),(A,C,C,B),(B,C,C,C),(C,A,A,A),(A,A,A,B),(B,A,A,C)),
  ((C,C,A,A),(A,C,A,B),(B,C,A,C),(C,A,B,A),(A,A,B,B),(B,A,B,C),(C,B,C,A),(A,B,C,B),(B,B,C,C))
)

def generate(symmetric_only):
  xs = np.array([[int(d) for d in bin(i)[2:].zfill(4)] for i in range(16)])   #x16
  ys = np.array([p for p in permutations((27, 9, 3, 1)) if p[1] > p[2]])      #x12
  return (t for x in xs for y in ys if (t := c_tuple(x, y, symmetric_only)))

def c_tuple(x, y, symmetric_only):
  A = (0, 0, 0, 0)
  B = np.multiply(x+1, y)
  C = np.multiply(2-x, y)
  a = c_array(A, B, C)
  return (tuple(map(tuple, a)), f"B = {B} C = {C}") if not symmetric_only or symmetric(a) else None

def c_array(*t):
  a = np.zeros((9, 9), dtype=int)
  for i in range(9):
    for j in range(9):
      a[i, j] = sum([t[l][k] for k, l in enumerate(CARPET[i][j])])+1
  validate(a) 
  return adjust(a)

def validate(a):
  numbers = list(range(1, a.size+1))
  for row in a: 
    for x in row: 
      numbers.remove(x)
  if numbers:
    raise ValueError(numbers, 'not empty')
  if not magic(a):
    raise ValueError('not magic')

def adjust(a):
  i, j = np.where(a == 41)
  return np.roll(a, (4-i[0], 4-j[0]), axis=(0, 1))

def symmetric(a):
  sums = np.array([a[i, j]+a[8-i, 8-j] for i in range(4) for j in range(4)])
  return np.all(sums == 82)

def magic(a):
  sums = np.array((np.sum(a, axis=0), np.sum(a, axis=1), sum_diag(a), sum_diag(np.fliplr(a))))
  return np.all(sums == 369)

def sum_diag(a):
  return np.array([np.trace(a, -i)+np.trace(a, 9-i) for i in range(9)])

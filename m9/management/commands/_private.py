from itertools import permutations
import numpy as np

A, B, C = 0, 1, 2

CARPET = (
    ((A, A, C, C), (B, A, C, A), (C, A, C, B), (A, B, A, C), (B, B,
     A, A), (C, B, A, B), (A, C, B, C), (B, C, B, A), (C, C, B, B)),
    ((A, B, B, C), (B, B, B, A), (C, B, B, B), (A, C, C, C), (B, C,
     C, A), (C, C, C, B), (A, A, A, C), (B, A, A, A), (C, A, A, B)),
    ((A, C, A, C), (B, C, A, A), (C, C, A, B), (A, A, B, C), (B, A,
     B, A), (C, A, B, B), (A, B, C, C), (B, B, C, A), (C, B, C, B)),
    ((B, A, C, B), (C, A, C, C), (A, A, C, A), (B, B, A, B), (C, B,
     A, C), (A, B, A, A), (B, C, B, B), (C, C, B, C), (A, C, B, A)),
    ((B, B, B, B), (C, B, B, C), (A, B, B, A), (B, C, C, B), (C, C,
     C, C), (A, C, C, A), (B, A, A, B), (C, A, A, C), (A, A, A, A)),
    ((B, C, A, B), (C, C, A, C), (A, C, A, A), (B, A, B, B), (C, A,
     B, C), (A, A, B, A), (B, B, C, B), (C, B, C, C), (A, B, C, A)),
    ((C, A, C, A), (A, A, C, B), (B, A, C, C), (C, B, A, A), (A, B,
     A, B), (B, B, A, C), (C, C, B, A), (A, C, B, B), (B, C, B, C)),
    ((C, B, B, A), (A, B, B, B), (B, B, B, C), (C, C, C, A), (A, C,
     C, B), (B, C, C, C), (C, A, A, A), (A, A, A, B), (B, A, A, C)),
    ((C, C, A, A), (A, C, A, B), (B, C, A, C), (C, A, B, A), (A, A,
     B, B), (B, A, B, C), (C, B, C, A), (A, B, C, B), (B, B, C, C))
)


def generate(*, s):
    xs = np.array([[int(j) for j in np.binary_repr(i, 4)] for i in range(16)])
    ys = [p for p in permutations((27, 9, 3, 1)) if p[1] > p[2]]
    return (d for x in xs for y in ys
            if (d := data((0,)*4, (x+1)*y, (2-x)*y, s=s)))


def data(*t, s):
    a = array(*t)
    if s and not symmetric(a):
        return None
    return {"values": a.tolist(), "hint": f"B = {t[1]} C = {t[2]}"}


def array(*t):
    a = np.empty((9, 9), dtype=int)
    for i in range(9):
        for j in range(9):
            a[i, j] = sum([t[l][k] for k, l in enumerate(CARPET[i][j])], 1)
    validate(a)
    return adjust(a)


def validate(a):
    if np.unique(a).size != a.size:
        raise ValueError("has non-unique elements")
    if not magic(a):
        raise ValueError("not magic")


def adjust(a):
    i, j = np.where(a == 41)
    return np.roll(a, (4-i[0], 4-j[0]), axis=(0, 1))


def symmetric(a):
    sums = np.array([a[i, j]+a[8-i, 8-j] for i in range(4) for j in range(4)])
    return np.all(sums == 82)


def magic(a):
    sums = np.array((np.sum(a, 0), np.sum(a, 1), dsum(a), dsum(np.fliplr(a))))
    return np.all(sums == 369)


def dsum(a):
    return np.array([np.trace(a, -i)+np.trace(a, 9-i) for i in range(9)])

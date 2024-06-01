import numpy as np

def random_matrix(n, rnd, lo, hi):
  # nxn matrix random vals in [lo,hi)
  return (hi - lo) * rnd.random_sample((n,n)) + lo

def mat_inverse(m):
  n = len(m)
  if n == 2:
    a = m[0][0]; b = m[0][1]
    c = m[1][0]; d = m[1][1]
    det = (a*d) - (b*c)
    return np.array([[ d/det, -b/det],
                     [-c/det,  a/det]])
  result = np.copy(m)
  (toggle, lum, perm) = mat_decompose(m)
  b = np.zeros(n)
  for i in range(n):
    for j in range(n):
      if i == perm[j]:
        b[j] = 1.0
      else:    # weirdly necessary
        b[j] = 0.0

    x = helper(lum, b)
    for j in range(n):
      result[j][i] = x[j]
  return result

def helper(lum, b):
  n = len(lum)
  x = np.copy(b)
  for i in range(1,n):
    sum = x[i]
    for j in range(0,i):
      sum -= lum[i][j] * x[j]
    x[i] = sum
 
  x[n-1] /= lum[n-1][n-1]
  i = n-2
  while i >= 0:
    sum = x[i]
    for j in range(i+1,n):
      sum -= lum[i][j] * x[j]
    x[i] = sum / lum[i][i]
    i -= 1
  return x

def mat_determinant(m):
  n = len(m)
  if n == 2:
    a = m[0][0]; b = m[0][1]
    c = m[1][0]; d = m[1][1]
    return (a * d) - (b * c)

  if n == 3:
    a = m[0][0]; b = m[0][1]; c = m[0][2]
    d = m[1][0]; e = m[1][1]; f = m[1][2]
    g = m[2][0]; h = m[2][1]; i = m[2][2]
    return (a * ((e*i)-(f*h))) - \
           (b * ((d*i)-(f*g))) + \
           (c * ((d*h)-(e*g))) 

  (toggle, lum, perm) = mat_decompose(m)

  result = toggle  # -1 or +1
  for i in range(n):
    result *= lum[i][i]
  return result

def mat_decompose(m):
  # Crout's LU decomposition
  toggle = +1  # even
  n = len(m)
  lum = np.copy(m)
  perm = np.arange(n)

  for j in range(0,n-1):  # by column. note n-1 
    max = np.abs(lum[j][j])  # or lum[i,j]
    piv = j

    for i in range(j+1,n):
      xij = np.abs(lum[i][j])
      if xij > max:
        max = xij; piv = i

    if piv != j:  # exchange rows j, piv
      lum[[j,piv]] = lum[[piv,j]]  # special syntax

      t = perm[piv]  # exchange items
      perm[piv] = perm[j]
      perm[j] = t

      toggle = -toggle

    xjj = lum[j][j]
    if np.abs(xjj) > 1.0e-5:  # if xjj != 0.0 
      for i in range(j+1,n):
        xij = lum[i][j] / xjj
        lum[i][j] = xij
        for k in range(j+1,n):
          lum[i][k] -= xij * lum[j][k]
  return (toggle, lum, perm)

def mat_equal(m1, m2, epsilon):
  n = len(m1)
  for i in range(n):
    for j in range(n):
      if np.abs(m1[i][j] - m2[i][j]) > epsilon:
        return False
  return True

def main():
  print("\nBegin matrix inverse from scratch Python ")
  np.set_printoptions(formatter={'float': '{: 8.4f}'.format})
  rnd = np.random.RandomState(1)

  # m = random_matrix(5, rnd, -10.0, +10.0)
  m = [[4,7], [2,6]]
  print("\nm = ")
  print(m)

  if mat_determinant(m) == 0:
    print("\nno inverse ")
  else:
    mi = mat_inverse(m)
    print("\nInverse from scratch mat_inverse() = ")
    print(mi)

    mi = np.linalg.inv(m)
    print("\nInverse from numpy.linalg.inv() = ")
    print(mi)

  print("\nEnd demo ")

if __name__ == "__main__":
  main()

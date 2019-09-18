from fractions import gcd
import random

def multiplicative_inverse(a, n):
  t = 0
  r = n
  t_i = 1
  r_i = a
  while r_i != 0:
    q = r // r_i
    t, t_i = t_i, t - (q * t_i)
    r, r_i = r_i, r - (q * r_i)
  if r > 1:
    return -1
  if t < 0:
    return t + n
  return t

def find_coprime(n):
  e = n

  while gcd(e, n) != 1:
    e = random.randrange(2, n)

  return e



def decrypt(c, **kwargs):
  totient = kwargs.get("phi")
  e = kwargs.get("e")
  p = kwargs.get("p")
  q = kwargs.get("q")
  n = kwargs.get("n")

  n = p * q

  if totient is None:
    totient = (p-1)*(q-1)

  if e is None:
    e = find_coprime(totient)

  d = multiplicative_inverse(e, totient)

  # decryption
  return pow(c, d, n)

m = decrypt(c=, e=, p=, q=)

# m_b = m.to_bytes((m.bit_length() + 7) // 8, 'big')

# print(''.join(chr(char) for char in m_b))





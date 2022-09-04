import sys
import bcrypt

#password

p = b'password'

a = sys.argv
c = len(a)

if c==2:
    p = str(a[1]).encode("utf-8")

s = bcrypt.gensalt()
h = bcrypt.hashpw(p, s)

print(h)

import math
#przykład 1


n=100
def policz(a,b,c,y=1):
    global n
    n = (a+b)*y - c + n + hx(b)
    return n

def hx(k):
    return math.sqrt(k)*k**3


print(policz(3,5,7,3))
print(policz(5.66,0.34,-9.04,8.12))
print(policz(5.66,0.34,-9.04))

print(n)


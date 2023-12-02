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

#przykład2
def rank(*lang,nrrank,**kwargs):
    print(f"ranking języków programowania nr {nrrank} -> miejsce pierwsze: {lang[0]}, "
          f"miejsce drugie: {lang[1]}, miejsce trzecie: {lang[2]}. [{kwargs}]")

rank("Python","Java","C++","C#",nrrank=456)
rank("Python","JavaScript","Java","C++","C#",nrrank=456,ver="1.2")

#funkcje anonimowe
print((lambda d:d+66)(4))
print((lambda d:d+66)(8.5))
print((lambda d,t:d+66-t)(-2,3.3))

b = lambda a,b,c=3:(a+b)/c
print(b(4,7,3))
print(b(5.5,8))

def multi(n):
    return lambda a:a*n

print(multi(7)(3))

#przykład

num  = [67,8,-9,13,5,132,0,111,-66,19,1222,3,-12,0,2]
parzlista = list(filter(lambda x:x%2==0,num))
print(parzlista)


cube = list(map(lambda x:x**3,num))
print(cube)

def mbl(n):
    return 5*n+n/7

values = list(map(mbl,num))

print(values)

kwadraty = [i**2 for i in num]
print(kwadraty)

def generuj_tablice(pot,min,max):
    return [i**pot for i in range(min,max+1)]

pt = generuj_tablice(5,101,1999)
print(pt)

#funkcja wyższego rzędu

def witaj(imie):
    return f"Miło Cię widzieć: {imie}"

def konkurs(imie,punkty,zaliczenie):
    return f"Uczestnik konkursu: {imie}, liczba punktów: {punkty} -> Czy zaliczył: {zaliczenie}"

def gx(x,y):
    return x+2*y

def info():
    return "to funkcja bez argumentów"

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Anna",65,"tak"))
print(osoba(gx,3,5))
print(osoba(info))

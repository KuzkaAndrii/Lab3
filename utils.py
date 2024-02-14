def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
def Is_p(n):
	i=1
	prime = True
	while i <= n**0.5:
		prime = prime and n%i!=0
		i+=1
	return prime
def gcd(a, b):
if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return gcd(a % b, b)
    else:
        return gcd(a, b % a)
def f(n):

if name=="__main__":
   print("Hello, World")

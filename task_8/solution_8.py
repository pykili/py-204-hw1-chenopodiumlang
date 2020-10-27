N = int(input("Print N: "))
a = int(input())
a1 = a
s = 0
while a != 0 and s != N-1:
	a = int(input())
	s = s+1
	a1 = a1+a
b = a1 / (s+1)
print(b)

N = int(input("Введите N: "))
N1 = 0
for i in range (1, N+1):
	N1 = N1 + (i*2 - 1)
a= N1 == N**2
print(a)

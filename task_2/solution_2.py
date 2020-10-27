user_input=input()
b=int(len(user_input))
c=0
for i in range (b):
	a=user_input[i]
	for u in range (i):
		if user_input[u] == a:
			c=c+1
			print(a, c)

a=input()
b=int(len(a))
p=int(a[0])
for i in range(b):
	if i != b:
		q=int(a[i])
		if p < q:
			p=int(a[i])
print(p)

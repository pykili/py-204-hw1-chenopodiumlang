word = input("Введите слово: ")
length = int(len(word))
is_palindrom = "unknown"
for i in range (length):
	if word[i] == word[length-1-i]:
		is_palindrom = True
	else: is_palindrom = False
print(is_palindrom)

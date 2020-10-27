alphabet = ""
for k in range (10):
	user_input = input()
	length = int(len(user_input))
	for i in range (length):
		if user_input[i] not in str(alphabet):
			alphabet = alphabet + user_input[i]
print(alphabet)

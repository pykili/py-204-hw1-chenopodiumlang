num = 1234567890
for k in range (10):
	user_input = input()
	if user_input[0] in str(num):
		a = int(len(user_input))
		i = 0
		for i in range (a):
			if user_input[i] == '\t':
				t3 = i+1
		for i in range (t3-1):
			if user_input[i] == '\t':
				t2 = i+1
		for i in range (t2-1):
			if user_input[i] == '\t':
				t1 = i+1
		form = user_input[t1]
		lemma = user_input[t2]
		for i in range (t1+1, t2):
			form = form + user_input[i]
		for i in range (t2+1, t3):
			lemma = lemma + user_input[i]
		if form != lemma:
			condition = True
		else: condition = False
		if condition == True:
			print (form, lemma)

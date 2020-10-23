front_vow = "eiöü"
back_vow = "aıou"
vows = "eiöüaıou"
user_input = input()
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
for i in range (t1+1, t2-1):
	form = form + user_input[i]
for i in range (t2+1, t3-1):
	lemma = lemma + user_input[i]
l = int(len(lemma))
f = int(len(form))
correct = 0
wrong = 0
if form != lemma and form[0] == lemma[0] and lemma in str(form):
	for k in range (t2+2, t3-1):
		if lemma[k] in vows:
			v = lemma[k]
	for k in range (t1+2, t2-1):
		if form[k] in vows:
			if form[k] in front_vow and v in front_vow:
				correct = correct + 1
			elif form[k] in back_vow and v in back_vow:
				correct = correct + 1
			else:
				wrong = wrong + 1
print("correct: ", correct)
print("wrong: ", wrong)


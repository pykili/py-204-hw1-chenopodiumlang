my_string = input()
length = int(len(my_string))
twos = ""
occured_twice = False
for i in range (length):
	if i != length-1:
		pair = my_string[i] + my_string[i+1]
		if pair in str(twos):
			occured_twice = True
		twos = twos + pair
print(occured_twice)

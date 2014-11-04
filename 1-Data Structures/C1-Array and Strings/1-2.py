def reverse_string(string):
	reversed_string = []
	string_length = len(string)
	for i in range(0, string_length):
		reversed_string.append(string[string_length-i-1])
	return reversed_string

print reverse_string("python")
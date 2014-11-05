def reverse_string(string):
	string_length = len(string)
	for i in range(0, string_length/2):
		temp = string[i]
		string[i] = string[string_length-i-1]
		string[string_length-i-1] = temp
	return string

print reverse_string(list("python"))
print "".join(reverse_string(list("python")))
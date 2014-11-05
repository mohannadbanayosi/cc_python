def ispermut(word, test):
	if len(word) != len(test):
		return False
	
	chars = {}
	for char in word:
		try:
			chars[char] += 1
		except KeyError:
			chars[char] = 1
	for char in test:
		try:
			chars[char] -= 1
			if chars[char] == 0:
				del chars[char]
		except KeyError:
			return False
	if len(chars) != 0:
		return False
	return True

print ispermut("google", "ogloeg")
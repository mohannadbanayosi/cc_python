def is_unique(word):
	chars = {}
	for char in word:
		try:
			chars[char]
			return False
		except:
			chars[char] = True
	return True


print is_unique("Honda")
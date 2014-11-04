def build_map(things):
	hash_map = {}
	for thing in things:
		hash_map[thing.id] = thing
	return hash_map

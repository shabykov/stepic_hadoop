import sys
import json

class Mapper:

	def map(self, key, value):
		for i in value.strip().split(" "):
			
			hash_map = {}
			for j in value.strip().split(" "):
				if i != j:
					hash_map[j] = hash_map.get(j, 0) + 1
	
			print("{}\t{}".format(i, json.dumps(hash_map)))

mapper = Mapper()

for i, line in enumerate(sys.stdin):
	mapper.map(key=i, value=line)

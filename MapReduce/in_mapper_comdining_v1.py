import sys

class Mapper:

	def map(self, key, value):
		dict_term = {}
		for token in value.strip().split(" "):
			if token:
				dict_term[token] = dict_term.get(token, 0) + 1

		for key, value in dict_term.items():
			print("{}\t{}".format(key, value))


mapper = Mapper()

for i, line in enumerate(sys.stdin):
	mapper.map(key=i, value=line)

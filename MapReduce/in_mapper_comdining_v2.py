import sys

class Mapper:

	__term_dict = {}

	def map(self, key, value):
		for token in value.strip().split(" "):
			if token:
				self.__term_dict[token] = self.__term_dict.get(token, 0) + 1

	def close(self):
		for key, value in self.__term_dict.items():
			print("{}\t{}".format(key, value))


mapper = Mapper()

for i, line in enumerate(sys.stdin):
	mapper.map(key=i, value=line)

mapper.close()


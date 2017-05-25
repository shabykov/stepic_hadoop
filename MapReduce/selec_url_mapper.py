import sys

class Mapper:

	def map(self, key, value):
		print(value.split("\t")[-1].strip())

mapper = Mapper()

for i, line in enumerate(sys.stdin):
	mapper.map(key=i, value=line)

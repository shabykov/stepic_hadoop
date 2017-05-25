import sys

class Mapper:

	def map(self, key, value):
		print("{}\t{}".format(value.strip().split(",")[-1], 1))

mapper = Mapper()

for i, line in enumerate(sys.stdin):
	mapper.map(key=i, value=line)

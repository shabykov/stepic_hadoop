import sys

class Mapper:

	def map(self, key, value):
		for i in value.strip().split(" "):
			for j in value.strip().split(" "):
				if i != j:
					print("{},{}\t{}".format(i, j, 1))

mapper = Mapper()

for i, line in enumerate(sys.stdin):
	mapper.map(key=i, value=line)

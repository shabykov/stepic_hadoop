import sys

class Mapper:

	def map(self, key, value):
		if value.split("\t")[1] == "user10":
			print(value.strip())

mapper = Mapper()

for i, line in enumerate(sys.stdin):
	mapper.map(key=i, value=line)

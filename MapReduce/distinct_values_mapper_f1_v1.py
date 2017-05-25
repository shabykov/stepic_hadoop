import sys

class Mapper:

	def map(self, key, value):
		for token in value.strip().split(","):
			print("{},{}\t{}".format(key, token, 1))

mapper = Mapper()

for line in sys.stdin:
	input_data = line.strip().split("\t")

	try:
		if len(input_data) and input_data[0] and input_data[-1]:
			mapper.map(key=input_data[0], value=input_data[-1])
	except Exception as error:
		pass
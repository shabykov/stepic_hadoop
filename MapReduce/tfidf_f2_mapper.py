import sys
import re

class Mapper:

	def map(self, key, value):
		print("{}\t{};{}".format(key, re.sub(r'\t', ';', value), 1))
			

mapper = Mapper()

for line in sys.stdin:
	input_data = line.strip().split("\t", 1)

	if len(input_data) == 2:
		try:
			if len(input_data) and input_data[0] and input_data[-1]:
				mapper.map(key=input_data[0], value=input_data[-1])
		except Exception as error:
			pass


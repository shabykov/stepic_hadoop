import sys


class Reducer:

	values = []

	def reduce(self, key, value):
		self.values.append(key)
	
	def close(self):
		for row in sorted(set(self.values)):
			print(row)


reducer = Reducer()

for line in sys.stdin:
	input_data = line.strip().split("\t")

	try:
		if len(input_data) and input_data[0] and input_data[-1]:
			reducer.reduce(key=input_data[0], value=input_data[-1])
	except Exception as error:
		pass

reducer.close()
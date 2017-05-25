import sys


class Reducer:

	hash_map = {}

	__last_key = None
	__variables = []

	def rest_data(self):
		self.__last_key = None
		self.__variables = []

	def reduce(self, key, value):

		if self.__last_key and self.__last_key != key:
			for token in set(self.__variables):
				self.hash_map[token] = self.hash_map.get(token, 0) + 1

			self.rest_data()

		self.__last_key = key
		self.__variables.append(value)

	def close(self):
		if self.__last_key:
			for token in set(self.__variables):
				self.hash_map[token] = self.hash_map.get(token, 0) + 1

		for key, value in self.hash_map.items():
			print("{}\t{}".format(key, value))


reducer = Reducer()

for line in sys.stdin:
	input_data = line.strip().split("\t")

	try:
		if len(input_data) and input_data[0] and input_data[-1]:
			reducer.reduce(key=input_data[0], value=input_data[-1])
	except Exception as error:
		pass

reducer.close()
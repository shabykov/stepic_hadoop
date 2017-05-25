import sys
import json

class Reducer:

	hash_map = {}

	__last_key = None

	def reduce(self, key, value):
		if self.__last_key and self.__last_key != key:
			for k, v in self.hash_map.items():
				print("{}:{}\t{}".format(self.__last_key, k, v))

			self.hash_map = {}

		self.__last_key = key
		for k, v in json.loads(value).items():
			self.hash_map[k] = self.hash_map.get(k, 0) + int(v)	

	def close(self):
		if self.__last_key:
			for k, v in self.hash_map.items():
				print("{}{}\t{}".format(self.__last_key, k, v))




reducer = Reducer()

for line in sys.stdin:
	input_data = line.strip().split("\t")

	try:
		if len(input_data) and input_data[0] and input_data[-1]:
			reducer.reduce(key=input_data[0], value=input_data[-1])
	except Exception as error:
		pass

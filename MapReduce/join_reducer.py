import sys 


class Reducer:

	__last_key = None
	__hash_map = {}

	def reduce(self, key, value):
		k = value.strip().split(":")[0]
		v = value.strip().split(":")[-1]

		if self.__last_key and self.__last_key != key:
			if len(self.__hash_map) > 1:
				for i in self.__hash_map['query']:
					for j in self.__hash_map['url']:
						print("{}\t{}\t{}".format(self.__last_key, i, j))
			
			self.__hash_map = {}

		if self.__hash_map.get(k) is None:
			self.__hash_map[k] = []

		self.__last_key = key
		self.__hash_map[k].append(v)

	def close(self):
		if self.__last_key:
			if len(self.__hash_map) > 1:
				for i in self.__hash_map['query']:
					for j in self.__hash_map['url']:
						print("{}\t{}\t{}".format(self.__last_key, i, j))



reducer = Reducer()

for line in sys.stdin:
	input_data = line.strip().split("\t")

	try:
		if len(input_data) and input_data[0] and input_data[-1]:
			reducer.reduce(key=input_data[0], value=input_data[-1])
	except Exception as error:
		pass

reducer.close()

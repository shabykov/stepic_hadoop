import sys 


class Reducer:

	__last_key = None
	__cache = []

	def reduce(self, key, value):

		if self.__last_key and self.__last_key != key:
			if len(self.__cache) > 1:
				print(self.__last_key)

			self.__cache = []

		self.__last_key = key
		self.__cache.append(value)

	def close(self):
		if self.__last_key:
			if len(self.__cache) > 1:
				print(self.__last_key)


reducer = Reducer()

for line in sys.stdin:
	input_data = line.strip().split("\t")

	try:
		if len(input_data) and input_data[0] and input_data[-1]:
			reducer.reduce(key=input_data[0], value=input_data[-1])
	except Exception as error:
		pass
		
reducer.close()


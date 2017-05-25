import sys 


class Reducer:

	__last_key = None
	__count = 0
	__values = []

	def reduce(self, key, value):
		if self.__last_key and self.__last_key != key:
			for d, t in self.__values:
				print("{}#{}\t{}\t{}".format(self.__last_key, d, t, self.__count))
			self.rest()

		self.__last_key = key
		self.__count += int(value.split(";")[2])
		self.__values.append((value.split(";")[0], value.split(";")[1]))

	def rest(self):
		self.__last_key = None
		self.__count = 0
		self.__values = []

	def close(self):
		if self.__last_key:
			for d, t in self.__values:
				print("{}#{}\t{}\t{}".format(self.__last_key, d, t, self.__count))
			

reducer = Reducer()

for line in sys.stdin:
	input_data = line.strip().split("\t")

	try:
		if len(input_data) and input_data[0] and input_data[-1]:
			reducer.reduce(key=input_data[0], value=input_data[-1])
	except Exception as error:
		pass

reducer.close()


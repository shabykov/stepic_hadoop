import sys


class Reducer:

	__last_key = None
	__sum = 0
	__count = 0

	def rest_data(self):
		self.__last_key = None
		self.__sum = 0
		self.__count = 0

	def reduce(self, key, value):
		summ = int(value.split(";")[0])
		count = int(value.split(";")[-1])

		if self.__last_key and self.__last_key != key:
			print("{}\t{};{}".format(self.__last_key, self.__sum, self.__count))

			self.rest_data()
		self.__last_key, self.__sum, self.__count = key, self.__sum + summ, self.__count + count

	def close(self):
		if self.__last_key:
			print("{}\t{};{}".format(self.__last_key, self.__sum, self.__count))


reducer = Reducer()

for line in sys.stdin:
	input_data = line.strip().split("\t")

	try:
		if len(input_data) and input_data[0] and input_data[-1]:
			reducer.reduce(key=input_data[0], value=input_data[-1])
	except Exception as error:
		pass

reducer.close()
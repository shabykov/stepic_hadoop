import sys
import re
import math


class Reducer:
    __last_key = None
    __values = []

    def parse(self, values):
        dist = []
        val = []
        for value in values:
            dist.append(float(value[0].lower()))
            line = re.sub(r'[}{]', '', value[-1])
            val += line.split(',') if line else []
        return int(min(dist)) if math.isfinite(min(dist)) else str(min(dist)).upper(), '{'+ "{}".format(','.join([v for v in val]) if len(val) else '') + '}'

    def reduce(self, key, value):

        if self.__last_key and self.__last_key != key:
            d, v = self.parse(self.__values)
            print("{}\t{}\t{}".format(self.__last_key, d, v))
            self.__values = []

        self.__last_key = key
        self.__values.append(value.split('\t'))

    def close(self):
        if self.__last_key:
            d, v = self.parse(self.__values)
            print("{}\t{}\t{}".format(self.__last_key, d, v))


reducer = Reducer()
for line in sys.stdin:
    input_data = line.strip().split("\t", 1)
    if len(input_data) == 2:
        reducer.reduce(key=input_data[0], value=input_data[-1])
reducer.close()

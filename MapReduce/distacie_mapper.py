import sys
import re
import math


class Mapper:

	def map(self, key, value):
		value = value.split("\t")
		dist_v = float(value[0].lower())
		line_v = re.sub(r'[}{]', '', value[-1])
		list_v = line_v.split(',')

		print("{}\t{}\t{}".format(key, int(dist_v) if math.isfinite(dist_v) else str(dist_v).upper(), value[-1]))

		for v in list_v:
			if v:
				print("{}\t{}\t{}".format(v, int(dist_v + 1) if math.isfinite(dist_v) else str(dist_v).upper(), {}))



mapper = Mapper()

for line in sys.stdin:
	input_data = line.strip().split("\t", 1)

	if len(input_data) == 2:
		mapper.map(key=input_data[0], value=input_data[-1])



import sys
import re

class Mapper:

	def map(self, key, value):
		for token in value.split():
			print("{}#{}\t{}".format(token, key, 1))
			

mapper = Mapper()

for line in sys.stdin:
	input_data = line.strip().split(":", 1)

	if len(input_data) == 2:
		try:
			if len(input_data) and input_data[0] and input_data[-1]:
				mapper.map(key=re.sub(r'[^A-Za-z0-9]+', '', input_data[0]), 
					       value=re.sub(r'[^A-Za-z0-9]+', ' ', input_data[-1]))
		except Exception as error:
			pass

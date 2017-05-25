import sys

lastKey, summ = None, 0

for line in sys.stdin:
	key, value = line.strip().split("\t")

	if lastKey and lastKey != key:
		print("{}\t{}".format(lastKey, summ))
		lastKey, summ = key, int(value)
	else:
		lastKey, summ = key, summ + int(value)

if lastKey:
	print("{}\t{}".format(lastKey, summ))




import csv
from datetime import datetime
from itertools import izip

RADIATION_RAW = "rawdata/radiation.csv"
GENERATION_RAW = "rawdata/generation.csv"

PREPARED_DATA = "tensorflow/sun_dataset.csv"

raw = csv.reader(open(RADIATION_RAW, "rb"), delimiter = ';')
transposed_raw = izip(*raw)

transposed_prepared = []

for i, row in enumerate(transposed_raw):
	data_row = []
	
	for j, item in enumerate(row):
		data_row.append(float(item))

	transposed_prepared.append(data_row)

generation = (csv.reader(open(GENERATION_RAW, "rb"), delimiter = ';'))
data_row = []
for i, row in enumerate(generation):
	datetime_object = datetime.strptime(row[0], '%d.%m.%Y %H:%M')
	data_row.append(row[1].replace(',', '.'))

transposed_prepared.append(data_row)

# for row in transposed_prepared:
# 	max_item = 0.0
# 	for item in row:
# 		a = abs(float(item))
# 		if a > max_item:
# 			max_item = a
# 	print max_item
# 	for i, item in enumerate(row):
# 		row[i] = float(item) / max_item  


prepared = izip(*transposed_prepared)

csv.writer(open(PREPARED_DATA, "wb"), delimiter = ';').writerows(prepared)
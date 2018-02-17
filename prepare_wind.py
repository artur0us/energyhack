import csv
from datetime import datetime
from itertools import izip

WEATHER_RAW = "rawdata/weather.csv"
GENERATION_RAW = "rawdata/generation.csv"

PREPARED_DATA = "tensorflow/wind_dataset.csv"

raw = csv.reader(open(WEATHER_RAW, "rb"), delimiter = ';')
transposed_raw = izip(*raw)

transposed_prepared = []

for i, row in enumerate(transposed_raw):
	data_row = []
	if i == 0:
		for item in row:
			datetime_object = datetime.strptime(item, '%d.%m.%Y %H:%M')
			data_row.append(float(datetime_object.day))
	if i in [1, 2, 4, 6]:
		last_item = 0.0
		for j, item in enumerate(row):
			if item == '':
				data_row.append(float(last_item))
			else:
				data_row.append(float(item))
				last_item = float(item)
	if i == 0 or i in [1, 2, 4, 6]:
		transposed_prepared.append(data_row)

generation = (csv.reader(open(GENERATION_RAW, "rb"), delimiter = ';'))
data_row = []
for i, row in enumerate(reversed(list(generation))):
	datetime_object = datetime.strptime(row[0], '%d.%m.%Y %H:%M')
	if datetime_object.hour % 3 == 0:
		data_row.append(row[2].replace(',', '.'))

transposed_prepared.append(data_row)

for row in transposed_prepared:
	max_item = 0.0
	for item in row:
		a = abs(float(item))
		if a > max_item:
			max_item = a
	print max_item
	for i, item in enumerate(row):
		row[i] = float(item) / max_item  


prepared = izip(*transposed_prepared)

csv.writer(open(PREPARED_DATA, "wb"), delimiter = ';').writerows(prepared)
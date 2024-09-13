#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# Sec001

def average_time(records: list[float | None]) -> float:
	records = list(filter(lambda x: x!=None,records))
	return sum(records) / len(records)

def running_streaks(records: list[float | None]) -> list[int]:
	records = list(filter(lambda x: x!=None,records))
	records_lower_average = list(filter(lambda x: x < average_time(records),records))
	# print(average_time(records))

	counter = list(map(lambda i: records_lower_average.count(i) ,records_lower_average))
	# print(counter)

	if len(counter) <= 0:
		return counter

	mapping = list(map(lambda i,j: (i , j), counter, records_lower_average))
	# print(mapping)
	# print(max(mapping)[0])
	
	list_max = list(filter(lambda x: x[0]==max(mapping)[0] , mapping))

	# print(list_max,end=" => ")
	result = []
	for i in range(len(list_max)):
		if list_max[i] != list_max[i-1] or len(list_max)==1:
			result.append(list_max.count(list_max[i]))
		elif(list_max[i] == list_max[i-1]):
			result.append(list_max[i][0])
			break
		else:
			continue			
	return result

if __name__ == '__main__':
	# print(average_time([12., 14., 18., None, 14., 13., 14., 22., 20., 15., 15., 15.]))
	print(running_streaks([15., 15.]))
	print(running_streaks([12., 14., 18., None, 14., 13., 14.,22., 20., 15., 15., 15.]))
	print(running_streaks([15., 16.] ))
	print(running_streaks([1., 16., 8.]))
	print(running_streaks([16., 8., 1.]))
	print(running_streaks([1., None, 1., 10.] ))

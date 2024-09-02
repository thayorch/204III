from HW09_2_670510662 import median_of_median as median_of_median2

def median_of_median(num: list[float]) -> float:
	n = len(num)
	if n == 0: return 0
	if n == 1: return num[0]
	if n == 2: return (num[0] + num[1]) / 2
	
	# size of sublist
	div_n = n // 3
	
	# divide 
	m1 = median_of_median(num[:div_n])
	m2 = median_of_median(num[div_n:div_n*2])
	m3 = median_of_median(num[div_n*2:])

	# find median

	# manual bubble sort
	if m1 > m2: [m1,m2] = [m2,m1]
	if m2 > m3: [m2,m3] = [m3,m2]
	if m1 > m2: [m1,m2] = [m2,m1]

	return m2


median_of_median([47, 25, 25, 39, 34, 31])



def test():
    import random
    for i in range(1000):
        l = []
        for j in range(random.randint(1,20)):
            l += [random.randint(1,100)]
        try:
            assert(median_of_median(l)) == median_of_median2(l)
        except:
            print(l)
            print('expect :',median_of_median2(l))
            print('got :',median_of_median(l))
            return 0
    print('--')
    
test()
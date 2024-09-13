#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# Sec001

def lucky_number(list_num: list[int]) -> int:
	if len(list_num) % 2 == 0:
		lists = list(map(lambda x: (list_num[x-1],list_num[x]) ,range(1,len(list_num),2)))
		m = list(map(lambda x: check(x) , lists))
	elif len(list_num) % 2 == 1:
		list_new = list(filter(lambda x: x!=list_num[-3],list_num))
		lists = list(map(lambda x: (list_new[x-1],list_new[x]) ,range(1,len(list_new),2)))
		m = list(map(lambda x: check(x) if x!=lists[-1] else check2(x, list_num) , lists))  
	
	# print(m)

	if len(m) == 1:
		return m[0]
	return lucky_number(m)


def check(t: tuple[int,int]):
	if sum(t)%2==0:
		return max([t[0],t[1]])
	elif sum(t)%2==1:
		return min([t[0],t[1]])

def check2(t: tuple[int,int], list_num):
	if sum(t)%2==0:
		return check((max([t[0],t[1]]) , list_num[-3]))
	elif sum(t)%2==1:
		return check((min([t[0],t[1]]) ,  list_num[-3]))


if __name__ == '__main__':

	lists = []
	for i in range(1,1000000):
		lists.append(i)
	lists = list(filter(lambda x: x%2==1, lists))
	print(lucky_number(lists))



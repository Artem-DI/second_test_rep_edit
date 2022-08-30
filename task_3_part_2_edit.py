#level 1
'''l = [1, 4, 1, 6, 'hello', 'a', '5', 'hello']
l2 = []

for i in l:
	if l.count(i) > 1:
		l2.append(i)
print()
print(list(set(l2)))'''




#level 2

'''from random import randint

n =5 
m = [[randint(0, 100) for i in range(n)] for j in range(n)]
max_list = []
for i in m:
	max_ = max(i)	
	max_list.append(max_)

	#if max_ not in max_list:
		#max_list.append(max_)
#print(max_list)
print()
print(m)
print()
print(max_list)
print()
print(max(max_list))'''
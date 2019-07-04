# testing random stuff

import re 

lst1 = ['terry', 'cat', 'ggigi']
list_as_string = str(lst1)
list_as_string = list_as_string.strip()
#print(type(list_as_string))

str1 = "cat burrito"

x = re.findall("[.?!]", str1)
y = re.sub("[#.!?]", " ", str1)
#z = y.split()

if (y):
	z = y.split()
	for i in z:
		lst1.append(i)

print(lst1)
#print(z)
# if (y):
# 	print("!!!")
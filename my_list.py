#create an empty list callked my list
my_list =[]
#Apeend the following elements to my_list:10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#insert the value 15 at thesecond position in the list
my_list.insert(1, 15)
#Extendmy list with another list:[50, 60, 70]
my_list.extend([50, 60, 70])
#Remove the lastelement from my list
my_list.pop()
#sort my list in ascending order
my_list.sort()
#find and print the index of the value 30 in my_list
index = my_list.index(30)
print(index)
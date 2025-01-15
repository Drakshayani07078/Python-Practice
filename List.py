
'''Homo + Hetro type data
order collection of data
duplicate allowed
mutable list ( we can modify)
Operation : 
 1.append(1 parameter) At end
 2. insert(2, "3") At specfic position
 3. .remove(element) only removes not returns removed value
 4. .pop()  removes and also returns removed value
 5. in & not in Checks whether element is present or not
'''
li1 = ["ert", 12, 34.6, 'V', True]
print(type(li1),li1)

li2= ["ert", 34.6, 'V', True, "ert", 12, 34.6, 'V', True]
print(li2)

li1.append(89)
print(li1)

li1.insert(4,67)
print(li1)

li1.remove(67)  
print(li1)

li1.pop()
print(li1)

li1.pop(3)
print(li1)

print( li1 in 12)
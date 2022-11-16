################################# FIBONACCI SERIES #############################

user = int(input("enter the number: \n")) # gets the integer from the user
a = 0
b = 1
for i in range(user): 
  c = a + b # initial values of a and b 
  b = a # swap of a in to b 
  a = c # swap of c in to a  
  print(c,end =' ')

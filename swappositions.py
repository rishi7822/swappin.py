#swap elements at a given psoitions
def swapPositions(list,pos1,pos2):

#storing the two elemnts as a pair in a tuple variable get
 get = list[pos1], list[pos2]

#unpacking those elements
 list[pos2], list[pos1] = get

 return list 

#drivers code
list = [23,65,19,90]

pos1,pos2 = 1,3
print(swapPositions(list,pos1-1,pos2-1))
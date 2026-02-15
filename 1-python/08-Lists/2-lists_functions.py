freinds = [1, " omar ", True, False ,[1," abd al gwad"]]
family = [2, " Amr ", False, True ,[1," abd al gwad"]]

#some lists functions
freinds.extend(family)   #to merge two lists in one 
freinds.append(" Amr ")  #add to list
freinds.insert(0, " Amr") #add in specific index
freinds.remove(1)         # to remove one thing
freinds.pop()             # remove the last index of the list

print(freinds.index(" omar "))  #find the index 

freinds.count(True)  # to know the repeated count number

freinds.sort()      # to sort the list

list_new = freinds.copy()  # to make a copy of the list and it willnot change if the main list change

#freinds.clear()           # remove allthing

print(freinds) 


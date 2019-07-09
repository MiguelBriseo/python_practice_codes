#Write your function here
def larger_list(lst1, lst2):
  if int(len(lst1)) > int(len(lst2)):
    return lst1[-1]
  elif int(len(lst1)) < int(len(lst2)):
    return lst2[-1]
  else:
    return lst1[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

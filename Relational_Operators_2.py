def greater_than(x, y):
  if x > y:
    return x
  if x < y:
    return y
  if x == y:
    return "These numbers are the same"
  
def graduation_reqs(credits):
  if credits >= 120:
    return "You have enough credits to graduate!"
  
print(greater_than(7, 9))
print(graduation_reqs(120))

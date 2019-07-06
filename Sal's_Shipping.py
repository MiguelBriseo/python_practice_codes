premium = 125.00

# Ground Shipping
def ground_shipping(weight, cost):
  if weight <= 2:
    return (weight * 1.50 + cost)
  elif 2 < weight <= 6:
    return (weight * 3.00 + cost)
  elif 6 < weight <= 10:
    return (weight * 4.00 + cost)
  else:
    return (weight * 4.75 + cost)
  
# Drone Shipping
def drone_shipping(weight, cost):
  if weight <= 2:
    return (weight * 4.50 + cost)
  elif 2 < weight <= 6:
    return (weight * 9.00 + cost)
  elif 6 < weight <= 10:
    return (weight * 12.00 + cost)
  else:
    return (weight * 14.25 + cost)

# Cheapest Method of shipping



print(ground_shipping(8.4, 20))
print(drone_shipping(1.5, 0))

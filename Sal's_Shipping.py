premium = 125.00
weight = 17.0

# Ground Shipping
def ground_shipping(weight):
  if weight <= 2:
    return (weight * 1.50 + 20)
  elif 2 < weight <= 6:
    return (weight * 3.00 + 20)
  elif 6 < weight <= 10:
    return (weight * 4.00 + 20)
  else:
    return (weight * 4.75 + 20)
  
# Drone Shipping
def drone_shipping(weight):
  if weight <= 2:
    return (weight * 4.50 + 0)
  elif 2 < weight <= 6:
    return (weight * 9.00 + 0)
  elif 6 < weight <= 10:
    return (weight * 12.00 + 0)
  else:
    return (weight * 14.25 + 0)

# Cheapest Method of shipping
def cheap_method(weight):
  if ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < premium:
    return "Ground shipping is the cheapest method, and it costs: " + str(ground_shipping(weight))
  elif drone_shipping(weight) < ground_shipping(weight) and drone_shipping(weight) < premium:
    return "Drone shipping is the chepeast method, and it costs: " + str(drone_shipping(weight))
  elif premium < ground_shipping(weight) and premium < drone_shipping(weight):
    return "Premium ground shipping is the cheapest method, and it costs: " + str(premium)


print(cheap_method(weight))

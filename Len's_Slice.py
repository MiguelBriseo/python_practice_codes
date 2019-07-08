# Lists
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]

# Arrangements
num_pizzas = len(toppings)
pizzas = list(zip(prices, toppings))
pizzas.sort()

chepeast_pizza = pizzas[1]
priciest_pizza = pizzas[-1]
three_chepeast = pizzas[:2]
num_two_dollar_slices = prices.count(2)

# Prints
print("We sell "+ str(num_pizzas) + " different kinds of pizza!")
print(pizzas)
print(chepeast_pizza)
print(priciest_pizza)
print(three_chepeast)
print(num_two_dollar_slices)

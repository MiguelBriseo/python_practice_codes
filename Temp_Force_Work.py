train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

f100_in_celsius = 0
c0_in_fahrenheit = 0
train_force = 0
c = 3 * 10**8
bomb_energy = 0
train_work = 0
# Functions--------------------------------------------
# Function that converts F to C


def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp

# Function that converts C to F


def c_to_f(c_temp):
    f_temp = c_temp * (9 / 5) + 32
    return f_temp

# Function Force


def get_force(mass, acceleration):
    return mass * acceleration


def get_energy(mass, c):
    return mass * (c**2)


def get_work(mass, acceleration, distance):
    return get_force(mass, acceleration) * distance

# -----------------------------------------------------


# 100 Fahrenheit F to Celcius C
f100_in_celsius = f_to_c(100)
# 0 C
c0_in_fahrenheit = c_to_f(0)
# Force Test
train_force = get_force(train_mass, train_acceleration)
# Energy Test
bomb_energy = get_energy(bomb_mass, c)
# Test Work
train_work = get_work(train_mass, train_acceleration, train_distance)

# Printing
print(str(f100_in_celsius) + " C")
print(str(c0_in_fahrenheit) + " F")
print("The GE train supplies " + str(train_force) + " Newtons of force.")
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")
print("The GE train does " + str(train_work) +
      " Joules of work over " + str(train_distance) + " meters.")

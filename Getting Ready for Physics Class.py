# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below:
#Fahrenheit converts to temperature in Celsius.
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

# Test usage:
f100_in_celsius = f_to_c(100)

print(f"100°F is {f100_in_celsius:.2f}°C")

#Celsius converts to temperature in Fahrenheit.
def c_to_f(c_temp):
    f_temp = c_temp * 5/9 + 32
    return f_temp

c0_in_fahrenheit = c_to_f(0)

print(f"0°C is {c0_in_fahrenheit:.2f}°F")

#Force Function
def get_force(mass, acceleration):
    force = mass * acceleration
    return force

train_force = get_force(train_mass, train_acceleration)
print(f"The GE train supplies {train_force} Newtons of force.")

#Energy Function
def get_energy(mass, c=3*10**8):
    energy = mass * c**2
    return energy

bomb_energy=get_energy(bomb_mass)

print(f"A 1kg bomb supplies {bomb_energy} Joules.")

#Final Function
def get_work(mass,acceleration,distance):
    

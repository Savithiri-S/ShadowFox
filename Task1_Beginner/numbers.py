# Question 1

def format_number(num, fmt):
    return format(num, fmt)

print(format_number(145, 'o'))

# Question 2

radius = 84
pi = 3.14

area = pi * radius * radius

water = area * 1.4

print("Area of pond =", area)
print("Total water =", int(water), "liters")

# Question 3

distance = 490
time_seconds = 7 * 60

speed = distance / time_seconds

print("Speed =", int(speed), "m/s")
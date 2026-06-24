# Question 1 - BMI Calculator

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))

bmi = weight / (height ** 2)

if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")


# Question 2 - Find Country from City

australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("\nEnter a city name: ")

if city in australia:
    print(city, "is in Australia")
elif city in uae:
    print(city, "is in UAE")
elif city in india:
    print(city, "is in India")
else:
    print("City not found")


# Question 3 - Check if Two Cities Belong to Same Country

city1 = input("\nEnter first city: ")
city2 = input("Enter second city: ")

if city1 in india and city2 in india:
    print("Both cities are in India")

elif city1 in australia and city2 in australia:
    print("Both cities are in Australia")

elif city1 in uae and city2 in uae:
    print("Both cities are in UAE")

else:
    print("They don't belong to the same country")
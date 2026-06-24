class Avenger:

    def __init__(self, name, age, gender, super_power, weapon, leader=False):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
        self.leader = leader

    def get_info(self):
        print("\n--- Avenger Details ---")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Super Power:", self.super_power)
        print("Weapon:", self.weapon)

    def is_leader(self):
        if self.leader:
            print(self.name, "is a leader.")
        else:
            print(self.name, "is not a leader.")


# Creating Avengers

captain_america = Avenger(
    "Captain America", 100, "Male",
    "Super Strength", "Shield", True
)

iron_man = Avenger(
    "Iron Man", 48, "Male",
    "Technology", "Armor"
)

black_widow = Avenger(
    "Black Widow", 35, "Female",
    "Superhuman", "Batons"
)

hulk = Avenger(
    "Hulk", 49, "Male",
    "Unlimited Strength", "No Weapon"
)

thor = Avenger(
    "Thor", 1500, "Male",
    "Super Energy", "Mjolnir"
)

hawkeye = Avenger(
    "Hawkeye", 40, "Male",
    "Fighting Skills", "Bow and Arrows"
)

# Store all objects in a list

avengers = [
    captain_america,
    iron_man,
    black_widow,
    hulk,
    thor,
    hawkeye
]

# Display information

for hero in avengers:
    hero.get_info()
    hero.is_leader()
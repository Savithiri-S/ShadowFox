justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern"
]

print("Original List:", justice_league)

print("Members:", len(justice_league))

justice_league.extend(["Batgirl", "Nightwing"])
print("\nAfter adding members:")
print(justice_league)

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("\nWonder Woman becomes leader:")
print(justice_league)

justice_league.remove("Green Lantern")

flash_index = justice_league.index("Flash")

justice_league.insert(flash_index, "Green Lantern")

print("\nSeparated Flash and Aquaman:")
print(justice_league)

justice_league = [
    "Cyborg",
    "Shazam",
    "Hawkgirl",
    "Martian Manhunter",
    "Green Arrow"
]

print("\nNew Team:")
print(justice_league)

justice_league.sort()

print("\nSorted Team:")
print(justice_league)

print("New Leader:", justice_league[0])
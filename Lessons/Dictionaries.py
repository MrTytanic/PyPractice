# Dictionary = collection of {key:value} pairs

capitals = {"USA": "Washington D.C.",
                    "India": "New Delhi",
                    "China": "Beijing",
                    "Russia": "Moscow"}

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")

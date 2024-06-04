countries = [["germany", "france", "italy", "romania"],
             ["usa", "canada", "mexico"],
             ["japan", "china"]]

# 2D Collections can be used to store a data matrix

for collection in countries:
    for nations in collection:
        print(nations, end=" ")
    print()
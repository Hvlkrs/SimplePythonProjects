products = ["Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice", "In Cold Blood", "Wide Sargasso Sea",\
"One Hundred Years of Solitude", "Brave New World",  "The Great Gatsby", "Brave New World",\
"I Capture The Castle", "Brave New World", "The Great Gatsby", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice"]

nonrepeated_values = set()
repeated_values = set()

for book in products:
    if book in repeated_values:
        continue
    if book in nonrepeated_values:
        nonrepeated_values.remove(book)
        repeated_values.add(book)
    else:
        nonrepeated_values.add(book)

print(list(nonrepeated_values))
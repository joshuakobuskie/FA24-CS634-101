# %% [markdown]
# # CS634-101 Midterm Project - Apriori Algorithm
# 
# **Author** : *Joshua Kobuskie*

# %% [markdown]
# ## Part 1 Details
# 1. Create 10 (or any number of, not less than 5) items usually seen in
# Amazon, K-mart, or any other supermarkets (e.g. diapers, clothes, etc.).
# 2. Create a database of at least 20 transactions each containing some of these
# items. Save the transaction in a CSV file.
# 3. Repeat (1) by creating 4 additional, different databases each containing at
# least 20 transactions.
# 4. Note: You can create these transactions and datasets manually, download
# them from the net, or use the examples I will provide. In any case, add a
# note to your report where and how you built your data sets.
# 5. The items and transaction must not be random so that your code is
# deterministic

# %% [markdown]
# ### Data Initialization: ###
# At the beginning of the program, transactional data is initialized for each store. A dataset is created for each of the retail stores represented and this data is saved into a CSV for future use in the current directory. Datasets 1 through 6 have been created based on the examples provided. Dataset 7 has been built using GenAI, and contains 1000 transactions with 30 unique items to simulate Walmart transactional data.

# %%
# Create Amazon transactions from provided example

import csv

amazonData  = [
["A Beginner’s Guide", "Java: The Complete Reference", "Java For Dummies", "Android Programming: The Big Nerd Ranch"],
["A Beginner’s Guide", "Java: The Complete Reference", "Java For Dummies"],
["A Beginner’s Guide", "Java: The Complete Reference", "Java For Dummies", "Android Programming: The Big Nerd Ranch", "Head First Java 2nd Edition"],
["Android Programming: The Big Nerd Ranch", "Head First Java 2nd Edition", "Beginning Programming with Java"],
["Android Programming: The Big Nerd Ranch", "Beginning Programming with Java", "Java 8 Pocket Guide"],
["A Beginner’s Guide", "Android Programming: The Big Nerd Ranch", "Head First Java 2nd Edition"],
["A Beginner’s Guide", "Head First Java 2nd Edition", "Beginning Programming with Java"],
["Java: The Complete Reference", "Java For Dummies", "Android Programming: The Big Nerd Ranch"],
["Java For Dummies", "Android Programming: The Big Nerd Ranch", "Head First Java 2nd Edition", "Beginning Programming with Java"],
["Beginning Programming with Java", "Java 8 Pocket Guide", "C++ Programming in Easy Steps"],
["A Beginner’s Guide", "Java: The Complete Reference", "Java For Dummies", "Android Programming: The Big Nerd Ranch"],
["A Beginner’s Guide", "Java: The Complete Reference", "Java For Dummies", "HTML and CSS: Design and Build Websites"],
["A Beginner’s Guide", "Java: The Complete Reference", "Java For Dummies", "Java 8 Pocket Guide", "HTML and CSS: Design and Build Websites"],
["Java For Dummies", "Android Programming: The Big Nerd Ranch", "Head First Java 2nd Edition"],
["Java For Dummies", "Android Programming: The Big Nerd Ranch"],
["A Beginner’s Guide", "Java: The Complete Reference", "Java For Dummies", "Android Programming: The Big Nerd Ranch"],
["A Beginner’s Guide", "Java: The Complete Reference", "Java For Dummies", "Android Programming: The Big Nerd Ranch"],
["Head First Java 2nd Edition", "Beginning Programming with Java", "Java 8 Pocket Guide"],
["Android Programming: The Big Nerd Ranch", "Head First Java 2nd Edition"],
["A Beginner’s Guide", "Java: The Complete Reference", "Java For Dummies"]
]

with open("amazonTransactions.csv", "w") as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(amazonData)

# %%
# Create Best Buy transactions from provided example:

bestBuyData = [
["Desk Top", "Printer", "Flash Drive", "Microsoft Office", "Speakers", "Anti-Virus"],
["Lab Top", "Flash Drive", "Microsoft Office", "Lab Top Case", "Anti-Virus"],
["Lab Top", "Printer", "Flash Drive", "Microsoft Office", "Anti-Virus", "Lab Top Case", "External Hard-Drive"],
["Lab Top", "Printer", "Flash Drive", "Anti-Virus", "External Hard-Drive", "Lab Top Case"],
["Lab Top", "Flash Drive", "Lab Top Case", "Anti-Virus"],
["Lab Top", "Printer", "Flash Drive", "Microsoft Office"],
["Desk Top", "Printer", "Flash Drive", "Microsoft Office"],
["Lab Top", "External Hard-Drive", "Anti-Virus"],
["Desk Top", "Printer", "Flash Drive", "Microsoft Office", "Lab Top Case", "Anti-Virus", "Speakers", "External Hard-Drive"],
["Digital Camera", "Lab Top", "Desk Top", "Printer", "Flash Drive", "Microsoft Office", "Lab Top Case", "Anti-Virus", "External Hard-Drive", "Speakers"],
["Lab Top", "Desk Top", "Lab Top Case", "External Hard-Drive", "Speakers", "Anti-Virus"],
["Digital Camera", "Lab Top", "Lab Top Case", "External Hard-Drive", "Anti-Virus", "Speakers"],
["Digital Camera", "Speakers"],
["Digital Camera", "Desk Top", "Printer", "Flash Drive", "Microsoft Office"],
["Printer", "Flash Drive", "Microsoft Office", "Anti-Virus", "Lab Top Case", "Speakers", "External Hard-Drive"],
["Digital Camera", "Flash Drive", "Microsoft Office", "Anti-Virus", "Lab Top Case", "External Hard-Drive", "Speakers"],
["Digital Camera", "Lab Top", "Lab Top Case"],
["Digital Camera", "Lab Top Case", "Speakers"],
["Digital Camera", "Lab Top", "Printer", "Flash Drive", "Microsoft Office", "Speakers", "Lab Top Case", "Anti-Virus"],
["Digital Camera", "Lab Top", "Speakers", "Anti-Virus", "Lab Top Case"]
]

with open("bestBuyTransactions.csv", "w") as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(bestBuyData)

# %%
# Create K-Mart transactions from provided example:
kMartData = [
["Decorative Pillows", "Quilts", "Embroidered Bedspread"],
["Embroidered Bedspread", "Shams", "Kids Bedding", "Bedding Collections", "Bed Skirts", "Bedspreads", "Sheets"],
["Decorative Pillows", "Quilts", "Embroidered Bedspread", "Shams", "Kids Bedding", "Bedding Collections"],
["Kids Bedding", "Bedding Collections", "Sheets", "Bedspreads", "Bed Skirts"],
["Decorative Pillows", "Kids Bedding", "Bedding Collections", "Sheets", "Bed Skirts", "Bedspreads"],
["Bedding Collections", "Bedspreads", "Bed Skirts", "Sheets", "Shams", "Kids Bedding"],
["Decorative Pillows", "Quilts"],
["Decorative Pillows", "Quilts", "Embroidered Bedspread"],
["Bedspreads", "Bed Skirts", "Shams", "Kids Bedding", "Sheets"],
["Quilts", "Embroidered Bedspread", "Bedding Collections"],
["Bedding Collections", "Bedspreads", "Bed Skirts", "Kids Bedding", "Shams", "Sheets"],
["Decorative Pillows", "Quilts"],
["Embroidered Bedspread", "Shams"],
["Sheets", "Shams", "Bed Skirts", "Kids Bedding"],
["Decorative Pillows", "Quilts"],
["Decorative Pillows", "Kids Bedding", "Bed Skirts", "Shams"],
["Decorative Pillows", "Shams", "Bed Skirts"],
["Quilts", "Sheets", "Kids Bedding"],
["Shams", "Bed Skirts", "Kids Bedding", "Sheets"],
["Decorative Pillows", "Bedspreads", "Shams", "Sheets", "Bed Skirts", "Kids Bedding"]
]

with open("kMartTransactions.csv", "w") as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(kMartData)

# %%
# Create Nike transactions from provided example:
# Corrected Dry Fir V-Nick to Dry Fit V-Neck
# Corrected one line with Dry to Dry Fit V-Neck

nikeData = [
["Running Shoe", "Socks", "Sweatshirts", "Modern Pants"],
["Running Shoe", "Socks", "Sweatshirts"],
["Running Shoe", "Socks", "Sweatshirts", "Modern Pants"],
["Running Shoe", "Sweatshirts", "Modern Pants"],
["Running Shoe", "Socks", "Sweatshirts", "Modern Pants", "Soccer Shoe"],
["Running Shoe", "Socks", "Sweatshirts"],
["Running Shoe", "Socks", "Sweatshirts", "Modern Pants", "Tech Pants", "Rash Guard", "Hoodies"],
["Swimming Shirt", "Socks", "Sweatshirts"],
["Swimming Shirt", "Rash Guard", "Dry Fit V-Neck", "Hoodies", "Tech Pants"],
["Swimming Shirt", "Rash Guard", "Dry Fit V-Neck"],
["Swimming Shirt", "Rash Guard", "Dry Fit V-Neck"],
["Running Shoe", "Swimming Shirt", "Socks", "Sweatshirts", "Modern Pants", "Soccer Shoe", "Rash Guard", "Hoodies", "Tech Pants", "Dry Fit V-Neck"],
["Running Shoe", "Swimming Shirt", "Socks", "Sweatshirts", "Modern Pants", "Soccer Shoe", "Rash Guard", "Tech Pants", "Dry Fit V-Neck", "Hoodies"],
["Running Shoe", "Swimming Shirt", "Rash Guard", "Tech Pants", "Hoodies", "Dry Fit V-Neck"],
["Running Shoe", "Swimming Shirt", "Socks", "Sweatshirts", "Modern Pants", "Dry Fit V-Neck", "Rash Guard", "Tech Pants"],
["Swimming Shirt", "Soccer Shoe", "Hoodies", "Dry Fit V-Neck", "Tech Pants", "Rash Guard"],
["Running Shoe", "Socks"],
["Socks", "Sweatshirts", "Modern Pants", "Soccer Shoe", "Hoodies", "Rash Guard", "Tech Pants", "Dry Fit V-Neck"],
["Running Shoe", "Swimming Shirt", "Rash Guard"],
["Running Shoe", "Swimming Shirt", "Socks", "Sweatshirts", "Modern Pants", "Soccer Shoe", "Hoodies", "Tech Pants", "Rash Guard", "Dry Fit V-Neck"]
]

with open("nikeTransactions.csv", "w") as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(nikeData)

# %%
# Create Generic transactions from provided example:

genericData = [
["A", "B", "C"],
["A", "B", "C"],
["A", "B", "C", "D"],
["A", "B", "C", "D", "E"],
["A", "B", "D", "E"],
["A", "D", "E"],
["A", "E"],
["A", "E"],
["A", "C", "E"],
["A", "C", "E"],
["A", "C", "E"]
]

with open("genericTransactions.csv", "w") as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(genericData)

# %%
# Create Custom transactions from provided example:

customData = [
["ink", "pen", "cheese", "bag"],
["milk", "pen", "juice", "cheese"],
["milk", "juice"],
["juice", "milk", "cheese"],
["ink", "pen", "cheese", "bag"],
["milk", "pen", "juice", "cheese"],
]

with open("customTransactions.csv", "w") as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(customData)

# %%
# Sample Walmart data created with GenAI that contains 1000 transactions and 30 unique items
# This data can be used to test larger cases and examine performance

walmartData = [
["Coffee", "Chicken", "Rice", "Sauces", "Tea", "Cleaning Supplies", "Toiletries", "Snacks", "Cereal"],
["Baby Products", "Rice", "Chicken", "Tea"],
["Nuts", "Lettuce", "Ice Cream", "Beef"],
["Soda", "Milk", "Cheese", "Cereal"],
["Fruits", "Pet Food", "Frozen Foods", "Yogurt", "Snacks", "Toiletries"],
["Vegetables", "Eggs", "Fruits", "Baking Goods", "Spices", "Granola", "Yogurt", "Sauces", "Snacks", "Bacon"],
["Soda", "Condiments", "Frozen Foods", "Sauces", "Lettuce", "Beef", "Coffee"],
["Soda", "Pet Food", "Spices", "Milk", "Cookies"],
["Baby Products", "Butter", "Spices", "Tea", "Sauces", "Snacks", "Cleaning Supplies", "Cereal"],
["Vegetables", "Coffee", "Baking Goods", "Spices", "Chicken", "Grains", "Milk", "Cereal"],
["Pasta", "Baking Goods", "Frozen Foods", "Chicken", "Rice", "Tea", "Sauces", "Toiletries", "Coffee"],
["Soda", "Condiments", "Juice", "Milk", "Snacks", "Cereal"],
["Soda", "Pet Food", "Chicken", "Rice", "Sauces", "Snacks"],
["Pet Food", "Pasta", "Baking Goods", "Frozen Foods", "Cheese"],
["Baking Goods", "Bun", "Snacks", "Lettuce", "Beef"],
["Vegetables", "Baby Products", "Juice", "Ice Cream", "Tea", "Nuts", "Cereal"],
["Vegetables", "Eggs", "Butter", "Chicken", "Ice Cream", "Juice", "Cleaning Supplies", "Bacon", "Nuts"],
["Fruits", "Baking Goods", "Condiments", "Granola", "Cheese", "Ice Cream", "Juice", "Nuts"],
["Eggs", "Pasta", "Butter", "Spices", "Rice", "Cheese", "Sauces", "Milk", "Toiletries", "Cereal"],
["Vegetables", "Chicken", "Ice Cream", "Juice", "Nuts", "Chocolate Sauce"],
["Pasta", "Rice", "Cheese", "Tea", "Milk", "Cookies"],
["Pet Food", "Pasta", "Coffee", "Yogurt", "Sauces", "Toiletries", "Cereal"],
["Soda", "Baking Goods", "Condiments", "Butter", "Yogurt", "Juice", "Toiletries", "Snacks", "Nuts", "Cereal"],
["Fruits", "Vegetables", "Chicken", "Granola", "Cereal", "Juice", "Sauces", "Snacks", "Coffee"],
["Eggs", "Frozen Foods", "Toiletries", "Cleaning Supplies", "Bacon"],
["Fruits", "Pasta", "Granola", "Sauces", "Toiletries", "Nuts"],
["Vegetables", "Bread", "Butter", "Spices", "Cheese", "Tea", "Milk", "Toiletries", "Nuts", "Cereal"],
["Vegetables", "Pet Food", "Baking Goods", "Frozen Foods", "Rice", "Juice", "Sauces", "Milk", "Cereal"],
["Eggs", "Cheese", "Baking Goods", "Yogurt"],
["Baby Products", "Eggs", "Bread", "Butter", "Cheese", "Sauces", "Jam", "Coffee"],
["Baby Products", "Spices", "Bun", "Rice", "Beef"],
["Soda", "Pasta", "Frozen Foods", "Chicken", "Rice", "Sauces", "Coffee"],
["Baby Products", "Baking Goods", "Butter", "Rice", "Milk", "Nuts", "Cereal"],
["Grains", "Ice Cream", "Juice", "Tea", "Chocolate Sauce"],
["Vegetables", "Fruits", "Granola", "Grains", "Yogurt", "Coffee"],
["Toiletries", "Cereal", "Butter", "Baking Goods"],
["Bread", "Bun", "Rice", "Jam", "Beef"],
["Soda", "Bread", "Condiments", "Butter", "Cereal", "Ice Cream", "Milk", "Jam", "Nuts", "Coffee"],
["Vegetables", "Soda", "Baking Goods", "Frozen Foods", "Grains", "Milk", "Snacks", "Cleaning Supplies", "Cereal", "Cookies"],
["Baby Products", "Pasta", "Eggs", "Grains", "Cheese", "Milk", "Cleaning Supplies", "Cookies"],
["Pet Food", "Bread", "Frozen Foods", "Spices", "Sauces", "Milk", "Cleaning Supplies", "Jam", "Coffee", "Cookies"],
["Pet Food", "Bread", "Frozen Foods", "Spices", "Butter", "Rice", "Grains", "Juice", "Tea", "Toiletries", "Coffee"],
["Fruits", "Bread", "Butter", "Yogurt", "Tea", "Sauces"],
["Chocolate Sauce", "Baking Goods", "Ice Cream", "Sauces"],
["Soda", "Fruits", "Yogurt", "Tea", "Snacks"],
["Baby Products", "Coffee", "Baking Goods", "Yogurt", "Grains", "Snacks", "Toiletries", "Cereal"],
["Milk", "Cleaning Supplies", "Cereal", "Spices"],
["Pet Food", "Snacks", "Cereal", "Tea"],
["Lettuce", "Cereal", "Beef"],
["Baby Products", "Eggs", "Bacon"],
["Butter", "Chicken", "Rice", "Cheese", "Yogurt", "Sauces", "Snacks", "Toiletries", "Nuts"],
["Vegetables", "Milk", "Cereal"],
["Soda", "Baking Goods", "Chicken", "Rice", "Yogurt", "Grains", "Toiletries"],
["Eggs", "Chicken", "Rice", "Ice Cream", "Tea", "Bacon", "Chocolate Sauce", "Coffee"],
["Bacon", "Eggs", "Nuts", "Juice"],
["Soda", "Baking Goods", "Bread", "Butter", "Lettuce", "Beef", "Cereal"],
["Pasta", "Pet Food", "Bread", "Cheese", "Jam"],
["Bun", "Rice", "Beef"],
["Fruits", "Pet Food", "Bread", "Butter", "Bun", "Granola", "Yogurt", "Cleaning Supplies", "Beef"],
["Pet Food", "Pasta", "Bread", "Yogurt", "Juice", "Sauces", "Jam"],
["Butter", "Bun", "Yogurt", "Lettuce", "Beef"],
["Vegetables", "Eggs", "Bun", "Cheese", "Toiletries", "Beef", "Bacon"],
["Soda", "Eggs", "Nuts", "Bacon"],
["Fruits", "Pet Food", "Coffee", "Granola", "Yogurt", "Sauces", "Cereal"],
["Soda", "Frozen Foods", "Bun", "Ice Cream", "Beef", "Nuts"],
["Pasta", "Yogurt", "Sauces", "Toiletries", "Nuts", "Coffee"],
["Soda", "Baby Products", "Bread", "Butter", "Ice Cream", "Toiletries", "Snacks", "Nuts"],
["Chicken", "Vegetables", "Cookies", "Milk"],
["Vegetables", "Condiments", "Juice", "Toiletries", "Nuts", "Cereal"],
["Pasta", "Baking Goods", "Frozen Foods", "Bun", "Grains", "Sauces", "Beef"],
["Eggs", "Toiletries", "Cheese"],
["Coffee", "Butter", "Rice", "Yogurt", "Milk", "Cleaning Supplies", "Nuts", "Cereal", "Cookies"],
["Soda", "Milk", "Cereal", "Vegetables"],
["Baby Products", "Eggs", "Soda", "Baking Goods", "Condiments", "Spices", "Grains", "Toiletries", "Bacon", "Cereal"],
["Baking Goods", "Condiments", "Grains", "Toiletries", "Lettuce", "Beef"],
["Baby Products", "Pet Food", "Pasta", "Juice", "Ice Cream", "Sauces", "Chocolate Sauce"],
["Baby Products", "Fruits", "Condiments", "Grains", "Yogurt", "Ice Cream", "Snacks", "Nuts"],
["Soda", "Fruits", "Butter", "Yogurt", "Snacks", "Lettuce", "Beef"],
["Vegetables", "Pet Food", "Bread", "Frozen Foods", "Butter", "Rice", "Yogurt", "Cleaning Supplies"],
["Pasta", "Eggs", "Pet Food", "Baking Goods", "Condiments", "Butter", "Cheese", "Juice", "Sauces", "Nuts"],
["Baking Goods", "Condiments", "Juice", "Snacks", "Toiletries"],
["Bun", "Pet Food", "Snacks", "Beef"],
["Baby Products", "Fruits", "Frozen Foods", "Grains", "Yogurt", "Juice", "Sauces", "Nuts"],
["Pet Food", "Bread", "Frozen Foods", "Butter", "Bun", "Beef", "Cereal"],
["Vegetables", "Pasta", "Rice", "Grains", "Sauces", "Toiletries", "Nuts", "Cereal"],
["Vegetables", "Coffee", "Milk", "Toiletries", "Cereal"],
["Fruits", "Pasta", "Chicken", "Rice", "Granola", "Cheese"],
["Fruits", "Pet Food", "Eggs", "Butter", "Granola", "Grains", "Cheese", "Juice", "Milk", "Toiletries", "Cereal"],
["Soda", "Pasta", "Butter", "Frozen Foods", "Cheese", "Nuts", "Cereal"],
["Butter", "Bun", "Milk", "Snacks", "Beef", "Cereal"],
["Soda", "Fruits", "Bread", "Butter", "Rice", "Granola", "Toiletries", "Snacks"],
["Pasta", "Pet Food", "Baking Goods", "Rice", "Sauces", "Milk", "Snacks", "Cookies"],
["Soda", "Frozen Foods", "Rice", "Yogurt", "Tea", "Toiletries", "Snacks", "Cleaning Supplies", "Lettuce", "Beef"],
["Baby Products", "Pet Food", "Bread", "Butter", "Rice", "Grains", "Yogurt", "Cleaning Supplies"],
["Eggs", "Pet Food", "Condiments", "Bread", "Cheese", "Snacks", "Cleaning Supplies", "Jam"],
["Fruits", "Vegetables", "Spices", "Granola", "Yogurt", "Tea", "Toiletries", "Snacks"],
["Fruits", "Eggs", "Soda", "Frozen Foods", "Yogurt", "Cheese", "Lettuce", "Beef"],
["Spices", "Juice", "Snacks", "Toiletries", "Nuts"],
["Vegetables", "Pet Food", "Condiments", "Butter", "Yogurt", "Ice Cream", "Nuts"],
["Grains", "Butter", "Sauces"],
["Baby Products", "Pet Food", "Cleaning Supplies"],
["Baby Products", "Pasta", "Pet Food", "Grains", "Cheese", "Sauces"],
["Fruits", "Baby Products", "Butter", "Rice", "Granola", "Lettuce", "Beef"],
["Soda", "Spices", "Rice", "Juice", "Cleaning Supplies"],
["Baby Products", "Cheese", "Toiletries", "Lettuce", "Beef"],
["Soda", "Pasta", "Cheese", "Cereal"],
["Fruits", "Cheese", "Yogurt", "Milk", "Snacks", "Lettuce", "Beef", "Cookies"],
["Vegetables", "Eggs", "Baby Products", "Soda", "Bread", "Butter", "Chicken", "Cheese"],
["Bacon", "Eggs", "Toiletries"],
["Baby Products", "Vegetables", "Soda", "Condiments", "Chicken"],
["Vegetables", "Spices", "Cereal", "Snacks", "Lettuce", "Beef", "Coffee"],
["Baby Products", "Eggs", "Spices", "Cleaning Supplies", "Snacks", "Bacon"],
["Fruits", "Pet Food", "Frozen Foods", "Butter", "Granola", "Grains", "Juice", "Nuts"],
["Fruits", "Butter", "Granola", "Nuts", "Coffee"],
["Baby Products", "Baking Goods", "Bread", "Grains", "Tea", "Jam", "Nuts"],
["Bun", "Snacks", "Beef"],
["Baking Goods", "Bread", "Butter", "Ice Cream", "Juice", "Sauces", "Toiletries", "Chocolate Sauce"],
["Soda", "Eggs", "Condiments", "Cereal", "Cheese", "Sauces", "Cleaning Supplies", "Coffee"],
["Eggs", "Butter", "Rice", "Cheese", "Sauces", "Toiletries", "Cereal"],
["Fruits", "Pet Food", "Eggs", "Bread", "Butter", "Cheese", "Yogurt", "Sauces", "Coffee"],
["Soda", "Eggs", "Baby Products", "Cheese", "Milk", "Cereal"],
["Fruits", "Baby Products", "Butter", "Bun", "Granola", "Beef", "Cereal"],
["Soda", "Pasta", "Butter", "Rice", "Cheese", "Milk", "Cereal"],
["Vegetables", "Fruits", "Pet Food", "Pasta", "Frozen Foods", "Rice", "Granola", "Cheese", "Nuts"],
["Chocolate Sauce", "Cereal", "Condiments", "Ice Cream"],
["Bun", "Tea", "Milk", "Beef", "Cereal", "Cookies"],
["Vegetables", "Eggs", "Condiments", "Bread", "Chicken", "Cheese", "Juice", "Jam"],
["Eggs", "Baking Goods", "Cereal", "Tea", "Milk", "Bacon", "Coffee"],
["Butter", "Rice", "Juice", "Milk", "Cereal"],
["Vegetables", "Eggs", "Frozen Foods", "Cheese", "Ice Cream", "Sauces", "Bacon", "Nuts"],
["Baking Goods", "Condiments", "Juice"],
["Snacks", "Bread", "Butter", "Spices"],
["Bread", "Butter", "Condiments", "Chicken", "Rice", "Cheese", "Sauces", "Tea", "Cleaning Supplies", "Jam"],
["Vegetables", "Butter", "Grains", "Tea", "Cleaning Supplies"],
["Vegetables", "Pasta", "Chicken", "Yogurt", "Cheese", "Juice", "Milk", "Snacks", "Cereal"],
["Bread", "Butter", "Grains", "Ice Cream", "Sauces", "Milk", "Nuts", "Chocolate Sauce", "Cereal", "Cookies"],
["Vegetables", "Baking Goods", "Condiments", "Frozen Foods", "Chicken", "Rice", "Juice", "Snacks", "Cereal"],
["Vegetables", "Eggs", "Baking Goods", "Spices", "Chicken", "Cheese", "Milk", "Bacon", "Nuts", "Cookies"],
["Nuts", "Grains", "Yogurt", "Frozen Foods"],
["Fruits", "Vegetables", "Pasta", "Yogurt", "Cheese", "Ice Cream", "Sauces", "Milk", "Nuts", "Coffee", "Cookies"],
["Pet Food", "Condiments", "Frozen Foods", "Bun", "Grains", "Beef", "Nuts"],
["Coffee", "Yogurt", "Bread", "Butter"],
["Baking Goods", "Rice", "Ice Cream", "Chocolate Sauce", "Coffee"],
["Milk", "Cheese", "Cereal", "Eggs"],
["Baby Products", "Tea", "Milk", "Coffee", "Cookies"],
["Vegetables", "Fruits", "Pasta", "Pet Food", "Frozen Foods", "Butter", "Chicken", "Yogurt", "Grains", "Sauces"],
["Vegetables", "Baby Products", "Ice Cream", "Snacks", "Chocolate Sauce", "Cereal"],
["Fruits", "Pet Food", "Condiments", "Granola", "Cheese", "Yogurt", "Toiletries", "Snacks", "Nuts", "Coffee"],
["Vegetables", "Lettuce", "Yogurt", "Beef"],
["Vegetables", "Baby Products", "Ice Cream", "Sauces", "Milk", "Toiletries", "Nuts", "Cookies"],
["Baby Products", "Vegetables", "Pasta", "Chicken", "Rice", "Cheese", "Juice", "Sauces", "Coffee"],
["Soda", "Chicken", "Rice", "Milk", "Nuts", "Cereal"],
["Eggs", "Condiments", "Bread", "Butter", "Cleaning Supplies", "Jam", "Bacon", "Nuts"],
["Eggs", "Bread", "Butter", "Grains", "Jam", "Bacon", "Coffee"],
["Pet Food", "Pasta", "Condiments", "Chicken", "Rice", "Cheese", "Sauces", "Snacks"],
["Soda", "Coffee", "Baking Goods"],
["Soda", "Eggs", "Spices", "Bun", "Cheese", "Tea", "Snacks", "Beef"],
["Vegetables", "Pet Food", "Snacks", "Tea"],
["Bread", "Grains", "Sauces", "Cleaning Supplies", "Jam"],
["Bread", "Rice", "Cheese", "Jam", "Cereal"],
["Snacks", "Baking Goods", "Spices"],
["Nuts", "Cleaning Supplies", "Baking Goods", "Sauces"],
["Fruits", "Eggs", "Bun", "Granola", "Cheese", "Beef"],
["Eggs", "Condiments", "Butter", "Rice", "Cheese", "Milk", "Bacon", "Cookies"],
["Vegetables", "Eggs", "Condiments", "Grains", "Cheese", "Sauces", "Tea", "Toiletries", "Nuts"],
["Baby Products", "Pet Food", "Spices", "Yogurt", "Toiletries", "Cleaning Supplies"],
["Eggs", "Pet Food", "Bread", "Butter", "Cereal", "Sauces", "Milk", "Bacon", "Coffee"],
["Pasta", "Condiments", "Butter", "Frozen Foods", "Bun", "Cheese", "Beef"],
["Pasta", "Pet Food", "Condiments", "Juice", "Sauces", "Cleaning Supplies", "Cereal"],
["Vegetables", "Rice", "Cheese"],
["Eggs", "Bread", "Butter", "Cheese", "Tea", "Jam"],
["Nuts", "Coffee", "Ice Cream"],
["Pet Food", "Eggs", "Baking Goods", "Butter", "Rice", "Tea", "Toiletries", "Bacon", "Nuts", "Cereal"],
["Pet Food", "Eggs", "Baking Goods", "Frozen Foods", "Rice", "Cheese", "Ice Cream", "Bacon", "Chocolate Sauce"],
["Baby Products", "Pasta", "Bread", "Cheese", "Jam"],
["Soda", "Eggs", "Baby Products", "Vegetables", "Baking Goods", "Bread", "Butter", "Condiments", "Grains", "Bacon"],
["Rice", "Bread", "Butter"],
["Baby Products", "Pasta", "Ice Cream", "Sauces", "Cleaning Supplies", "Nuts"],
["Soda", "Bread", "Frozen Foods", "Butter", "Yogurt", "Jam"],
["Soda", "Vegetables", "Baking Goods", "Bread", "Butter", "Bun", "Cheese", "Jam", "Beef", "Nuts"],
["Nuts", "Coffee", "Ice Cream", "Tea"],
["Frozen Foods", "Grains", "Ice Cream", "Tea", "Juice", "Cleaning Supplies", "Snacks", "Nuts", "Cereal"],
["Vegetables", "Eggs", "Baking Goods", "Cereal", "Grains", "Cheese", "Snacks", "Bacon", "Coffee"],
["Fruits", "Granola", "Coffee", "Spices"],
["Pasta", "Bread", "Butter", "Bun", "Sauces", "Beef"],
["Sauces", "Frozen Foods", "Tea"],
["Soda", "Pet Food", "Condiments", "Ice Cream", "Toiletries", "Chocolate Sauce"],
["Eggs", "Baking Goods", "Rice", "Cheese", "Bacon", "Nuts", "Coffee"],
["Vegetables", "Milk", "Toiletries", "Cereal"],
["Pet Food", "Bread", "Grains", "Ice Cream", "Snacks", "Jam", "Nuts"],
["Nuts", "Cheese", "Baking Goods", "Ice Cream"],
["Fruits", "Vegetables", "Pasta", "Condiments", "Chicken", "Yogurt", "Grains", "Cheese", "Nuts", "Coffee"],
["Soda", "Bread", "Spices", "Juice", "Sauces", "Jam"],
["Pasta", "Baking Goods", "Bread", "Tea", "Sauces", "Snacks", "Jam"],
["Eggs", "Chicken", "Rice", "Ice Cream", "Milk", "Bacon", "Nuts", "Cereal"],
["Fruits", "Pasta", "Bread", "Butter", "Granola", "Grains", "Sauces"],
["Fruits", "Pasta", "Baking Goods", "Bread", "Butter", "Granola", "Yogurt", "Cheese", "Ice Cream", "Chocolate Sauce"],
["Lettuce", "Butter", "Beef"],
["Vegetables", "Soda", "Baby Products", "Frozen Foods", "Chicken", "Rice", "Sauces"],
["Baby Products", "Eggs", "Condiments", "Frozen Foods", "Butter", "Cheese", "Sauces", "Toiletries", "Snacks", "Cereal"],
["Frozen Foods", "Butter", "Rice", "Ice Cream", "Chocolate Sauce", "Cereal"],
["Fruits", "Frozen Foods", "Spices", "Yogurt", "Ice Cream", "Snacks", "Toiletries", "Nuts", "Coffee"],
["Fruits", "Granola", "Yogurt", "Ice Cream", "Nuts", "Chocolate Sauce"],
["Condiments", "Spices", "Cheese", "Tea", "Toiletries", "Cereal"],
["Vegetables", "Eggs", "Juice", "Tea", "Ice Cream", "Bacon", "Chocolate Sauce"],
["Vegetables", "Baking Goods", "Bread", "Butter", "Chicken", "Grains", "Cleaning Supplies"],
["Soda", "Yogurt", "Condiments", "Butter"],
["Baby Products", "Toiletries", "Cheese", "Frozen Foods"],
["Baby Products", "Eggs", "Fruits", "Granola", "Ice Cream", "Cleaning Supplies", "Snacks", "Bacon", "Chocolate Sauce"],
["Nuts", "Chocolate Sauce", "Ice Cream"],
["Baby Products", "Pasta", "Bread", "Butter", "Spices", "Cheese", "Jam", "Nuts"],
["Bun", "Baking Goods", "Beef"],
["Fruits", "Milk", "Yogurt", "Cookies"],
["Fruits", "Toiletries", "Granola", "Frozen Foods"],
["Soda", "Condiments", "Bun", "Tea", "Milk", "Snacks", "Beef", "Cereal"],
["Baby Products", "Fruits", "Soda", "Granola", "Tea", "Snacks", "Toiletries"],
["Baby Products", "Soda", "Baking Goods", "Juice", "Sauces", "Milk", "Snacks", "Nuts", "Cookies"],
["Eggs", "Frozen Foods", "Butter", "Rice", "Yogurt", "Cleaning Supplies", "Toiletries", "Bacon"],
["Pasta", "Pet Food", "Frozen Foods", "Butter", "Spices", "Cheese", "Cleaning Supplies", "Nuts", "Coffee"],
["Soda", "Fruits", "Coffee", "Grains", "Yogurt", "Ice Cream", "Sauces", "Milk", "Nuts", "Cereal"],
["Baby Products", "Snacks", "Juice"],
["Baking Goods", "Bread", "Butter", "Milk", "Snacks", "Cereal"],
["Fruits", "Pasta", "Baby Products", "Pet Food", "Soda", "Spices", "Granola", "Cheese", "Tea"],
["Vegetables", "Eggs", "Pasta", "Butter", "Rice", "Sauces", "Bacon"],
["Fruits", "Baking Goods", "Bread", "Butter", "Yogurt", "Milk", "Cereal"],
["Soda", "Baking Goods", "Frozen Foods", "Juice", "Sauces", "Snacks"],
["Fruits", "Spices", "Granola", "Lettuce", "Beef"],
["Vegetables", "Fruits", "Spices", "Yogurt", "Milk", "Snacks", "Cereal"],
["Vegetables", "Pet Food", "Pasta", "Baby Products", "Condiments", "Butter", "Cheese", "Tea", "Cereal"],
["Soda", "Pasta", "Vegetables", "Condiments", "Sauces", "Milk", "Cleaning Supplies", "Toiletries", "Cereal"],
["Vegetables", "Fruits", "Pet Food", "Spices", "Yogurt", "Tea", "Coffee"],
["Fruits", "Pasta", "Pet Food", "Baking Goods", "Yogurt", "Juice", "Sauces", "Milk", "Cereal"],
["Baby Products", "Soda", "Condiments", "Frozen Foods", "Yogurt"],
["Bread", "Spices", "Chicken", "Rice", "Cheese", "Jam", "Nuts"],
["Baby Products", "Pasta", "Bun", "Rice", "Cheese", "Yogurt", "Beef"],
["Bread", "Butter", "Ice Cream", "Sauces", "Milk", "Toiletries", "Chocolate Sauce", "Cookies"],
["Fruits", "Eggs", "Soda", "Condiments", "Granola", "Cheese", "Milk", "Cookies"],
["Fruits", "Pet Food", "Baking Goods", "Bread", "Butter", "Spices", "Granola", "Cleaning Supplies", "Snacks", "Nuts", "Cereal"],
["Soda", "Baby Products", "Eggs", "Juice", "Tea", "Toiletries", "Bacon", "Cereal"],
["Eggs", "Ice Cream", "Cleaning Supplies", "Bacon", "Nuts"],
["Eggs", "Coffee", "Cereal", "Cheese"],
["Eggs", "Pasta", "Bun", "Cheese", "Snacks", "Beef", "Bacon", "Cereal"],
["Vegetables", "Eggs", "Baking Goods", "Bread", "Frozen Foods", "Butter", "Chicken", "Cheese", "Tea", "Bacon"],
["Pet Food", "Chicken", "Rice", "Cheese", "Grains", "Snacks", "Toiletries"],
["Soda", "Vegetables", "Condiments", "Rice", "Ice Cream", "Lettuce", "Beef", "Nuts", "Cereal"],
["Fruits", "Granola", "Ice Cream", "Milk", "Chocolate Sauce", "Cereal"],
["Bread", "Cheese", "Yogurt", "Juice", "Toiletries", "Jam", "Nuts", "Cereal"],
["Soda", "Baby Products", "Vegetables", "Bread", "Butter", "Chicken", "Rice", "Toiletries", "Cereal"],
["Bun", "Cleaning Supplies", "Yogurt", "Beef"],
["Cereal", "Yogurt", "Sauces", "Milk", "Snacks", "Nuts", "Coffee"],
["Baby Products", "Pasta", "Ice Cream", "Sauces", "Cleaning Supplies", "Chocolate Sauce"],
["Butter", "Rice", "Condiments", "Frozen Foods"],
["Soda", "Fruits", "Bun", "Granola", "Cheese", "Sauces", "Tea", "Beef", "Nuts", "Cereal"],
["Fruits", "Baby Products", "Vegetables", "Butter", "Chicken", "Rice", "Granola", "Juice", "Tea", "Toiletries"],
["Soda", "Pet Food", "Milk", "Snacks", "Cleaning Supplies", "Cookies"],
["Eggs", "Baking Goods", "Butter", "Rice", "Cheese"],
["Nuts", "Bread", "Butter"],
["Toiletries", "Butter", "Sauces"],
["Condiments", "Butter", "Frozen Foods", "Milk", "Toiletries", "Cereal"],
["Soda", "Baking Goods", "Bread", "Butter", "Tea", "Milk", "Cereal"],
["Chicken", "Rice", "Vegetables", "Condiments"],
["Eggs", "Butter", "Rice", "Cheese", "Ice Cream", "Milk", "Toiletries", "Nuts", "Cereal"],
["Vegetables", "Pasta", "Cheese", "Snacks", "Coffee"],
["Chicken", "Vegetables", "Lettuce", "Beef"],
["Fruits", "Spices", "Granola", "Cheese", "Toiletries"],
["Vegetables", "Pet Food", "Spices", "Chicken", "Rice", "Cheese", "Sauces", "Milk", "Snacks", "Cereal"],
["Fruits", "Vegetables", "Chicken", "Rice", "Grains", "Yogurt", "Milk", "Cleaning Supplies", "Cereal", "Cookies"],
["Vegetables", "Butter", "Chicken", "Rice", "Cereal", "Tea", "Milk", "Cleaning Supplies", "Coffee"],
["Soda", "Pasta", "Condiments", "Butter", "Rice", "Cheese", "Tea"],
["Baby Products", "Chicken", "Rice", "Snacks", "Cereal"],
["Eggs", "Pasta", "Bun", "Cheese", "Tea", "Milk", "Beef", "Bacon", "Cereal"],
["Baby Products", "Nuts", "Cleaning Supplies", "Condiments"],
["Eggs", "Pet Food", "Cheese"],
["Pasta", "Toiletries", "Cheese", "Frozen Foods"],
["Butter", "Spices", "Rice", "Nuts", "Coffee"],
["Nuts", "Yogurt", "Ice Cream", "Tea"],
["Fruits", "Vegetables", "Condiments", "Spices", "Granola", "Yogurt", "Tea", "Milk", "Cereal"],
["Soda", "Eggs", "Cheese", "Lettuce", "Beef", "Coffee"],
["Vegetables", "Baking Goods", "Frozen Foods", "Yogurt", "Juice", "Nuts"],
["Fruits", "Condiments", "Butter", "Granola", "Cleaning Supplies"],
["Pet Food", "Eggs", "Bread", "Butter", "Cheese", "Ice Cream", "Snacks", "Lettuce", "Beef", "Nuts"],
["Pasta", "Pet Food", "Eggs", "Cheese", "Ice Cream", "Bacon", "Nuts", "Chocolate Sauce"],
["Pasta", "Butter", "Bun", "Grains", "Cheese", "Tea", "Beef", "Nuts"],
["Fruits", "Eggs", "Frozen Foods", "Granola", "Grains", "Tea", "Cleaning Supplies", "Bacon"],
["Pasta", "Condiments", "Cheese", "Ice Cream", "Nuts"],
["Eggs", "Condiments", "Bread", "Butter", "Juice", "Snacks", "Bacon", "Coffee"],
["Vegetables", "Pasta", "Chicken", "Rice", "Ice Cream", "Sauces", "Nuts"],
["Vegetables", "Baking Goods", "Bread", "Butter", "Spices", "Chicken", "Rice", "Cheese", "Snacks", "Nuts"],
["Spices", "Grains", "Tea", "Cleaning Supplies", "Nuts"],
["Condiments", "Butter", "Grains", "Ice Cream", "Snacks", "Chocolate Sauce"],
["Baby Products", "Pasta", "Coffee", "Condiments", "Cheese", "Grains", "Snacks", "Cereal"],
["Vegetables", "Baking Goods", "Butter", "Spices", "Sauces"],
["Baking Goods", "Coffee", "Tea"],
["Vegetables", "Frozen Foods", "Ice Cream", "Milk", "Chocolate Sauce", "Cereal"],
["Pasta", "Eggs", "Baking Goods", "Grains", "Cheese", "Juice", "Tea", "Bacon", "Nuts", "Cereal"],
["Fruits", "Baby Products", "Baking Goods", "Butter", "Rice", "Granola", "Juice", "Cleaning Supplies"],
["Eggs", "Rice", "Cheese", "Juice", "Toiletries", "Cereal"],
["Soda", "Vegetables", "Pet Food", "Chicken", "Rice", "Bun", "Cheese", "Cleaning Supplies", "Beef", "Cereal"],
["Soda", "Eggs", "Baking Goods", "Bread", "Butter", "Spices", "Tea", "Milk", "Toiletries", "Bacon", "Cookies"],
["Tea", "Yogurt", "Juice", "Spices"],
["Chocolate Sauce", "Ice Cream", "Spices"],
["Milk", "Toiletries", "Nuts", "Coffee", "Cookies"],
["Soda", "Baby Products", "Pasta", "Spices", "Rice", "Cheese", "Juice", "Cleaning Supplies", "Lettuce", "Beef"],
["Bread", "Condiments", "Snacks", "Jam", "Nuts", "Coffee"],
["Eggs", "Cheese", "Juice", "Tea", "Toiletries"],
["Eggs", "Rice", "Cheese", "Juice", "Sauces", "Milk", "Bacon", "Cereal"],
["Bacon", "Eggs", "Butter"],
["Pet Food", "Pasta", "Frozen Foods", "Spices", "Cheese", "Ice Cream", "Sauces", "Toiletries", "Chocolate Sauce"],
["Snacks", "Cereal", "Grains", "Spices"],
["Pasta", "Baking Goods", "Bread", "Butter", "Spices", "Rice", "Sauces", "Toiletries"],
["Pet Food", "Jam", "Bread"],
["Baby Products", "Milk", "Cleaning Supplies", "Cookies"],
["Soda", "Cheese", "Ice Cream", "Sauces", "Tea", "Cleaning Supplies", "Snacks", "Chocolate Sauce", "Coffee"],
["Vegetables", "Pasta", "Baby Products", "Eggs", "Frozen Foods", "Cheese", "Sauces"],
["Pasta", "Chicken", "Rice", "Cheese", "Sauces"],
["Nuts", "Frozen Foods", "Butter"],
["Pet Food", "Chicken", "Rice", "Cheese", "Sauces"],
["Butter", "Frozen Foods", "Spices", "Yogurt", "Milk", "Cereal"],
["Chicken", "Vegetables", "Baking Goods"],
["Soda", "Grains", "Yogurt", "Sauces", "Cleaning Supplies", "Cereal"],
["Condiments", "Frozen Foods", "Chicken", "Rice", "Milk", "Cleaning Supplies", "Cookies"],
["Soda", "Rice", "Grains", "Ice Cream", "Chocolate Sauce", "Coffee"],
["Bread", "Butter", "Bun", "Tea", "Beef"],
["Fruits", "Baking Goods", "Frozen Foods", "Rice", "Granola", "Lettuce", "Beef"],
["Nuts", "Baking Goods", "Ice Cream"],
["Soda", "Eggs", "Baking Goods", "Bread", "Butter", "Spices", "Juice", "Bacon"],
["Pet Food", "Bread", "Butter", "Bun", "Yogurt", "Ice Cream", "Toiletries", "Snacks", "Beef", "Chocolate Sauce"],
["Soda", "Vegetables", "Eggs", "Bread", "Frozen Foods", "Yogurt", "Cleaning Supplies", "Toiletries", "Jam", "Bacon"],
["Baking Goods", "Tea", "Milk", "Toiletries", "Cookies"],
["Rice", "Toiletries", "Cheese", "Snacks"],
["Butter", "Sauces", "Tea", "Toiletries", "Nuts"],
["Vegetables", "Baking Goods", "Chicken", "Lettuce", "Beef", "Coffee"],
["Grains", "Chocolate Sauce", "Coffee", "Ice Cream"],
["Pasta", "Bread", "Condiments", "Yogurt", "Cheese", "Sauces", "Tea", "Jam", "Cereal"],
["Baby Products", "Pasta", "Eggs", "Baking Goods", "Frozen Foods", "Butter", "Cheese", "Sauces", "Snacks", "Toiletries"],
["Fruits", "Pet Food", "Condiments", "Bread", "Butter", "Rice", "Cheese", "Yogurt", "Cereal"],
["Baby Products", "Pet Food", "Soda", "Butter", "Yogurt", "Cheese", "Ice Cream", "Sauces", "Tea", "Nuts"],
["Soda", "Vegetables", "Baby Products", "Pet Food", "Butter", "Juice", "Snacks", "Nuts"],
["Pasta", "Butter", "Cheese", "Milk", "Snacks", "Nuts", "Cookies"],
["Baby Products", "Frozen Foods", "Rice", "Cheese", "Yogurt", "Milk", "Toiletries", "Nuts", "Cookies"],
["Pet Food", "Spices", "Cheese", "Ice Cream", "Nuts", "Coffee"],
["Fruits", "Spices", "Rice", "Yogurt", "Toiletries"],
["Baby Products", "Chicken", "Rice", "Yogurt", "Sauces", "Toiletries"],
["Soda", "Pet Food", "Butter", "Bun", "Grains", "Ice Cream", "Toiletries", "Beef", "Chocolate Sauce"],
["Pasta", "Eggs", "Cheese", "Yogurt", "Sauces", "Bacon"],
["Eggs", "Spices", "Yogurt", "Cheese", "Sauces", "Bacon", "Cereal"],
["Nuts", "Grains", "Ice Cream"],
["Chicken", "Vegetables", "Cleaning Supplies", "Nuts"],
["Soda", "Baby Products", "Pasta", "Bun", "Cheese", "Ice Cream", "Beef", "Chocolate Sauce", "Coffee"],
["Fruits", "Pet Food", "Granola", "Cereal"],
["Baking Goods", "Bun", "Rice", "Juice", "Sauces", "Milk", "Toiletries", "Beef", "Cookies"],
["Soda", "Vegetables", "Rice", "Ice Cream", "Juice", "Chocolate Sauce"],
["Vegetables", "Eggs", "Soda", "Baking Goods", "Butter", "Spices", "Bun", "Cleaning Supplies", "Beef", "Bacon"],
["Pet Food", "Butter", "Chicken", "Rice", "Yogurt", "Grains", "Sauces", "Toiletries", "Cereal"],
["Coffee", "Cheese", "Butter"],
["Soda", "Juice", "Toiletries", "Lettuce", "Cleaning Supplies", "Beef", "Nuts"],
["Soda", "Spices", "Rice", "Yogurt", "Sauces", "Cleaning Supplies"],
["Vegetables", "Soda", "Chicken", "Bun", "Rice", "Snacks", "Beef"],
["Fruits", "Pasta", "Butter", "Granola", "Cheese", "Yogurt"],
["Eggs", "Bun", "Grains", "Cleaning Supplies", "Beef", "Bacon", "Nuts", "Cereal"],
["Condiments", "Frozen Foods", "Sauces", "Toiletries", "Lettuce", "Beef"],
["Condiments", "Bread", "Rice", "Sauces", "Toiletries", "Snacks", "Cleaning Supplies", "Jam", "Nuts"],
["Fruits", "Eggs", "Granola", "Cheese", "Juice", "Toiletries"],
["Vegetables", "Eggs", "Bread", "Butter", "Chicken", "Cheese", "Ice Cream", "Tea", "Chocolate Sauce"],
["Soda", "Pasta", "Spices", "Chicken", "Rice", "Sauces", "Milk", "Cereal"],
["Chicken", "Vegetables", "Rice"],
["Nuts", "Cheese", "Frozen Foods", "Sauces"],
["Eggs", "Cheese", "Ice Cream", "Sauces", "Snacks", "Lettuce", "Beef", "Chocolate Sauce"],
["Baby Products", "Pasta", "Condiments", "Sauces", "Coffee"],
["Chicken", "Rice", "Bun", "Beef"],
["Vegetables", "Pasta", "Butter", "Cheese", "Lettuce", "Beef"],
["Vegetables", "Chicken", "Cheese", "Ice Cream", "Milk", "Snacks", "Cleaning Supplies", "Nuts", "Cookies"],
["Baby Products", "Pasta", "Bread", "Butter", "Cheese", "Grains", "Juice", "Jam", "Nuts", "Cereal"],
["Fruits", "Butter", "Spices", "Chicken", "Rice", "Yogurt", "Nuts", "Coffee"],
["Fruits", "Eggs", "Spices", "Yogurt", "Grains", "Juice", "Milk", "Cleaning Supplies", "Bacon", "Cookies"],
["Vegetables", "Pet Food", "Condiments", "Frozen Foods", "Chicken", "Rice", "Cheese", "Yogurt", "Toiletries"],
["Baby Products", "Pasta", "Bread", "Butter", "Cheese", "Ice Cream", "Tea", "Chocolate Sauce"],
["Vegetables", "Baking Goods", "Butter", "Spices", "Rice", "Yogurt", "Sauces", "Tea", "Coffee"],
["Nuts", "Grains", "Ice Cream", "Tea"],
["Vegetables", "Pasta", "Chicken", "Rice", "Cheese", "Sauces", "Tea"],
["Fruits", "Pasta", "Vegetables", "Chicken", "Granola", "Cheese", "Cleaning Supplies"],
["Butter", "Chocolate Sauce", "Ice Cream"],
["Soda", "Baking Goods", "Bread", "Frozen Foods", "Spices", "Yogurt", "Juice", "Cleaning Supplies", "Snacks", "Jam"],
["Vegetables", "Rice", "Cereal", "Baking Goods"],
["Fruits", "Condiments", "Spices", "Granola", "Ice Cream", "Toiletries", "Nuts"],
["Eggs", "Pasta", "Baking Goods", "Frozen Foods", "Yogurt", "Sauces", "Bacon"],
["Vegetables", "Soda", "Butter", "Chicken", "Ice Cream", "Snacks", "Nuts", "Chocolate Sauce"],
["Pasta", "Condiments", "Frozen Foods", "Sauces", "Coffee"],
["Soda", "Condiments", "Yogurt", "Juice", "Sauces", "Tea", "Snacks", "Toiletries", "Cleaning Supplies", "Cereal"],
["Fruits", "Pet Food", "Condiments", "Frozen Foods", "Rice", "Cheese", "Grains", "Yogurt", "Tea"],
["Eggs", "Spices", "Rice", "Ice Cream", "Tea", "Sauces", "Toiletries", "Bacon", "Nuts", "Coffee"],
["Fruits", "Pet Food", "Bread", "Butter", "Yogurt", "Grains", "Juice", "Cleaning Supplies", "Nuts"],
["Vegetables", "Bread", "Butter", "Condiments", "Chicken", "Rice", "Snacks", "Toiletries"],
["Vegetables", "Soda", "Baking Goods", "Bread", "Butter", "Cheese", "Grains", "Sauces", "Snacks"],
["Pasta", "Eggs", "Cheese", "Grains", "Sauces"],
["Fruits", "Pet Food", "Pasta", "Coffee", "Vegetables", "Yogurt", "Sauces", "Cereal"],
["Vegetables", "Bread", "Condiments", "Juice", "Sauces", "Snacks", "Jam"],
["Vegetables", "Pasta", "Condiments", "Frozen Foods", "Spices", "Chicken", "Rice", "Cheese", "Nuts", "Cereal"],
["Fruits", "Bread", "Frozen Foods", "Rice", "Granola", "Tea", "Milk", "Jam", "Cereal"],
["Pet Food", "Cleaning Supplies", "Frozen Foods"],
["Baby Products", "Baking Goods", "Condiments", "Cleaning Supplies", "Lettuce", "Beef"],
["Baking Goods", "Frozen Foods", "Grains", "Milk", "Toiletries", "Coffee", "Cookies"],
["Soda", "Rice", "Condiments"],
["Bread", "Butter", "Cheese", "Tea", "Snacks", "Cereal"],
["Pet Food", "Coffee", "Eggs", "Rice", "Cheese", "Sauces", "Milk", "Bacon", "Cereal", "Cookies"],
["Bread", "Butter", "Ice Cream", "Tea", "Chocolate Sauce"],
["Bread", "Butter", "Rice", "Ice Cream", "Sauces", "Snacks", "Lettuce", "Beef", "Nuts"],
["Fruits", "Pasta", "Baking Goods", "Rice", "Cheese", "Yogurt"],
["Fruits", "Baking Goods", "Frozen Foods", "Yogurt", "Tea", "Cleaning Supplies"],
["Rice", "Cereal", "Yogurt", "Milk", "Coffee"],
["Coffee", "Frozen Foods", "Yogurt", "Tea", "Nuts", "Cereal"],
["Baby Products", "Pasta", "Vegetables", "Fruits", "Spices", "Grains", "Cheese", "Yogurt", "Milk", "Cereal"],
["Vegetables", "Eggs", "Pasta", "Grains", "Cheese", "Sauces", "Cleaning Supplies", "Bacon", "Nuts"],
["Vegetables", "Condiments", "Chicken", "Milk", "Cleaning Supplies", "Lettuce", "Beef", "Cereal"],
["Soda", "Baby Products", "Rice", "Yogurt", "Snacks", "Cereal"],
["Pet Food", "Bread", "Butter", "Rice", "Cheese", "Ice Cream", "Nuts", "Cereal"],
["Fruits", "Coffee", "Chicken", "Rice", "Yogurt", "Sauces", "Milk", "Nuts", "Cereal"],
["Baking Goods", "Bread", "Yogurt", "Ice Cream", "Jam", "Chocolate Sauce"],
["Fruits", "Pet Food", "Baby Products", "Frozen Foods", "Spices", "Yogurt", "Milk", "Cereal"],
["Rice", "Grains", "Cereal", "Tea"],
["Baby Products", "Coffee", "Cereal", "Frozen Foods"],
["Fruits", "Eggs", "Spices", "Yogurt", "Cheese", "Milk", "Cereal", "Cookies"],
["Baby Products", "Eggs", "Condiments", "Frozen Foods", "Rice", "Cereal", "Juice", "Milk", "Bacon", "Coffee"],
["Butter", "Toiletries", "Frozen Foods"],
["Soda", "Pet Food", "Vegetables", "Frozen Foods", "Tea", "Nuts", "Coffee"],
["Fruits", "Pet Food", "Soda", "Rice", "Granola", "Yogurt", "Juice", "Sauces", "Snacks", "Cereal"],
["Snacks", "Cereal", "Spices"],
["Pet Food", "Butter", "Frozen Foods", "Rice", "Ice Cream", "Chocolate Sauce", "Cereal"],
["Bread", "Butter", "Bun", "Snacks", "Beef"],
["Fruits", "Bread", "Butter", "Granola", "Yogurt", "Grains", "Juice", "Tea", "Jam"],
["Vegetables", "Condiments", "Frozen Foods", "Chicken", "Toiletries", "Lettuce", "Beef"],
["Soda", "Vegetables", "Butter", "Frozen Foods", "Bun", "Chicken", "Cleaning Supplies", "Lettuce", "Beef", "Cereal"],
["Eggs", "Pasta", "Frozen Foods", "Rice", "Cheese", "Bacon", "Nuts", "Coffee"],
["Soda", "Pet Food", "Spices", "Ice Cream", "Cleaning Supplies", "Nuts"],
["Soda", "Pet Food", "Baking Goods", "Spices", "Chicken", "Rice", "Cereal"],
["Nuts", "Eggs", "Cheese", "Ice Cream"],
["Fruits", "Eggs", "Pet Food", "Baking Goods", "Granola", "Cheese", "Juice", "Toiletries", "Nuts"],
["Pasta", "Butter", "Yogurt", "Grains", "Cheese", "Juice", "Sauces", "Cereal"],
["Vegetables", "Jam", "Bread", "Frozen Foods"],
["Vegetables", "Soda", "Chicken", "Grains", "Milk", "Snacks", "Toiletries", "Cereal"],
["Fruits", "Rice", "Yogurt", "Juice", "Cleaning Supplies", "Coffee"],
["Cereal", "Lettuce", "Juice", "Beef"],
["Pet Food", "Eggs", "Baking Goods", "Condiments", "Butter", "Bacon"],
["Vegetables", "Frozen Foods", "Butter", "Chicken", "Rice", "Spices"],
["Soda", "Pet Food", "Bacon", "Eggs"],
["Baby Products", "Vegetables", "Fruits", "Butter", "Frozen Foods", "Granola", "Yogurt", "Sauces", "Cleaning Supplies"],
["Baby Products", "Rice", "Grains", "Ice Cream", "Milk", "Lettuce", "Beef", "Nuts", "Cereal"],
["Vegetables", "Bread", "Butter", "Chicken", "Toiletries", "Snacks", "Jam"],
["Pasta", "Pet Food", "Frozen Foods", "Juice", "Sauces", "Toiletries", "Snacks", "Coffee"],
["Nuts", "Frozen Foods", "Ice Cream"],
["Vegetables", "Fruits", "Soda", "Cheese", "Yogurt", "Ice Cream", "Chocolate Sauce", "Cereal"],
["Vegetables", "Fruits", "Eggs", "Granola", "Juice", "Toiletries", "Cleaning Supplies", "Lettuce", "Beef", "Bacon", "Cereal"],
["Baking Goods", "Bread", "Frozen Foods", "Spices", "Cheese", "Sauces", "Jam", "Cereal"],
["Pasta", "Bread", "Bun", "Yogurt", "Sauces", "Jam", "Beef"],
["Soda", "Baking Goods", "Butter", "Frozen Foods", "Milk", "Cereal"],
["Bacon", "Eggs", "Coffee", "Butter"],
["Vegetables", "Baking Goods", "Spices", "Rice", "Milk", "Toiletries", "Cereal", "Cookies"],
["Vegetables", "Pet Food", "Butter", "Juice", "Tea", "Cleaning Supplies"],
["Vegetables", "Eggs", "Baking Goods", "Chicken", "Sauces", "Milk", "Cleaning Supplies", "Bacon", "Nuts", "Cereal"],
["Toiletries", "Lettuce", "Beef"],
["Fruits", "Eggs", "Pasta", "Frozen Foods", "Granola", "Yogurt", "Tea", "Sauces", "Bacon"],
["Vegetables", "Bun", "Beef", "Sauces"],
["Baby Products", "Vegetables", "Eggs", "Spices", "Chicken", "Yogurt", "Juice", "Tea", "Bacon", "Nuts"],
["Chicken", "Rice", "Nuts", "Vegetables"],
["Baby Products", "Fruits", "Cereal", "Yogurt", "Cheese", "Ice Cream", "Tea", "Nuts", "Coffee"],
["Fruits", "Yogurt", "Bread", "Butter"],
["Fruits", "Granola", "Grains", "Tea"],
["Pet Food", "Toiletries", "Baking Goods", "Condiments"],
["Condiments", "Frozen Foods", "Rice", "Sauces", "Coffee"],
["Pet Food", "Rice", "Ice Cream", "Sauces", "Chocolate Sauce"],
["Vegetables", "Butter", "Rice", "Ice Cream", "Toiletries", "Chocolate Sauce"],
["Pet Food", "Bread", "Butter", "Frozen Foods", "Chicken", "Rice", "Yogurt", "Juice", "Snacks", "Cleaning Supplies"],
["Pasta", "Snacks", "Cheese", "Butter"],
["Vegetables", "Pasta", "Sauces", "Milk", "Cookies"],
["Baby Products", "Pasta", "Soda", "Vegetables", "Bread", "Butter", "Cheese", "Jam", "Coffee"],
["Eggs", "Bun", "Cheese", "Sauces", "Beef", "Cereal"],
["Condiments", "Spices", "Ice Cream", "Nuts", "Cereal"],
["Condiments", "Tea", "Milk", "Toiletries", "Coffee", "Cookies"],
["Bread", "Condiments", "Toiletries", "Jam", "Coffee"],
["Chicken", "Rice", "Grains", "Frozen Foods"],
["Vegetables", "Pet Food", "Frozen Foods", "Chicken", "Yogurt", "Juice"],
["Baby Products", "Fruits", "Condiments", "Frozen Foods", "Butter", "Granola", "Yogurt", "Ice Cream", "Nuts"],
["Vegetables", "Pet Food", "Soda", "Baby Products", "Spices", "Nuts", "Cereal"],
["Fruits", "Eggs", "Bread", "Yogurt", "Snacks", "Jam", "Bacon"],
["Nuts", "Toiletries", "Pet Food", "Snacks"],
["Soda", "Frozen Foods", "Ice Cream", "Sauces", "Tea", "Cleaning Supplies", "Chocolate Sauce", "Coffee"],
["Baby Products", "Yogurt", "Butter"],
["Soda", "Rice", "Tea"],
["Pet Food", "Grains", "Frozen Foods"],
["Pasta", "Frozen Foods", "Sauces"],
["Eggs", "Rice", "Grains", "Cheese", "Milk", "Nuts", "Cereal"],
["Fruits", "Pasta", "Baking Goods", "Cheese", "Yogurt", "Ice Cream", "Milk", "Nuts", "Chocolate Sauce", "Cereal"],
["Tea", "Nuts", "Juice", "Spices"],
["Fruits", "Baking Goods", "Yogurt", "Milk", "Cookies"],
["Vegetables", "Pet Food", "Spices", "Chicken", "Grains", "Ice Cream", "Chocolate Sauce"],
["Vegetables", "Fruits", "Butter", "Yogurt", "Ice Cream", "Cleaning Supplies", "Chocolate Sauce", "Cereal"],
["Vegetables", "Soda", "Baking Goods", "Butter", "Chicken", "Rice", "Tea", "Cleaning Supplies", "Nuts"],
["Vegetables", "Condiments", "Frozen Foods", "Bread", "Cereal", "Grains", "Milk", "Cleaning Supplies", "Jam", "Coffee"],
["Vegetables", "Baby Products", "Condiments", "Butter", "Cheese", "Yogurt", "Toiletries", "Snacks", "Nuts"],
["Snacks", "Lettuce", "Beef"],
["Baby Products", "Bread", "Butter", "Spices", "Rice", "Ice Cream", "Nuts", "Cereal"],
["Soda", "Cereal", "Grains", "Ice Cream", "Chocolate Sauce", "Coffee"],
["Pet Food", "Lettuce", "Baking Goods", "Beef"],
["Baby Products", "Bun", "Cheese", "Cleaning Supplies", "Snacks", "Beef"],
["Fruits", "Pasta", "Rice", "Granola", "Sauces", "Snacks", "Cereal"],
["Eggs", "Bread", "Frozen Foods", "Cheese", "Grains", "Sauces", "Tea", "Toiletries", "Jam"],
["Baking Goods", "Cheese", "Condiments", "Sauces"],
["Fruits", "Condiments", "Butter", "Spices", "Chicken", "Rice", "Granola", "Toiletries", "Cleaning Supplies", "Cereal"],
["Eggs", "Condiments", "Rice", "Cleaning Supplies", "Bacon", "Coffee"],
["Vegetables", "Milk", "Cookies", "Frozen Foods"],
["Soda", "Pet Food", "Fruits", "Baking Goods", "Bread", "Butter", "Granola", "Grains", "Juice", "Jam"],
["Pet Food", "Bread", "Butter", "Frozen Foods", "Ice Cream", "Tea", "Cleaning Supplies", "Chocolate Sauce"],
["Baby Products", "Baking Goods", "Spices", "Cereal", "Coffee"],
["Bread", "Butter", "Spices", "Bun", "Cheese", "Beef"],
["Fruits", "Pet Food", "Pasta", "Bun", "Yogurt", "Cheese", "Snacks", "Beef"],
["Fruits", "Cheese", "Yogurt", "Juice", "Sauces", "Tea", "Cleaning Supplies"],
["Soda", "Baby Products", "Butter", "Spices", "Rice", "Juice", "Toiletries", "Nuts"],
["Baby Products", "Pet Food", "Pasta", "Cheese", "Ice Cream", "Tea", "Sauces", "Chocolate Sauce", "Cereal"],
["Nuts", "Cleaning Supplies", "Frozen Foods"],
["Bread", "Butter", "Spices"],
["Fruits", "Pet Food", "Granola", "Grains", "Yogurt"],
["Frozen Foods", "Spices", "Butter", "Tea"],
["Spices", "Lettuce", "Beef", "Tea"],
["Soda", "Yogurt", "Cereal"],
["Sauces", "Milk", "Toiletries", "Nuts", "Cookies"],
["Fruits", "Eggs", "Pet Food", "Granola", "Juice", "Cleaning Supplies", "Snacks", "Bacon"],
["Pasta", "Baking Goods", "Bread", "Butter", "Cheese", "Sauces", "Toiletries"],
["Vegetables", "Fruits", "Condiments", "Spices", "Chicken", "Granola", "Cleaning Supplies", "Nuts"],
["Soda", "Frozen Foods", "Yogurt", "Sauces", "Lettuce", "Beef", "Coffee"],
["Baby Products", "Condiments", "Frozen Foods", "Grains", "Ice Cream", "Nuts"],
["Baby Products", "Baking Goods", "Yogurt", "Juice", "Milk", "Toiletries", "Lettuce", "Beef", "Cereal"],
["Fruits", "Baking Goods", "Butter", "Rice", "Yogurt", "Cheese", "Snacks", "Lettuce", "Beef", "Coffee"],
["Vegetables", "Chicken", "Ice Cream", "Tea", "Nuts"],
["Soda", "Eggs", "Fruits", "Frozen Foods", "Cheese", "Yogurt", "Sauces"],
["Baby Products", "Vegetables", "Eggs", "Spices", "Cheese", "Grains", "Ice Cream", "Bacon", "Chocolate Sauce"],
["Pasta", "Baking Goods", "Cheese", "Ice Cream", "Sauces", "Tea", "Snacks", "Toiletries", "Nuts", "Cereal"],
["Baking Goods", "Bread", "Butter", "Rice", "Yogurt", "Ice Cream", "Sauces", "Chocolate Sauce"],
["Vegetables", "Cereal", "Baking Goods", "Butter"],
["Nuts", "Rice", "Coffee", "Baking Goods"],
["Toiletries", "Yogurt", "Tea"],
["Milk", "Cookies", "Tea"],
["Vegetables", "Rice", "Sauces", "Milk", "Snacks", "Toiletries", "Cookies"],
["Bread", "Butter", "Cheese", "Jam", "Nuts"],
["Baby Products", "Baking Goods", "Ice Cream", "Sauces", "Chocolate Sauce"],
["Baby Products", "Pet Food", "Vegetables", "Chicken", "Toiletries"],
["Soda", "Eggs", "Chicken", "Rice", "Bun", "Sauces", "Lettuce", "Beef", "Bacon"],
["Vegetables", "Milk", "Cereal"],
["Fruits", "Baking Goods", "Yogurt", "Juice", "Toiletries"],
["Soda", "Condiments", "Bun", "Tea", "Milk", "Toiletries", "Beef", "Cereal"],
["Vegetables", "Condiments", "Frozen Foods", "Spices", "Rice", "Yogurt", "Ice Cream", "Cleaning Supplies", "Snacks", "Chocolate Sauce"],
["Soda", "Rice", "Grains", "Sauces", "Tea"],
["Pasta", "Condiments", "Rice", "Grains", "Cheese", "Yogurt", "Juice"],
["Baby Products", "Pasta", "Pet Food", "Baking Goods", "Bread", "Frozen Foods", "Butter", "Sauces", "Tea"],
["Pasta", "Frozen Foods", "Chicken", "Rice", "Cheese", "Ice Cream", "Chocolate Sauce"],
["Soda", "Rice", "Lettuce", "Beef", "Cereal"],
["Fruits", "Bun", "Granola", "Ice Cream", "Juice", "Beef", "Chocolate Sauce"],
["Vegetables", "Baking Goods", "Bread", "Frozen Foods", "Chicken", "Tea", "Cleaning Supplies", "Jam", "Nuts"],
["Vegetables", "Milk", "Cleaning Supplies", "Cereal"],
["Vegetables", "Pet Food", "Chicken", "Cheese", "Juice", "Sauces", "Ice Cream", "Cleaning Supplies", "Nuts"],
["Rice", "Toiletries", "Snacks", "Cleaning Supplies", "Cereal"],
["Condiments", "Butter", "Cheese", "Toiletries", "Snacks", "Nuts"],
["Pet Food", "Ice Cream", "Tea", "Lettuce", "Beef", "Chocolate Sauce"],
["Rice", "Cheese", "Juice", "Lettuce", "Beef"],
["Nuts", "Cheese", "Butter"],
["Soda", "Pet Food", "Eggs", "Butter", "Rice", "Cheese", "Grains", "Tea"],
["Soda", "Pasta", "Chicken", "Rice", "Cheese", "Yogurt", "Nuts"],
["Soda", "Vegetables", "Pasta", "Frozen Foods", "Chicken", "Rice", "Yogurt", "Sauces"],
["Bacon", "Eggs", "Cheese"],
["Baby Products", "Ice Cream", "Sauces", "Toiletries", "Nuts"],
["Pasta", "Baking Goods", "Condiments", "Rice", "Cheese", "Tea", "Toiletries", "Nuts", "Cereal"],
["Vegetables", "Lettuce", "Cereal", "Beef"],
["Vegetables", "Condiments", "Frozen Foods", "Chicken", "Rice", "Milk", "Snacks", "Cookies"],
["Soda", "Rice", "Chicken", "Baking Goods"],
["Pet Food", "Butter", "Grains", "Milk", "Cleaning Supplies", "Snacks", "Cookies"],
["Soda", "Eggs", "Vegetables", "Bread", "Chicken", "Rice", "Cheese", "Cleaning Supplies", "Jam", "Coffee"],
["Baby Products", "Baking Goods", "Condiments", "Spices", "Grains", "Milk", "Cleaning Supplies", "Toiletries", "Cookies"],
["Vegetables", "Pasta", "Bread", "Butter", "Sauces", "Tea"],
["Soda", "Sauces", "Milk", "Coffee", "Cookies"],
["Soda", "Baby Products", "Bread", "Butter", "Condiments", "Juice", "Tea", "Milk", "Cleaning Supplies", "Cereal"],
["Vegetables", "Soda", "Eggs", "Butter", "Cheese", "Tea", "Sauces", "Nuts"],
["Bacon", "Eggs", "Vegetables", "Rice"],
["Fruits", "Pasta", "Baking Goods", "Bun", "Granola", "Yogurt", "Sauces", "Cleaning Supplies", "Beef"],
["Soda", "Toiletries", "Grains"],
["Fruits", "Pasta", "Pet Food", "Vegetables", "Butter", "Cheese", "Yogurt", "Ice Cream", "Cleaning Supplies", "Nuts"],
["Nuts", "Cookies", "Ice Cream", "Milk"],
["Fruits", "Eggs", "Soda", "Bread", "Butter", "Granola", "Cheese", "Jam", "Bacon", "Cereal"],
["Vegetables", "Soda", "Frozen Foods", "Spices", "Rice", "Juice", "Cleaning Supplies", "Lettuce", "Snacks", "Beef"],
["Soda", "Butter", "Spices", "Rice", "Cheese", "Grains"],
["Baking Goods", "Rice", "Cereal", "Milk"],
["Soda", "Bread", "Butter", "Grains", "Sauces", "Snacks", "Jam", "Cereal"],
["Soda", "Baking Goods", "Cheese", "Grains", "Ice Cream", "Juice", "Lettuce", "Beef", "Nuts", "Coffee"],
["Eggs", "Butter", "Frozen Foods", "Spices", "Cheese", "Ice Cream", "Nuts"],
["Fruits", "Pet Food", "Butter", "Chicken", "Rice", "Yogurt", "Juice", "Snacks", "Toiletries", "Coffee"],
["Soda", "Bread", "Butter", "Rice", "Lettuce", "Beef"],
["Baby Products", "Frozen Foods", "Sauces"],
["Fruits", "Pet Food", "Frozen Foods", "Spices", "Granola", "Snacks"],
["Fruits", "Pet Food", "Condiments", "Frozen Foods", "Rice", "Yogurt", "Sauces", "Cereal"],
["Pasta", "Frozen Foods", "Cheese", "Ice Cream", "Sauces", "Snacks", "Nuts", "Chocolate Sauce", "Cereal"],
["Soda", "Bread", "Frozen Foods", "Yogurt", "Ice Cream", "Sauces", "Jam", "Chocolate Sauce"],
["Soda", "Bread", "Grains", "Yogurt", "Ice Cream", "Sauces", "Snacks", "Jam", "Chocolate Sauce", "Cereal"],
["Baby Products", "Vegetables", "Fruits", "Cheese", "Yogurt", "Ice Cream", "Toiletries", "Nuts"],
["Condiments", "Spices", "Cheese", "Yogurt", "Juice", "Nuts"],
["Pet Food", "Pasta", "Eggs", "Cheese", "Juice", "Ice Cream", "Bacon", "Chocolate Sauce"],
["Fruits", "Pet Food", "Frozen Foods", "Granola", "Toiletries"],
["Baby Products", "Baking Goods", "Frozen Foods", "Rice", "Sauces", "Snacks", "Lettuce", "Beef"],
["Fruits", "Pet Food", "Frozen Foods", "Butter", "Spices", "Yogurt"],
["Chicken", "Vegetables", "Nuts", "Ice Cream"],
["Baby Products", "Fruits", "Condiments", "Frozen Foods", "Bread", "Butter", "Yogurt", "Toiletries", "Cereal"],
["Baby Products", "Baking Goods", "Grains", "Ice Cream", "Chocolate Sauce"],
["Baby Products", "Soda", "Bread", "Condiments", "Butter", "Toiletries", "Cereal"],
["Soda", "Condiments", "Butter", "Bread", "Rice", "Cheese", "Cereal"],
["Soda", "Condiments", "Frozen Foods", "Spices", "Grains", "Milk", "Snacks", "Cereal"],
["Eggs", "Spices", "Bun", "Juice", "Beef", "Bacon"],
["Soda", "Cleaning Supplies", "Frozen Foods"],
["Fruits", "Condiments", "Frozen Foods", "Yogurt", "Grains", "Toiletries"],
["Soda", "Baking Goods", "Condiments", "Frozen Foods", "Snacks", "Nuts"],
["Toiletries", "Yogurt", "Sauces"],
["Baby Products", "Fruits", "Bread", "Butter", "Yogurt", "Cleaning Supplies"],
["Fruits", "Condiments", "Frozen Foods", "Chicken", "Rice", "Yogurt", "Tea", "Cleaning Supplies"],
["Baking Goods", "Condiments", "Grains", "Ice Cream", "Milk", "Snacks", "Nuts", "Cookies"],
["Soda", "Vegetables", "Baby Products", "Butter", "Ice Cream", "Tea", "Milk", "Nuts", "Cereal"],
["Soda", "Pasta", "Baby Products", "Vegetables", "Condiments", "Yogurt", "Sauces", "Milk", "Nuts", "Cereal"],
["Fruits", "Eggs", "Granola", "Juice", "Tea", "Milk", "Bacon", "Cereal"],
["Eggs", "Spices", "Rice", "Tea", "Milk", "Bacon", "Cereal", "Cookies"],
["Pet Food", "Baking Goods", "Bread", "Butter", "Grains", "Sauces", "Tea", "Milk", "Snacks", "Cookies"],
["Pasta", "Baking Goods", "Frozen Foods", "Cheese", "Juice", "Nuts"],
["Butter", "Bun", "Chicken", "Rice", "Cheese", "Beef", "Coffee"],
["Soda", "Fruits", "Condiments", "Frozen Foods", "Rice", "Granola", "Grains", "Yogurt", "Sauces", "Coffee"],
["Cleaning Supplies", "Butter", "Spices"],
["Rice", "Grains", "Ice Cream", "Juice", "Cleaning Supplies", "Nuts"],
["Frozen Foods", "Bread", "Butter"],
["Fruits", "Pet Food", "Baking Goods", "Rice", "Granola", "Grains"],
["Rice", "Nuts", "Cheese"],
["Baby Products", "Frozen Foods", "Ice Cream", "Tea", "Chocolate Sauce"],
["Vegetables", "Pet Food", "Bread", "Butter", "Spices", "Frozen Foods", "Chicken", "Rice", "Juice", "Cereal"],
["Pasta", "Frozen Foods", "Butter", "Cheese", "Sauces"],
["Grains", "Yogurt", "Juice", "Cheese", "Milk", "Cleaning Supplies", "Toiletries", "Cereal"],
["Coffee", "Bread", "Butter", "Cheese", "Cereal"],
["Eggs", "Frozen Foods", "Sauces", "Bacon", "Cereal"],
["Fruits", "Bread", "Frozen Foods", "Grains", "Yogurt", "Tea", "Jam"],
["Pet Food", "Eggs", "Chicken", "Rice", "Cheese", "Toiletries"],
["Fruits", "Baking Goods", "Butter", "Spices", "Rice", "Granola", "Grains", "Toiletries", "Cereal"],
["Fruits", "Vegetables", "Condiments", "Bread", "Butter", "Bun", "Yogurt", "Jam", "Beef"],
["Condiments", "Bread", "Cheese", "Juice", "Snacks", "Jam"],
["Soda", "Fruits", "Frozen Foods", "Chicken", "Rice", "Yogurt", "Grains", "Toiletries"],
["Fruits", "Granola", "Grains", "Tea", "Sauces", "Toiletries", "Nuts", "Coffee"],
["Vegetables", "Pet Food", "Bread", "Butter", "Grains", "Jam", "Cereal"],
["Spices", "Bun", "Sauces", "Beef", "Coffee"],
["Soda", "Baking Goods", "Butter", "Grains", "Cleaning Supplies", "Cereal"],
["Vegetables", "Eggs", "Pet Food", "Baking Goods", "Cheese", "Juice", "Tea"],
["Vegetables", "Bread", "Butter", "Grains", "Cheese", "Jam"],
["Rice", "Cleaning Supplies", "Cheese", "Frozen Foods"],
["Eggs", "Coffee", "Condiments", "Frozen Foods", "Grains", "Juice", "Milk", "Cleaning Supplies", "Bacon", "Cereal"],
["Pet Food", "Baking Goods", "Cheese", "Milk", "Toiletries", "Cookies"],
["Fruits", "Pasta", "Pet Food", "Condiments", "Granola", "Cheese", "Grains", "Sauces", "Nuts", "Coffee"],
["Fruits", "Spices", "Chicken", "Rice", "Granola", "Yogurt", "Juice", "Cleaning Supplies", "Coffee"],
["Fruits", "Baking Goods", "Granola", "Yogurt", "Ice Cream", "Snacks", "Chocolate Sauce", "Coffee"],
["Vegetables", "Pasta", "Juice", "Sauces", "Ice Cream", "Snacks", "Toiletries", "Nuts", "Coffee"],
["Fruits", "Pet Food", "Eggs", "Condiments", "Butter", "Bread", "Granola", "Cheese", "Sauces"],
["Pet Food", "Bread", "Frozen Foods", "Spices", "Butter", "Rice", "Tea", "Cleaning Supplies"],
["Bread", "Yogurt", "Cheese", "Jam", "Coffee"],
["Vegetables", "Pasta", "Baking Goods", "Bread", "Grains", "Cheese", "Sauces", "Milk", "Jam", "Cookies"],
["Pet Food", "Cheese", "Juice"],
["Frozen Foods", "Spices", "Rice", "Milk", "Cleaning Supplies", "Snacks", "Coffee", "Cookies"],
["Eggs", "Baking Goods", "Bread", "Rice", "Yogurt", "Cheese", "Tea", "Jam", "Bacon", "Cereal"],
["Baby Products", "Baking Goods", "Chicken", "Rice", "Grains", "Ice Cream", "Tea", "Chocolate Sauce"],
["Baby Products", "Pet Food", "Condiments", "Cheese", "Grains", "Ice Cream", "Snacks", "Lettuce", "Beef", "Nuts"],
["Vegetables", "Pasta", "Baking Goods", "Butter", "Chicken", "Rice", "Cheese", "Nuts", "Cereal"],
["Fruits", "Baking Goods", "Yogurt", "Snacks", "Toiletries"],
["Baby Products", "Pet Food", "Soda", "Baking Goods", "Condiments", "Rice", "Tea"],
["Chicken", "Vegetables", "Toiletries", "Cereal"],
["Fruits", "Pasta", "Bun", "Yogurt", "Juice", "Sauces", "Toiletries", "Beef", "Nuts"],
["Yogurt", "Bread", "Butter", "Baking Goods"],
["Rice", "Pet Food", "Toiletries"],
["Butter", "Chocolate Sauce", "Ice Cream"],
["Vegetables", "Milk", "Cookies", "Juice"],
["Vegetables", "Fruits", "Bread", "Butter", "Spices", "Condiments", "Rice", "Cheese", "Yogurt", "Tea"],
["Pet Food", "Baking Goods", "Cheese", "Yogurt", "Sauces", "Milk", "Nuts", "Cookies"],
["Fruits", "Bun", "Chicken", "Rice", "Granola", "Beef"],
["Baby Products", "Rice", "Jam", "Bread"],
["Butter", "Pet Food", "Grains", "Juice"],
["Vegetables", "Pet Food", "Bread", "Frozen Foods", "Chicken", "Grains", "Tea", "Jam", "Nuts", "Cereal"],
["Vegetables", "Pasta", "Frozen Foods", "Chicken", "Sauces", "Lettuce", "Beef", "Cereal"],
["Vegetables", "Butter", "Spices", "Juice", "Tea", "Toiletries", "Cleaning Supplies", "Nuts"],
["Baby Products", "Vegetables", "Pasta", "Condiments", "Spices", "Chicken", "Grains", "Cheese", "Juice"],
["Snacks", "Yogurt", "Spices"],
["Soda", "Eggs", "Pet Food", "Frozen Foods", "Spices", "Cheese", "Sauces", "Bacon"],
["Bread", "Butter", "Tea", "Milk", "Jam", "Cookies"],
["Fruits", "Bread", "Butter", "Frozen Foods", "Spices", "Yogurt", "Juice", "Sauces", "Cereal"],
["Lettuce", "Juice", "Beef"],
["Bread", "Spices", "Bun", "Cleaning Supplies", "Jam", "Beef", "Nuts"],
["Baby Products", "Pasta", "Bread", "Butter", "Rice", "Cheese", "Juice", "Nuts"],
["Cereal", "Yogurt", "Ice Cream", "Sauces", "Juice", "Nuts", "Coffee"],
["Baby Products", "Pet Food", "Frozen Foods", "Butter", "Cheese", "Sauces", "Milk", "Toiletries", "Cereal"],
["Vegetables", "Milk", "Cereal"],
["Vegetables", "Eggs", "Soda", "Baking Goods", "Chicken", "Cheese", "Sauces", "Toiletries", "Cleaning Supplies", "Bacon"],
["Soda", "Vegetables", "Frozen Foods", "Chicken", "Rice", "Cheese", "Tea", "Sauces", "Cereal"],
["Vegetables", "Baby Products", "Frozen Foods", "Spices", "Toiletries", "Cereal"],
["Baby Products", "Frozen Foods", "Chicken", "Rice", "Ice Cream", "Milk", "Toiletries", "Cleaning Supplies", "Nuts", "Cereal"],
["Baby Products", "Grains", "Lettuce", "Beef", "Nuts", "Coffee"],
["Eggs", "Pet Food", "Condiments", "Tea", "Sauces", "Bacon", "Cereal"],
["Bread", "Butter", "Grains", "Nuts", "Cereal"],
["Eggs", "Pet Food", "Spices", "Yogurt", "Bacon", "Cereal"],
["Pet Food", "Coffee", "Bread", "Butter", "Tea", "Milk", "Lettuce", "Beef", "Cereal"],
["Eggs", "Frozen Foods", "Ice Cream", "Tea", "Toiletries", "Bacon", "Chocolate Sauce"],
["Lettuce", "Cereal", "Beef"],
["Soda", "Vegetables", "Spices", "Grains", "Snacks", "Coffee"],
["Baby Products", "Nuts", "Coffee", "Rice"],
["Fruits", "Spices", "Bun", "Rice", "Yogurt", "Lettuce", "Beef"],
["Fruits", "Granola", "Grains", "Yogurt", "Cheese", "Snacks", "Coffee"],
["Sauces", "Condiments", "Juice", "Spices"],
["Baking Goods", "Condiments", "Chicken", "Rice", "Sauces", "Milk", "Cleaning Supplies", "Coffee", "Cookies"],
["Fruits", "Vegetables", "Baking Goods", "Frozen Foods", "Rice", "Granola", "Yogurt", "Toiletries"],
["Baby Products", "Fruits", "Soda", "Bread", "Condiments", "Spices", "Chicken", "Rice", "Yogurt", "Jam"],
["Baby Products", "Eggs", "Butter", "Frozen Foods", "Cheese", "Juice"],
["Vegetables", "Toiletries", "Cheese"],
["Vegetables", "Eggs", "Pasta", "Baking Goods", "Butter", "Chicken", "Rice", "Ice Cream", "Sauces", "Bacon", "Nuts"],
["Butter", "Spices", "Toiletries", "Snacks", "Nuts"],
["Nuts", "Yogurt", "Ice Cream"],
["Bread", "Frozen Foods", "Butter", "Grains", "Snacks", "Cereal"],
["Vegetables", "Fruits", "Baking Goods", "Frozen Foods", "Spices", "Butter", "Granola", "Grains", "Cheese"],
["Milk", "Cereal", "Frozen Foods", "Sauces"],
["Vegetables", "Chicken", "Cheese", "Juice", "Sauces", "Nuts"],
["Baby Products", "Pet Food", "Soda", "Yogurt", "Ice Cream", "Chocolate Sauce"],
["Coffee", "Baking Goods", "Butter", "Frozen Foods", "Spices", "Yogurt", "Grains", "Cheese", "Toiletries", "Cereal"],
["Vegetables", "Baby Products", "Fruits", "Spices", "Chicken", "Granola", "Grains", "Yogurt", "Juice", "Nuts"],
["Vegetables", "Eggs", "Frozen Foods", "Cheese", "Toiletries"],
["Vegetables", "Eggs", "Spices", "Chicken", "Yogurt", "Toiletries", "Bacon"],
["Soda", "Fruits", "Yogurt", "Frozen Foods"],
["Soda", "Coffee", "Baking Goods", "Frozen Foods", "Rice", "Cheese", "Grains", "Nuts", "Cereal"],
["Bread", "Butter", "Cheese", "Grains", "Cleaning Supplies"],
["Condiments", "Butter", "Spices", "Frozen Foods", "Cereal", "Milk", "Cleaning Supplies", "Lettuce", "Beef", "Coffee"],
["Soda", "Pasta", "Rice", "Grains", "Yogurt", "Sauces", "Toiletries"],
["Baby Products", "Pasta", "Bread", "Butter", "Cheese", "Sauces"],
["Baby Products", "Soda", "Rice", "Yogurt", "Cleaning Supplies", "Snacks", "Cereal"],
["Spices", "Juice", "Sauces"],
["Soda", "Cleaning Supplies", "Bread", "Butter"],
["Vegetables", "Eggs", "Spices", "Rice", "Bacon"],
["Baby Products", "Eggs", "Baking Goods", "Frozen Foods", "Bun", "Cheese", "Yogurt", "Milk", "Beef", "Bacon", "Cereal"],
["Fruits", "Baking Goods", "Spices", "Yogurt", "Cereal"],
["Vegetables", "Pet Food", "Frozen Foods", "Yogurt", "Milk", "Cleaning Supplies", "Cookies"],
["Pet Food", "Coffee", "Eggs", "Baking Goods", "Cheese", "Milk", "Cleaning Supplies", "Bacon", "Cereal", "Cookies"],
["Fruits", "Spices", "Bun", "Granola", "Yogurt", "Tea", "Cleaning Supplies", "Toiletries", "Beef"],
["Baby Products", "Pasta", "Bread", "Butter", "Sauces", "Cereal"],
["Eggs", "Bread", "Spices", "Yogurt", "Juice", "Ice Cream", "Jam", "Bacon", "Chocolate Sauce"],
["Vegetables", "Frozen Foods", "Cheese", "Tea", "Snacks", "Cleaning Supplies", "Coffee"],
["Soda", "Chicken", "Rice", "Yogurt", "Ice Cream", "Sauces", "Lettuce", "Beef", "Chocolate Sauce"],
["Bacon", "Eggs", "Lettuce", "Beef"],
["Pet Food", "Cheese", "Tea"],
["Baby Products", "Eggs", "Fruits", "Condiments", "Cheese", "Yogurt", "Tea", "Milk", "Coffee", "Cookies"],
["Pet Food", "Condiments", "Rice", "Cereal", "Cheese", "Sauces", "Tea", "Milk", "Nuts", "Coffee"],
["Baby Products", "Fruits", "Frozen Foods", "Granola", "Milk", "Cereal", "Cookies"],
["Fruits", "Soda", "Bread", "Butter", "Spices", "Yogurt", "Cleaning Supplies"],
["Vegetables", "Pasta", "Chicken", "Rice", "Juice", "Sauces", "Cleaning Supplies", "Cereal"],
["Pasta", "Cheese", "Sauces"],
["Fruits", "Baking Goods", "Butter", "Rice", "Yogurt", "Milk", "Toiletries", "Cookies"],
["Milk", "Cereal", "Bread", "Butter"],
["Vegetables", "Grains", "Juice", "Cleaning Supplies", "Coffee"],
["Nuts", "Snacks", "Juice", "Sauces"],
["Baby Products", "Pet Food", "Bun", "Yogurt", "Snacks", "Beef"],
["Vegetables", "Soda", "Butter", "Chicken", "Toiletries"],
["Baby Products", "Vegetables", "Soda", "Eggs", "Yogurt", "Bacon"],
["Pasta", "Baking Goods", "Chicken", "Rice", "Cheese", "Ice Cream", "Cleaning Supplies", "Lettuce", "Beef", "Chocolate Sauce"],
["Baby Products", "Pet Food", "Pasta", "Bread", "Butter", "Yogurt", "Sauces", "Cereal"],
["Pasta", "Bread", "Frozen Foods", "Ice Cream", "Sauces", "Toiletries", "Jam", "Nuts"],
["Soda", "Bread", "Butter", "Spices", "Rice", "Yogurt", "Juice", "Tea"],
["Butter", "Snacks", "Cereal", "Frozen Foods"],
["Pet Food", "Eggs", "Bread", "Butter", "Rice", "Grains", "Sauces", "Milk", "Snacks", "Bacon", "Cereal"],
["Baby Products", "Condiments", "Frozen Foods", "Tea", "Milk", "Cleaning Supplies", "Nuts", "Cookies"],
["Fruits", "Pasta", "Granola", "Cheese"],
["Vegetables", "Coffee", "Baking Goods", "Butter", "Chicken", "Rice", "Tea", "Toiletries", "Cereal"],
["Lettuce", "Beef", "Spices"],
["Fruits", "Eggs", "Bread", "Rice", "Granola", "Cheese", "Yogurt", "Jam", "Cereal"],
["Yogurt", "Chocolate Sauce", "Grains", "Ice Cream"],
["Baby Products", "Grains", "Cheese", "Milk", "Cookies"],
["Vegetables", "Condiments", "Butter", "Grains", "Yogurt", "Tea", "Sauces", "Lettuce", "Beef", "Nuts"],
["Soda", "Vegetables", "Frozen Foods", "Bun", "Rice", "Chicken", "Beef"],
["Milk", "Coffee", "Cookies", "Butter"],
["Pasta", "Cheese", "Bread", "Butter"],
["Soda", "Baking Goods", "Baby Products", "Tea"],
["Fruits", "Pasta", "Baking Goods", "Bun", "Granola", "Cheese", "Yogurt", "Tea", "Sauces", "Beef"],
["Pasta", "Spices", "Yogurt", "Sauces"],
["Baby Products", "Pet Food", "Eggs", "Grains", "Cleaning Supplies", "Toiletries", "Bacon"],
["Eggs", "Pasta", "Baking Goods", "Butter", "Cheese", "Juice", "Milk", "Cleaning Supplies", "Snacks", "Bacon", "Cereal"],
["Bread", "Butter", "Spices", "Rice", "Tea", "Cleaning Supplies"],
["Pasta", "Spices", "Cheese", "Tea"],
["Fruits", "Eggs", "Chicken", "Rice", "Yogurt", "Milk", "Bacon", "Cereal"],
["Pet Food", "Pasta", "Cheese", "Milk", "Cereal"],
["Bun", "Rice", "Milk", "Snacks", "Toiletries", "Beef", "Cereal", "Cookies"],
["Pasta", "Baking Goods", "Butter", "Cereal", "Cheese", "Tea", "Sauces", "Milk", "Coffee"],
["Vegetables", "Eggs", "Fruits", "Rice", "Yogurt", "Lettuce", "Beef", "Bacon", "Cereal"],
["Rice", "Cleaning Supplies", "Bread", "Butter"],
["Soda", "Baby Products", "Vegetables", "Frozen Foods", "Chicken", "Sauces", "Snacks", "Coffee"],
["Fruits", "Pasta", "Pet Food", "Condiments", "Granola", "Cheese", "Yogurt", "Juice", "Tea", "Toiletries"],
["Eggs", "Baking Goods", "Condiments", "Rice", "Sauces", "Milk", "Bacon", "Cereal"],
["Pasta", "Spices", "Chicken", "Rice", "Bun", "Cheese", "Tea", "Milk", "Lettuce", "Beef", "Cookies"],
["Vegetables", "Pet Food", "Yogurt"],
["Eggs", "Frozen Foods", "Chicken", "Rice", "Grains", "Cheese", "Cleaning Supplies", "Bacon", "Coffee"],
["Pasta", "Frozen Foods", "Chicken", "Rice", "Sauces", "Coffee"],
["Fruits", "Milk", "Yogurt", "Cookies"],
["Vegetables", "Pasta", "Bun", "Chicken", "Ice Cream", "Sauces", "Toiletries", "Beef", "Nuts", "Coffee"],
["Fruits", "Frozen Foods", "Spices", "Bun", "Rice", "Granola", "Cleaning Supplies", "Toiletries", "Beef"],
["Eggs", "Frozen Foods", "Spices", "Tea", "Cleaning Supplies", "Bacon"],
["Vegetables", "Soda", "Baking Goods", "Butter", "Grains", "Ice Cream", "Sauces", "Milk", "Nuts", "Cookies"],
["Condiments", "Yogurt", "Cheese", "Juice", "Tea", "Nuts"],
["Vegetables", "Baking Goods", "Bread", "Butter", "Spices", "Juice", "Coffee"],
["Vegetables", "Lettuce", "Beef"],
["Baby Products", "Condiments", "Yogurt", "Juice", "Milk", "Lettuce", "Beef", "Cereal"],
["Baby Products", "Pet Food", "Ice Cream", "Toiletries", "Lettuce", "Beef", "Nuts"],
["Vegetables", "Nuts", "Ice Cream", "Spices"],
["Bread", "Spices", "Milk", "Jam", "Nuts", "Cereal"],
["Vegetables", "Fruits", "Butter", "Chicken", "Grains", "Yogurt", "Cleaning Supplies"],
["Nuts", "Coffee", "Ice Cream"],
["Fruits", "Baking Goods", "Bun", "Granola", "Yogurt", "Tea", "Beef"],
["Cheese", "Ice Cream", "Toiletries", "Nuts", "Chocolate Sauce", "Cereal"],
["Pasta", "Coffee", "Butter", "Sauces"],
["Fruits", "Coffee", "Baking Goods", "Granola", "Cheese", "Ice Cream", "Nuts", "Cereal"],
["Eggs", "Spices", "Chicken", "Rice", "Bacon"],
["Baking Goods", "Bun", "Cheese", "Juice", "Tea", "Cleaning Supplies", "Toiletries", "Beef"],
["Bread", "Butter", "Frozen Foods", "Spices", "Yogurt", "Juice", "Tea", "Ice Cream", "Jam", "Nuts", "Cereal"],
["Pasta", "Toiletries", "Cheese", "Cereal"],
["Vegetables", "Baby Products", "Chicken", "Rice", "Sauces", "Milk", "Toiletries", "Nuts", "Cereal"],
["Bacon", "Eggs", "Cleaning Supplies", "Tea"],
["Eggs", "Bread", "Butter", "Chicken", "Rice", "Cheese"],
["Bread", "Chicken", "Rice", "Snacks", "Jam"],
["Pet Food", "Cleaning Supplies", "Tea"],
["Baby Products", "Coffee", "Tea"],
["Nuts", "Cereal", "Spices"],
["Vegetables", "Coffee", "Baking Goods", "Condiments", "Chicken", "Bun", "Milk", "Beef", "Cereal"],
["Eggs", "Condiments", "Cheese", "Tea", "Milk", "Bacon", "Cookies"],
["Vegetables", "Baby Products", "Condiments", "Chicken", "Yogurt", "Juice"],
["Nuts", "Toiletries", "Yogurt"],
["Vegetables", "Soda", "Spices", "Rice", "Yogurt", "Ice Cream", "Sauces", "Nuts", "Chocolate Sauce"],
["Soda", "Frozen Foods", "Spices", "Yogurt", "Cereal"],
["Snacks", "Cereal", "Juice"],
["Spices", "Bun", "Ice Cream", "Beef", "Nuts"],
["Fruits", "Baby Products", "Pet Food", "Yogurt", "Ice Cream", "Cleaning Supplies", "Nuts", "Chocolate Sauce"],
["Vegetables", "Pet Food", "Eggs", "Baking Goods", "Spices", "Chicken", "Cheese", "Milk", "Cereal"],
["Baking Goods", "Condiments", "Chicken", "Rice", "Grains", "Juice", "Lettuce", "Beef", "Cereal"],
["Soda", "Butter", "Cheese", "Sauces", "Snacks"],
["Spices", "Grains", "Sauces", "Milk", "Cleaning Supplies", "Lettuce", "Beef", "Nuts", "Cookies"],
["Baby Products", "Baking Goods", "Butter", "Chicken", "Rice", "Yogurt", "Cleaning Supplies", "Cereal"],
["Baking Goods", "Condiments", "Bread", "Chicken", "Rice", "Grains", "Yogurt", "Jam", "Nuts"],
["Vegetables", "Butter", "Grains", "Cheese", "Ice Cream", "Milk", "Nuts", "Chocolate Sauce", "Cookies"],
["Fruits", "Eggs", "Soda", "Granola", "Cheese", "Yogurt", "Juice", "Bacon", "Coffee"],
["Condiments", "Butter", "Cheese", "Lettuce", "Beef"],
["Vegetables", "Fruits", "Baby Products", "Condiments", "Cereal", "Granola", "Ice Cream", "Nuts", "Coffee"],
["Bread", "Frozen Foods", "Butter", "Grains", "Yogurt", "Sauces", "Toiletries", "Snacks", "Nuts", "Coffee"],
["Fruits", "Pasta", "Baking Goods", "Butter", "Spices", "Yogurt", "Cheese", "Snacks"],
["Pet Food", "Rice", "Yogurt", "Ice Cream", "Sauces", "Milk", "Chocolate Sauce", "Cookies"],
["Vegetables", "Baby Products", "Condiments", "Frozen Foods", "Rice", "Snacks", "Cleaning Supplies"],
["Vegetables", "Butter", "Rice", "Ice Cream", "Toiletries", "Nuts", "Chocolate Sauce", "Coffee"],
["Pet Food", "Baking Goods", "Condiments", "Grains", "Tea"],
["Soda", "Baby Products", "Baking Goods", "Tea", "Snacks"],
["Vegetables", "Coffee", "Chicken", "Bun", "Ice Cream", "Sauces", "Toiletries", "Beef", "Chocolate Sauce", "Cereal"],
["Fruits", "Pet Food", "Vegetables", "Baking Goods", "Frozen Foods", "Granola", "Grains", "Snacks", "Toiletries"],
["Baking Goods", "Condiments", "Grains", "Ice Cream", "Toiletries", "Nuts"],
["Baby Products", "Eggs", "Cheese"],
["Butter", "Spices", "Cheese", "Yogurt", "Tea", "Sauces", "Cleaning Supplies", "Snacks"],
["Baking Goods", "Rice", "Milk", "Nuts", "Cookies"],
["Baking Goods", "Condiments", "Butter", "Cheese", "Juice", "Tea", "Milk", "Cookies"],
["Vegetables", "Baking Goods", "Butter", "Spices", "Grains", "Cheese", "Ice Cream", "Snacks", "Nuts", "Coffee"],
["Baby Products", "Pet Food", "Coffee", "Butter", "Frozen Foods", "Rice", "Milk", "Nuts", "Cereal"],
["Baby Products", "Fruits", "Cereal", "Granola", "Sauces", "Nuts", "Coffee"],
["Pet Food", "Baking Goods", "Frozen Foods", "Spices", "Yogurt", "Cheese", "Juice", "Ice Cream", "Nuts"],
["Cereal", "Grains", "Baking Goods"],
["Fruits", "Toiletries", "Yogurt", "Grains"],
["Fruits", "Vegetables", "Spices", "Granola", "Juice", "Tea", "Cleaning Supplies", "Nuts"],
["Vegetables", "Eggs", "Baking Goods", "Bread", "Cheese", "Grains", "Lettuce", "Jam", "Beef"],
["Soda", "Pet Food", "Baby Products", "Vegetables", "Spices", "Chicken", "Rice", "Snacks", "Nuts"],
["Fruits", "Frozen Foods", "Rice", "Granola", "Yogurt", "Grains", "Ice Cream", "Tea", "Nuts"],
["Eggs", "Frozen Foods", "Ice Cream", "Bacon", "Nuts"],
["Fruits", "Bread", "Butter", "Rice", "Yogurt", "Ice Cream", "Tea", "Milk", "Cleaning Supplies", "Nuts", "Cookies"],
["Soda", "Bread", "Butter", "Spices", "Toiletries", "Cleaning Supplies"],
["Pasta", "Baking Goods", "Yogurt", "Juice", "Sauces", "Milk", "Lettuce", "Beef", "Coffee", "Cookies"],
["Baking Goods", "Bread", "Frozen Foods", "Butter", "Bun", "Cleaning Supplies", "Beef"],
["Eggs", "Condiments", "Rice", "Ice Cream", "Sauces", "Tea", "Bacon", "Chocolate Sauce"],
["Eggs", "Pasta", "Bun", "Cheese", "Grains", "Ice Cream", "Juice", "Sauces", "Beef", "Chocolate Sauce"],
["Soda", "Pasta", "Chicken", "Rice", "Grains", "Cheese", "Sauces", "Nuts"],
["Vegetables", "Fruits", "Condiments", "Frozen Foods", "Spices", "Chicken", "Rice", "Yogurt", "Cleaning Supplies", "Nuts"],
["Fruits", "Pet Food", "Butter", "Cereal", "Grains", "Yogurt", "Cheese", "Milk", "Coffee", "Cookies"],
["Vegetables", "Baby Products", "Fruits", "Yogurt", "Ice Cream", "Tea", "Nuts", "Chocolate Sauce"],
["Baby Products", "Pet Food", "Vegetables", "Pasta", "Ice Cream", "Sauces", "Snacks", "Cleaning Supplies", "Chocolate Sauce", "Cereal"],
["Vegetables", "Pasta", "Soda", "Chicken", "Cheese", "Yogurt", "Cleaning Supplies"],
["Eggs", "Baking Goods", "Condiments", "Rice", "Cheese", "Sauces"],
["Rice", "Cereal", "Cheese", "Grains", "Milk", "Coffee"],
["Vegetables", "Soda", "Fruits", "Baking Goods", "Chicken", "Grains", "Yogurt", "Cheese", "Sauces", "Tea"],
["Nuts", "Juice", "Ice Cream"],
["Vegetables", "Condiments", "Juice", "Milk", "Cereal"],
["Soda", "Vegetables", "Condiments", "Butter", "Rice", "Tea", "Snacks", "Cleaning Supplies"],
["Soda", "Pasta", "Pet Food", "Cheese", "Ice Cream", "Nuts"],
["Vegetables", "Soda", "Baby Products", "Pet Food", "Spices", "Cereal", "Toiletries", "Nuts", "Coffee"],
["Vegetables", "Yogurt", "Ice Cream", "Tea", "Nuts"],
["Fruits", "Granola", "Cleaning Supplies", "Lettuce", "Beef"],
["Baby Products", "Eggs", "Ice Cream", "Bacon", "Nuts"],
["Baby Products", "Vegetables", "Condiments", "Butter", "Frozen Foods", "Cheese", "Juice", "Cereal"],
["Vegetables", "Frozen Foods", "Cleaning Supplies", "Butter"],
["Vegetables", "Coffee", "Bread", "Chicken", "Rice", "Grains", "Juice", "Milk", "Jam", "Cereal"],
["Pasta", "Butter", "Frozen Foods", "Ice Cream", "Sauces", "Juice", "Chocolate Sauce"],
["Butter", "Frozen Foods", "Rice", "Grains", "Sauces", "Tea", "Cleaning Supplies", "Lettuce", "Beef"],
["Eggs", "Cheese", "Yogurt"],
["Lettuce", "Baking Goods", "Beef"],
["Vegetables", "Bread", "Butter", "Condiments", "Frozen Foods", "Juice", "Snacks", "Jam", "Nuts", "Coffee"],
["Bread", "Spices", "Chicken", "Rice", "Bun", "Tea", "Milk", "Jam", "Beef", "Cereal"],
["Baby Products", "Pasta", "Fruits", "Yogurt", "Sauces", "Milk", "Toiletries", "Coffee", "Cookies"],
["Butter", "Cheese", "Ice Cream", "Cleaning Supplies", "Nuts", "Chocolate Sauce"],
["Condiments", "Bun", "Grains", "Snacks", "Beef"],
["Baby Products", "Pasta", "Grains", "Tea", "Sauces", "Cleaning Supplies", "Toiletries", "Coffee"],
["Bread", "Butter", "Ice Cream", "Sauces", "Tea", "Toiletries", "Nuts", "Chocolate Sauce", "Cereal"],
["Pasta", "Pet Food", "Cheese", "Ice Cream", "Sauces", "Snacks", "Nuts"],
["Eggs", "Condiments", "Spices", "Cheese", "Grains", "Nuts"],
["Eggs", "Rice", "Yogurt", "Ice Cream", "Tea", "Bacon", "Chocolate Sauce"],
["Nuts", "Toiletries", "Ice Cream", "Spices"],
["Vegetables", "Eggs", "Baking Goods", "Condiments", "Cheese", "Sauces"],
["Pet Food", "Pasta", "Baking Goods", "Bread", "Butter", "Sauces"],
["Pasta", "Butter", "Sauces"],
["Baby Products", "Ice Cream", "Sauces", "Toiletries", "Nuts"],
["Pasta", "Pet Food", "Ice Cream", "Sauces", "Chocolate Sauce", "Coffee"],
["Toiletries", "Jam", "Bread", "Butter"],
["Soda", "Milk", "Cookies", "Butter"],
["Vegetables", "Eggs", "Cheese", "Milk", "Coffee", "Cookies"],
["Pasta", "Butter", "Spices", "Bun", "Grains", "Sauces", "Beef"],
["Vegetables", "Eggs", "Baking Goods", "Frozen Foods", "Chicken", "Bun", "Tea", "Cleaning Supplies", "Beef", "Bacon"],
["Milk", "Grains", "Cookies"],
["Fruits", "Vegetables", "Bread", "Spices", "Rice", "Yogurt", "Toiletries", "Jam", "Cereal"],
["Soda", "Baby Products", "Eggs", "Spices", "Yogurt", "Cheese", "Milk", "Cookies"],
["Baby Products", "Spices", "Juice", "Sauces", "Snacks"],
["Frozen Foods", "Spices", "Yogurt", "Sauces", "Cleaning Supplies"],
["Soda", "Eggs", "Bread", "Butter", "Frozen Foods", "Cheese", "Juice", "Cleaning Supplies", "Bacon", "Coffee"],
["Vegetables", "Cheese", "Juice", "Sauces", "Snacks", "Cereal"],
["Pet Food", "Snacks", "Toiletries"],
["Baby Products", "Condiments", "Ice Cream", "Snacks", "Chocolate Sauce"],
["Fruits", "Eggs", "Condiments", "Butter", "Bun", "Rice", "Yogurt", "Cheese", "Toiletries", "Beef"],
["Pasta", "Bread", "Butter", "Sauces", "Nuts"],
["Vegetables", "Fruits", "Eggs", "Chicken", "Yogurt", "Bacon"],
["Soda", "Pasta", "Chicken", "Rice", "Cheese", "Cleaning Supplies"],
["Condiments", "Bun", "Cheese", "Snacks", "Beef"],
["Pet Food", "Condiments", "Butter", "Cheese", "Juice", "Ice Cream", "Nuts"],
["Condiments", "Frozen Foods", "Butter", "Spices", "Grains", "Snacks"],
["Rice", "Condiments", "Tea"],
["Fruits", "Vegetables", "Granola", "Juice", "Toiletries", "Snacks", "Cereal"],
["Soda", "Vegetables", "Bread", "Butter", "Chicken"],
["Vegetables", "Pet Food", "Soda", "Eggs", "Butter", "Tea", "Snacks", "Bacon", "Nuts", "Cereal"],
["Fruits", "Eggs", "Baby Products", "Granola", "Cheese", "Yogurt", "Milk", "Toiletries", "Nuts", "Cereal"],
["Toiletries", "Cereal", "Frozen Foods"],
["Baby Products", "Eggs", "Baking Goods", "Bun", "Chicken", "Rice", "Beef", "Bacon"],
["Butter", "Sauces", "Milk", "Nuts", "Cookies"],
["Fruits", "Pet Food", "Baking Goods", "Yogurt", "Toiletries", "Lettuce", "Beef"],
["Rice", "Pet Food", "Coffee", "Baking Goods"],
["Fruits", "Eggs", "Pet Food", "Frozen Foods", "Granola", "Cheese", "Yogurt", "Cleaning Supplies", "Coffee"],
["Soda", "Eggs", "Butter", "Juice", "Sauces", "Lettuce", "Beef", "Bacon"],
["Vegetables", "Bread", "Butter", "Spices", "Chicken", "Juice", "Snacks"],
["Eggs", "Snacks", "Cheese", "Yogurt"],
["Soda", "Vegetables", "Pasta", "Frozen Foods", "Spices", "Chicken", "Yogurt", "Sauces", "Coffee"],
["Chicken", "Vegetables", "Toiletries"],
["Baby Products", "Frozen Foods", "Rice", "Juice", "Sauces", "Tea", "Coffee"],
["Vegetables", "Baking Goods", "Juice", "Tea", "Sauces", "Ice Cream", "Cleaning Supplies", "Toiletries", "Snacks", "Nuts"],
["Chicken", "Vegetables", "Rice"],
["Fruits", "Condiments", "Granola", "Grains", "Milk", "Snacks", "Lettuce", "Beef", "Cereal", "Cookies"],
["Eggs", "Spices", "Bun", "Cheese", "Sauces", "Snacks", "Beef"],
["Eggs", "Chicken", "Rice", "Juice", "Bacon"],
["Baby Products", "Eggs", "Soda", "Baking Goods", "Condiments", "Cheese", "Ice Cream", "Cleaning Supplies", "Nuts", "Coffee"],
["Bread", "Butter", "Ice Cream", "Jam", "Nuts", "Coffee"],
["Baby Products", "Pasta", "Condiments", "Cheese", "Milk", "Toiletries", "Snacks", "Nuts", "Cereal"],
["Fruits", "Pasta", "Condiments", "Butter", "Chicken", "Rice", "Granola", "Grains", "Cheese", "Nuts"],
["Pasta", "Spices", "Yogurt", "Sauces", "Tea"],
["Vegetables", "Chicken", "Rice", "Ice Cream", "Chocolate Sauce"],
["Vegetables", "Baby Products", "Frozen Foods", "Yogurt", "Juice", "Cleaning Supplies", "Nuts"],
["Eggs", "Pet Food", "Yogurt", "Juice", "Ice Cream", "Toiletries", "Snacks", "Bacon", "Nuts", "Cereal"],
["Fruits", "Baking Goods", "Butter", "Granola", "Milk", "Cookies"],
["Fruits", "Granola", "Grains", "Toiletries", "Cleaning Supplies"],
["Baby Products", "Pasta", "Chicken", "Rice", "Cheese", "Grains", "Milk", "Snacks", "Coffee", "Cookies"],
["Soda", "Fruits", "Yogurt"],
["Soda", "Eggs", "Butter", "Cheese", "Ice Cream", "Lettuce", "Beef", "Bacon", "Nuts", "Chocolate Sauce"],
["Fruits", "Yogurt", "Granola", "Baking Goods"],
["Soda", "Pet Food", "Condiments", "Grains", "Sauces", "Nuts"],
["Vegetables", "Eggs", "Spices", "Milk", "Bacon", "Cereal"],
["Baby Products", "Bun", "Beef"],
["Pasta", "Baking Goods", "Frozen Foods", "Yogurt", "Ice Cream", "Sauces", "Cleaning Supplies", "Nuts", "Chocolate Sauce", "Cereal"],
["Butter", "Frozen Foods", "Rice", "Grains", "Yogurt", "Ice Cream", "Juice", "Cleaning Supplies", "Nuts", "Coffee"],
["Baby Products", "Fruits", "Bread", "Cheese", "Yogurt", "Tea", "Milk", "Snacks", "Jam", "Cereal"],
["Bacon", "Eggs", "Toiletries", "Cheese"],
["Eggs", "Condiments", "Butter", "Cereal", "Cheese", "Tea", "Milk", "Coffee"],
["Baby Products", "Soda", "Bread", "Yogurt", "Grains", "Ice Cream", "Toiletries", "Jam", "Nuts"],
["Pet Food", "Bread", "Butter", "Sauces", "Toiletries", "Snacks"],
["Pet Food", "Pasta", "Baking Goods", "Bread", "Rice", "Sauces", "Tea", "Jam"],
["Fruits", "Eggs", "Spices", "Chicken", "Rice", "Cheese", "Yogurt", "Juice", "Sauces", "Toiletries"],
["Fruits", "Eggs", "Baby Products", "Frozen Foods", "Bun", "Granola", "Cheese", "Toiletries", "Beef", "Bacon"],
["Pet Food", "Pasta", "Frozen Foods", "Butter", "Ice Cream", "Sauces", "Nuts", "Chocolate Sauce", "Coffee"],
["Baby Products", "Pasta", "Baking Goods", "Butter", "Cheese", "Yogurt", "Juice", "Sauces", "Cereal"],
["Vegetables", "Eggs", "Baking Goods", "Spices", "Chicken", "Rice", "Cheese", "Cleaning Supplies"],
["Soda", "Vegetables", "Pasta", "Bread", "Cheese", "Milk", "Toiletries", "Jam", "Nuts", "Cereal"],
["Baby Products", "Fruits", "Condiments", "Chicken", "Rice", "Yogurt", "Juice", "Milk", "Nuts", "Cereal"],
["Pasta", "Eggs", "Bread", "Butter", "Rice", "Cheese", "Juice", "Sauces"],
["Baby Products", "Butter", "Yogurt", "Grains", "Ice Cream", "Cleaning Supplies", "Chocolate Sauce"],
["Soda", "Eggs", "Baking Goods", "Milk", "Bacon", "Cookies"],
["Vegetables", "Soda", "Eggs", "Chicken", "Bun", "Cheese", "Cleaning Supplies", "Lettuce", "Beef", "Bacon"],
["Chicken", "Rice", "Cheese", "Vegetables"],
["Fruits", "Pasta", "Vegetables", "Baby Products", "Condiments", "Spices", "Yogurt", "Sauces", "Nuts"],
["Fruits", "Spices", "Grains", "Yogurt", "Ice Cream", "Nuts"]
]

with open("walmartTransactions.csv", "w") as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(walmartData)


# %% [markdown]
# ## Part 2 Details
# * Implement the brute force method to generate frequent items and generate
# association rules.
# * The brute force method for finding frequent itemsets works as follows.
# Enumerate and generate all possible 1-itemsets and 2-itemsets. There are
# 30 items, so there are 435 possible 2-itemsets totally. Check to see whether
# each possible 1-itemset/2-itemset is frequent. Then enumerate and generate
# all possible 3-itemsets. There are 4060 possible 3-itemsets totally. Check to
# see whether each possible 3-itemset is :frequent. Keep on doing so until
# you see none of the possible k-itemsets is :frequent for some k, at which
# point the brute force method terminates without generating (k+1)-itemsets.

# %% [markdown]
# ### Input Selection and Validation: ###
# After successfully initializing the datasets, the user is welcomed to the Apriori Algorithm on the command line and prompted to enter the following user specified variables.

# %% [markdown]
# ### Determination of Dataset: ###
# The user is provided with a list of datasets and is prompted to enter an integer value between 1 and 7 on the command line to select the corresponding dataset. If a value outside of this range or a non-integer value is entered, an error is created and the program terminates.

# %%
# The data set selection, support, and confidence must be user-specified parameters

# Start and take in user input

print("CS634-101 Apriori Midterm Project - Joshua Kobuskie")

dataSelect = input("Please select a dataset by number: \n1. Amazon \n2. Best Buy \n3. K-Mart \n4. Nike \n5. Generic \n6. Custom\n7. Walmart\n")

# Confirm selection is valid
try:
    dataSelect = int(dataSelect)
    if dataSelect not in range(1,8):
        print("Invalid input. Please restart and enter a valid dataset number.")
        raise SystemExit
except ValueError:
    print("Invalid input. Please restart and enter a valid dataset number.")
    raise SystemExit

datasets = ["Amazon", "Best Buy", "K-Mart", "Nike", "Generic", "Custom", "Walmart"]

print("You have selected dataset {}: {}".format(dataSelect, datasets[dataSelect-1]))

# %% [markdown]
# ### Determination of Support: ###
# The user is prompted to enter an integer value between 1 and 100 on the command line to select the minimum support. If a value outside of this range or a non-integer value is entered, an error is created and the program terminates.

# %%
support = input("Please select the minimum support level in % (value 1 to 100):\n")

# Confirm selection is valid
try:
    support = int(support)
    if support not in range(1,101):
        print("Invalid input. Please restart and enter a valid support level.")
        raise SystemExit
except ValueError:
    print("Invalid input. Please restart and enter a valid support level.")
    raise SystemExit

print("You have selected a minimum support level of {}%".format(support))

# %% [markdown]
# ### Determination of Confidence: ###
# The user is prompted to enter an integer value between 1 and 100 on the command line to select the minimum confidence. If a value outside of this range or a non-integer value is entered, an error is created and the program terminates.

# %%
confidence = input("Please select the minimum confidence level in % (value 1 to 100):\n")

# Confirm selection is valid
try:
    confidence = int(confidence)
    if confidence not in range(1,101):
        print("Invalid input. Please restart and enter a valid confidence level.")
        raise SystemExit
except ValueError:
    print("Invalid input. Please restart and enter a valid confidence level.")
    raise SystemExit

print("You have selected a minimum confidence level of {}%".format(confidence))

# %% [markdown]
# ### Data Loading and Preprocessing: ###
# The support and confidence levels entered by the user are converted into a float representing the percentage of support and confidence required. The selected dataset is loaded from the corresponding CSV file, and each transaction is read into an array for future traversal. The set of unique items is generated from the array of transactions by traversing all transactions and adding each unique item to the set. A frequent items dictionary is also initialized to store the frequent items and the support for each item.

# %% [markdown]
# ### Timing: ###
# To time the execution of each algorithm, the time library was used. The start time is recorded when preprocessing has been completed and the algorithm begins identifying frequent items and association rules. The stop time is then determined for both the frequent itemset identification and the association rule identification at the end of printing the frequent itemsets and at the end of printing the association rules respectively. The time to determine frequent itemsets and the time to determine association rules is then calculated as the difference between the stop and start times, and this is calculated for each of the three algorithms and printed to the user on the command line.

# %%
# Open selected sets and transactions
import itertools
import time

support /= 100
confidence /= 100

transactions = ["amazonTransactions.csv", "bestBuyTransactions.csv", "kMartTransactions.csv", "nikeTransactions.csv", "genericTransactions.csv", "customTransactions.csv", "walmartTransactions.csv"]

with open(transactions[dataSelect-1], mode ='r') as file:
  csvFile = csv.reader(file)
  curTrans = []
  for line in csvFile:
    curTrans.append(line)

# All implementations will start with the data in curTrans
# Begin timing from here for comparison
bruteFreqTime = time.time()

# Having the starting sets is redundant. Removing and just find unique items in transactions

curSet = set()
for trans in curTrans:
  for item in trans:
    # Will only add if the item has not been encountered yet since it is a set
    curSet.add(item)

frequentItems = {}

# %% [markdown]
# ### Iterate over Candidate Itemsets of Size K: ###
# Using a brute force method, candidate itemsets of size K will be created, starting with K=1 and increasing by 1 during each iteration. Candidate itemset generation is repeated only if at least 1 frequent itemset was found for the previous value of K and the candidate itemset size does not exceed the number of unique items. 
# 
# * ### Computer Combinations: ###
# Using the itertools library, the candidate set of K-itemsets is created by calculating the combinations of the unique itemset of the specified size K. Each combination is then searched for within the transactional array, and its frequency is calculated.
# 
# * ### Check Support and Store Frequency: ###
# If the frequency divided by the total number of transactions for a given candidate itemset is greater than or equal to the support value specified by the user, the itemset is considered to be frequent and the itemset and support level are stored in the frequent itemset dictionary as a key-value pair. If a frequent item is found, the looping parameter will also be updated to ensure exploration of the next set of candidate itemsets of size K+1.
# 
# * ### Update Candidate Set Size to K+1: ###
# After checking all candidate itemsets of size K, the candidate set size will be incremented by 1 from K to K+1. The program begins the iteration process again, performing the same evaluation to determine if any frequent items were found during the prior iteration. If no frequent itemsets were found, the program will terminate and not explore any larger K-itemsets based on the Apriori Principle.
# 

# %%
# Check all sizes of combinations until one is not found or reach max len
# Originally was going to limit the size of the combinations as being checked, but upon review realized that this was not truly brute force
# Removed optimization

found = 1
i = 1
while (i <= len(curSet) and found > 0):
  found = 0

  # For each combination of size i
  for combination in itertools.combinations(curSet, i):
    # Count support of combination by iterating through the transactions
    count = 0

    for trans in curTrans:
      # Cast combination to a set to use the issubset function
      # Check if combination occurs in transaction and incriment count
      if set(combination).issubset(trans):
        count += 1
    
    if count/len(curTrans) >= support:
      # Save frequent items
      frequentItems[combination] = count/len(curTrans)
      # Found at least one frequent item in this size of combinations
      found += 1

  # Check next combination size
  i += 1

# %% [markdown]
# ### Print Frequent Itemsets: ###
# For each itemset identified as frequent and stored in the frequent itemsets dictionary, the frequent itemset and support value for that itemset are printed to the user on the command line.

# %%
print("\nBrute Force Frequent Itemsets\n")

for i, (items, supp) in enumerate(frequentItems.items()):
    print("Frequent Itemset {}: [{}]\nSupport: {:0.2f}%\n".format(i+1, ", ".join(items), supp*100))

# Frequent items generated, end timing
bruteFreqTime = time.time() - bruteFreqTime

print("Generated Brute Force Frequent Itemsets in {} seconds".format(bruteFreqTime))

# %% [markdown]
# ### Iterate over Frequent Itemsets to Find Association Rules: ###
# An association rules array is initialized to store association rules as discovered. The stored frequent itemsets previously discovered are now iterated over for all itemsets with at least 2 unique items. 
# 
# * ### Generate Increasing Large Combinations as an Antecedent for each Itemset: ###
# Each frequent itemset is composed of unique items. All subsets of the current frequent itemset being evaluated will be generated, starting with subsets of size 1 and increasing until one less than the size of the frequent itemset. Each subset generated will represent the antecedent in the association rules to be tested. For each antecedent, which must be a frequent itemset previously explored due to the Apriori Principle, the support of the itemset can be divided by the support of the antecedent by finding their associated values in the frequent items dictionary. The resulting value is the confidence of the association rule.
# 
# * ### Check Confidence and Store Association Rules: ###
# If the confidence of the association rule is greater than or equal to the user specified confidence level, the consequent can be calculated by removing the antecedent from the itemset, and the association rule is stored as the antecedent, consequent, confidence, and support in a tuple.
# 

# %%
bruteRuleTime = time.time()

associationRules = []

for itemset in frequentItems:
    if len(itemset) > 1:

        # For all subsets of the itemset
        for i in range(1, len(itemset)):
            for ant in itertools.combinations(itemset, i):
                # Check confidence
                if frequentItems[itemset]/frequentItems[ant] >= confidence:
                    cons = tuple(set(itemset) - set(ant))
                    # Store antecedent, consequent, confidence, support
                    associationRules.append((ant, cons, frequentItems[itemset]/frequentItems[ant], frequentItems[itemset]))

# %% [markdown]
# ### Print Association Rules: ###
# For each association rule identified and stored in the association rules array, the antecedent, consequent, confidence, and support is printed to the user on the command line.

# %%
print("\nBrute Force Association Rules\n")

for i in range(len(associationRules)):
    print("Association Rule {}: [{}] -> [{}]\nConfidence: {:0.2f}%\nSupport: {:0.2f}%\n".format(i+1, ", ".join(associationRules[i][0]), ", ".join(associationRules[i][1]), associationRules[i][2]*100, associationRules[i][3]*100))

# Association rules generated, end timing
bruteRuleTime = time.time() - bruteRuleTime
print("Generated Brute Force Association Rules in {} seconds".format(bruteRuleTime))
print("#"*64)

# %% [markdown]
# ## Part 3 Details
# Use an existing Apriori implementation from Python libraries/packages to
# verify the results from your brute force algorithm implementation.
# * Use Python existing package for fpgrowth (as known as fp-tree algorithm)
# to generate the items and rules.
# * Compare the results from your brute-force, Apriori, and FP-Tree/Growth.
# * Do the three algorithms produce the same results?
# * Report the timing performance for all three algorithms as well.
# * Which one is faster?
# So, for all three algorithms, generate and print out all the association rules and
# the input transactions for each of the 5 transactional databases you created/used.
# The data set selection, support, and confidence must be user-specified
# parameters, so the output should show different rules with respect to different
# databases and different support/confidence.
# Make sure to show multiple support and confidence results for each data set.
# You should prompt the user only once for the input and reuse for the three
# algorithms in each run.
# The items and transactions must be clear and easy to identify. Your
# program should show the performance time for each algorithm.

# %% [markdown]
# ### Results and Evaluation: ###
# The accuracy of my brute force implementation is verified by comparing the results of two library-based implementations of the Apriori and FP-growth algorithm to determine frequent itemsets and association rules. The time taken to execute each of these methods is then compared to illustrate the differences in execution time for each implementation.
# 
# * ### Existing Libraries used to Validate: ###
# The mlxtend library was used to validate the results of my brute force implementation. The same dataset, support, and confidence as previously specified by the user are used to inform the Apriori and FP-Growth algorithms and recalculate the frequent itemsets. This information is then passed to the mlxtend association rule function to determine the association rules for both the Apriori and FP-Growth algorithms. The same print output is generated by iterating through the output of each algorithm.
# 
# * ### Difference in Data Representation: ###
# A notable difference in the implementation of my brute force algorithm and the mlxtend implementations is the use of a pandas dataframe. My implementation of the brute force algorithm relies on a 2D array to represent the transactions, where the mlxtend algorithms take in a pandas dataframe. To create this dataframe, the transactions were first encoded and transformed to ensure equal dimensions in each transaction were represented as a row in the dataframe. This difference does not impact the data itself, but does change how it is represented and stored. The use of a pandas dataframe may have an influence on the timing of these algorithms as compared to the use of a 2D array.
# 

# %%
import mlxtend
import mlxtend.frequent_patterns
import mlxtend.preprocessing
import pandas as pd

transEncoder = mlxtend.preprocessing.TransactionEncoder()
transEncoderArr = transEncoder.fit(curTrans).transform(curTrans)
transDF = pd.DataFrame(transEncoderArr, columns=transEncoder.columns_)

# Begin timing from here for comparison
aprioriFreqTime = time.time()

aprioriFreqItems = mlxtend.frequent_patterns.apriori(transDF, min_support=support, use_colnames=True)

print("\nApriori Frequent Itemsets\n")

for index, row in aprioriFreqItems.iterrows():
    print("Frequent Itemset {}: [{}]\nSupport: {:0.2f}%\n".format(index+1, ", ".join(row["itemsets"]), row["support"]*100))

aprioriFreqTime =  time.time() - aprioriFreqTime

print("Generated Apriori Frequent Itemsets in {} seconds".format(aprioriFreqTime))

# %%
aprioriRulesTime = time.time()

if not aprioriFreqItems.empty:
    aprioriRules = mlxtend.frequent_patterns.association_rules(aprioriFreqItems, metric="confidence", min_threshold=confidence)
else:
    aprioriRules = pd.DataFrame(columns=["antecedents", "consequents", "confidence", "support"])

print("\nApriori Association Rules\n")

for index, row in aprioriRules.iterrows():
    print("Association Rule {}: [{}] -> [{}]\nConfidence: {:0.2f}%\nSupport: {:0.2f}%\n".format(index+1, ", ".join(row["antecedents"]), ", ".join(row["consequents"]), row["confidence"]*100, row["support"]*100))

aprioriRulesTime = time.time() - aprioriRulesTime

print("Generated Apriori Association Rules in {} seconds".format(aprioriRulesTime))
print("#"*64)

# %%
# Begin timing from here for comparison
fpFreqTime = time.time()

fpFreqItems = mlxtend.frequent_patterns.fpgrowth(transDF, min_support=support, use_colnames=True)

print("\nFP-Growth Frequent Itemsets\n")

for index, row in fpFreqItems.iterrows():
    print("Frequent Itemset {}: [{}]\nSupport: {:0.2f}%\n".format(index+1, ", ".join(row["itemsets"]), row["support"]*100))

fpFreqTime =  time.time() - fpFreqTime

print("Generated FP-Growth Frequent Itemsets in {} seconds".format(fpFreqTime))

# %%
fpRulesTime = time.time()

if not fpFreqItems.empty:
    fpRules = mlxtend.frequent_patterns.association_rules(fpFreqItems, metric="confidence", min_threshold=confidence)
else:
    fpRules = pd.DataFrame(columns=["antecedents", "consequents", "confidence", "support"])

print("\nFP-Growth Association Rules\n")

for index, row in fpRules.iterrows():
    print("Association Rule {}: [{}] -> [{}]\nConfidence: {:0.2f}%\nSupport: {:0.2f}%\n".format(index+1, ", ".join(row["antecedents"]), ", ".join(row["consequents"]), row["confidence"]*100, row["support"]*100))

fpRulesTime = time.time() - fpRulesTime

print("Generated FP-Growth Association Rules in {} seconds".format(fpRulesTime))
print("#"*64)

# %% [markdown]
# ## Part 4 Details
# Github & Jupyter Notebook.
# * After you finish your code in development and testing
# and make sure it works, and prepare the report (meaning
# all heavy lifting job is done ), Create a Github
# repository in https://github.com/. Your account must be
# with your NJIT email not your personal email (unless if
# you have to, but indicate that in your report as well).
# * Load your project to the repository.
# * Create Jupyter notebook for your work to show the
# output, for more info visit https://jupyter.org/
# * Give me ya54@njit.edu access as a collaborator to your
# repository. (If we have a grader, you give him/her access
# too).
# * Add Github link to your repository to your report.



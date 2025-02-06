""" Assignment_02 source code"""

__author__ = "Kelton Zinn"

__version__ = "1.0.0"

# SIMPLE DATA TYPES

name = "Kelton"

print(type(name))

print("name:", name, "type:", type(name))

has_license = True

print("has license:", has_license, "type:", type(has_license))

Year = 2025

print("This year:", Year, "type:", type(Year))

Next_year = Year + 1

print("Next year:", Next_year, "type:", type(Next_year))

# MATHEMATICAL OPERATIONS

GST = 0.05

PST = 0.07

vehicle_price = 80000

federal_tax = vehicle_price * GST

provincial_tax = vehicle_price * PST

final_cost = federal_tax + provincial_tax + vehicle_price

print("Purchase price:", vehicle_price, "Provincial tax:", provincial_tax, "Federal tax:", federal_tax, "Total:", final_cost)

print(f"Purchase price: ${vehicle_price:,.2f}", f"Provincial tax: ${provincial_tax:,.2f}", f"Federal tax: ${federal_tax:,.2f}", f"Total: ${final_cost:,.2f}")

# LISTS

integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(type(integers))

print("List:", integers)

name = "Kelton"

integers.insert(5, name)

print(integers)

integers.remove(9)

print(integers)

letters = ["A", "B", "C"]

catalogue = integers + letters 

print(catalogue)

# TUPLES

Provinces = ("ON", "MB", "AB", "SK")

print(type(Provinces))

print(Provinces)

# DICTIONARIES

coins = {
    'nickel': 0.05,
    'dime': 0.10,
    'quarter': 0.25
}
print(type(coins))

print(coins)

coins['nickel'] = 5
coins['dime'] = 10 
coins['quarter'] = 25

print(coins)

coins['loonie'] = 100
coins['toonie'] = 200

print(coins)


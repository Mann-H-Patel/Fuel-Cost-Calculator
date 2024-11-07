print("")
print("--- Fuel Cost Calculator ---")
print("This program will help you calculate the cost of fuel required to travel a specific distance.")

print("\nPlease enter the following details:")

mileage = int(input("1. Your Vehicle Mileage (KM per Liter): "))
fuel_price = float(input("2. Fuel Price (Per Liter): "))
km = int(input("3. Distance to Travel (KM): "))

fuel_needed = km / mileage  
total_cost = fuel_needed * fuel_price  

price_per_km = fuel_price / mileage

print("")
print("--- Results ---")
print(f"Total cost of fuel to travel {km} KM: {total_cost:.2f} currency units")
print(f"Cost per KM of travel: {price_per_km:.2f} currency units\n")
print("")


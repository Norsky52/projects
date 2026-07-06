print("===Road Trip Budget Planner===")



# 1. Gather inputs from the user
destination=str(input("Where to?"))
Distance = float(input("how many miles?"))
days = int(input("How many days is the trip? "))
gas_money = float(input("Estimated total gas cost? $"))
Airlines_money = float(input("Airline cost? $"))
hotel_per_night = float(input("Hotel cost per night? $"))
food_per_day = float(input("Food budget per day? $"))
# 2. get the totals
print("--- Cost Breakdown ---")
total_hotel = hotel_per_night * (days - 1)
total_food = food_per_day * days
total_airline = Airlines_money
total_cost = gas_money + total_hotel + total_food 
# 3. Display the results
print("\n--- Road Trip Budget Summary---")
print(f"Total Gas: ${gas_money:.2f}")
print(f"Total Hotel:  ${total_hotel:.2f}")
print(f"Total Food:   ${total_food:.2f}")

print("-" * 22)
print(f"GRAND TOTAL:  ${total_cost:.2f}")
print(f"Per Day Cost: ${total_cost / days:.2f}")

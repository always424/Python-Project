# Shopping Cart

foods = []
total_Prices = 0

while True :
    food = input("Enter a food you want to buy (q to quit) : ")

    if food.lower() == "q":
        break
    else:
        prices = float(input(f"Enter the price of the {food} : "))
        foods.append(food)
        total_Prices+=prices


print("__________YOUR CART__________")
print("-----------------------------")
for food in foods:
    print(f"     {food} ")
print("-----------------------------")
print("-----------------------------")
print(f"The total cost of is = {total_Prices}")

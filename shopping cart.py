# Create a shopping card programme that will continuously ask the user for a food product and the price of that product
# Have an exit clause if the wishes to stop adding more things to their cart
# At the end the food items and the total cost th the user


foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy or press q to quit: ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of the {food}: R"))
        foods.append(food)
        prices.append(prices)
        
        print("......YOUR CART......")
        
        for food in foods:
            print(food, end= " ")
            
            for price in prices:
                total += price
                
                print("\n")
                print(f"your total is:  R{total}")
''' write a py program 
1)To display a menu of food items(List)
2) Create a tuple of prices with respect to food items List
3)Ready the input from the user for ordering the food including the Quantity
    if it exists in the menu --confirm order
    if not print a message ---
4)while Billing , read Phone nUmber , feed back, read Tip amount
5)add 18% gst to the bill & print the bill if bill>0      

'''

FoodItem=['Chicken Biryani','Chicken Thikka','Mutton Biryani','Prawns fry']
price=(289,189,359,499)
n=input("Enter the food items you would like to order: ")
if n in FoodItem:
    print("--confirm order")
elif n not in FoodItem:
    print("--Item not available")
    
    

















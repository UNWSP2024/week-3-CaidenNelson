hot_dog_type = input("would you like a Chili dog or a Hot Dog? ")
#get topping
toppings = input("Would you like cheese, peppers, or grilled onions ")
#define variables
cheese_price  = 0
onion = 0
pepper_price =0
hot_dog_price = 0
#determine price of toppings and if they are on the dog
if toppings == 'cheese' or toppings == 'Cheese':
    cheese_price = .5

elif toppings == 'grilled onions' or toppings == 'Grilled onions' or toppings == 'Grilled Onions':
    onion = 1.00

elif toppings == 'peppers' or toppings == 'Peppers':
    pepper_price = .75
#determine price of dog and what kind of dog
if hot_dog_type == 'Hot Dog' or hot_dog_type == 'Hot dog' or hot_dog_type == 'hot dog':
    hot_dog_price = 3.5,
elif hot_dog_type == 'Chili Dog' or hot_dog_type == 'Chili dog' or hot_dog_type == 'chili dog':
    hot_dog_price = 4.5
#get topping price
topping_price = cheese_price + onion + pepper_price
#get tax
tax = (topping_price + hot_dog_price)*.07
#round tax
tax = round(tax,3)
#get total price
total_price = tax+topping_price + hot_dog_price
#displat price of dog, tax, and total price
print('Your hot dog will cost',hot_dog_price,'$ the tax will be',tax,'$ the total will be',total_price,'$')


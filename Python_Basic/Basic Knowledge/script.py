#this is a statement of lovely_loveseat_description
lovely_loveseat_description="""Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."""
#this is a statement of lovely_loveseat_price
lovely_loveseat_price = 254.00
#this is a statement of stylish_settee_description
stylish_settee_description="""Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""
#this is a statement of stylish_settee_price = 180.50
stylish_settee_price = 180.50
#this is a statement of luxurious_lamp_description
luxurious_lamp_description = """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."""
#this is a statement of luxurious_lamp_price
luxurious_lamp_price = 52.15
#this is a statement of lsales_tax
sales_tax = .088

customer_one_total = 0

customer_one_itemization = ""

customer_one_total += lovely_loveseat_price

customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price

customer_one_itemization += luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax

customer_one_total += customer_one_tax
# this will print  Customer one items
print("Customer One Items:")

print(customer_one_itemization)

print("Customer One Total:")
#question
print(f"${customer_one_total:.2f}")
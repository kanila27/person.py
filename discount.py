def calculate_discount(price,discount_percent):
    #check if discount is 20% or higher
    if discount_percent>=20:
        #calculate the discount amount
        discount_amount=(discount_percent/100)*price
        #Apply the discount to get the final price
        final_price =price - discount_amount
        return final_price
    else:
        #if the discount is less than 20%, return the original price
        return price
    #prompt the user for the original price and the discount percentage
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage=float(input("Enter the discount percentage: "))
    #calculate the final price
    final_price=calculate_discount(original_price,discount_percentage)
    #print the final price or the original price

    if discount_percentage >= 20:
        print(f"the final price after applying the discount is:{final_price}")
    else:
        print(f"No discount was applied.The original price is {original_price}")

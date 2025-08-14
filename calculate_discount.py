def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = (100 - discount_percent) / 100 * price
        print(f"The answer from the formula: {final_price}")
        return final_price
    else:
        print("No discount applied, returning original price")
        return price
# this formula takes the original percent which 100 minus the discount percent,
# converts it to a decimal by dividing with 100, then multiplies it by the original price to get the final discounted price.
    

original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percent) #this calls the calculate_discount function.
if discount_percent >= 20:
    print(f"Final Price: {final_price} (after {discount_percent}% discount)")
else:
    print(f"No discount. Original Price: {original_price}")


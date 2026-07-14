#David Edwards
#2026-CAX-176
#July 13, 2026
#Simple Discount Calculator

# Define function
def calculate_price(original_price, discount_rate=0.10):

    # return sends the calculated value back to whoever called the function
    return original_price - (original_price * discount_rate)

# Ask for the price to be discounted
price = float(input('Enter price: $'))

# Price after calculation
final_price = calculate_price(price)

# Print the value with 2 behind decimal since its money
print(f'${final_price:.2f}')
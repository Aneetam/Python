def get_discount(amount):
    # Complete this function
    if amount<500:
        print("5%")
    elif amount>=500 and amount<2500:
        print("10%")
    elif amount>=2500:
        print("20%")
    else:
        print()


amount = int(input())
# Call the get_discount function
get_discount(amount)
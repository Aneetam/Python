def calculate_bill(amount):
    dis=0
    # Complete this function
    if amount<500:
        dis=amount-(amount*(5/100))
        return dis
    elif amount>=500 and amount<2500:
        dis=amount-(amount*(10/100))
        return dis
    elif amount>=2500:
        dis=amount-(amount*(20/100))
        return dis
        
        


amount = int(input())
# Call the calculate_bill function
result=calculate_bill(amount)
print(result)
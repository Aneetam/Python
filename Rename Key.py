fruits = {
    "apples": 10,
    "bananas": 20,
    "mangoes": 15,
    "oranges": 200,
    "watermelons": 50
}

# Write your code here
old_key=input()
new_key=input()
updated_fruits={}
for key,value in fruits.items():
    if key==old_key:
        updated_fruits[new_key]=value
    else:
        updated_fruits[key]=value
fruits_list=list(updated_fruits.items())
print(fruits_list)
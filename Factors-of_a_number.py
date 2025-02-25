def factors_of_n(number):
    num_list = []
    for i in range(1, number + 1):
        if number % i == 0:
            num_list.append(str(i))  # Convert to string before adding to the list
    return " ".join(num_list)  # Join the list of strings with spaces

number = int(input())
result = factors_of_n(number)
print(result)
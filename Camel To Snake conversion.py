def camel_to_snake(camel_str):
    snake_str = ""
    for char in camel_str:
        if char.isupper():
            if snake_str:  # Add underscore before uppercase letter (except at start)
                
                snake_str += "_"
            snake_str += char.lower()
        else:
            snake_str += char
    return snake_str

# Example usage
camel_case_str = input("")
snake_case_str = camel_to_snake(camel_case_str)
print( snake_case_str)
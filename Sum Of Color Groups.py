def color_sum(input_str):
    pairs = input_str.split(",")
    color_dict = {}

    # Process each pair
    for pair in pairs:
        color, value = pair.split(":")
        value = int(value)

        # Add the value to the corresponding color
        if color in color_dict:
            color_dict[color] += value
        else:
            color_dict[color] = value

    # Convert the values of 'r' and 'g' to strings
    for key in color_dict:
        if key in ['r', 'g']:
            color_dict[key] = str(color_dict[key])

    return color_dict

# Input
input_str = "r:1,g:2,r:3,b:1,g:4"
print(color_sum(input_str))
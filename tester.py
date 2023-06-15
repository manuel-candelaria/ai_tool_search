input_string = "#cherry #apple #orange"

output_list = input_string.split("#")[1:]  # Split and remove the first empty element

result = [item.strip() for item in output_list]  # Remove leading/trailing whitespace

print(result)

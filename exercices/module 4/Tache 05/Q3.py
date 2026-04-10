colors_tuple = ("red", "green", "blue")

colors_list = list(colors_tuple)
colors_list[1] = "yellow"

colors_tuple_modified = tuple(colors_list)

print(f"Original: {('red', 'green', 'blue')}")
print(f"Modified: {colors_tuple_modified}")
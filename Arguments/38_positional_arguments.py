# positional arguments = arguments that must be passed in the correct order
#                        Python assigns them based on their position, not name
#                        changing the order changes which parameter receives the value


def rectangle_area(length, width):
    return length * width

print(rectangle_area(10, 4))   # length=10, width=4
print(rectangle_area(4, 10))   # length=4, width=10
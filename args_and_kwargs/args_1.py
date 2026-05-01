# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyord-arguments
#   * unpacking operator

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 4))
# **kwargs = allows you to pass multiple keyord-arguments
#   * unpacking operator

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="Bay Harbor Club",
              apt="10B",
              city="Miami",
              state="Florida",
              zip="123456")


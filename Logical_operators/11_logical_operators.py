# and, or, not
# or = atleast one condition must be true
# and = both conditions must be true
# not = inverts the condition (not false, not true)

temp = -5
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled.")
else:
    print("The ooutoor event is still scheduled.")
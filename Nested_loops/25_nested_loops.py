# A loop within another loop (outer, inner)
# outer loop:
#     inner loop:

for x in range(3):
  for x in range(1, 10):
    print(x, end="")
  print()
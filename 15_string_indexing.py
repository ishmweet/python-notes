# indexing = accessing elements of a sequence using [] (indexing operator)
# [start : end : step]

credit_number = "1234-5678-9012-3456"
last_digits = credit_number[-4:]
credit_number = credit_number[::-1]
print(credit_number)

#print(f"XXXX-XXXX-XXXX-{last_digits}")

#print(credit_number[1])
#print(credit_number[0:4])
#print(credit_number[5:9])
#print(credit_number[5:])
#print(credit_number[-2])
#print(credit_number[::3])
alphabet="0123456789abcd"
for x in alphabet:
    f=int(f'1{x}563', 14)+int(f'871{x}3', 14)
    if f%24==0:
        print(f//24)
        break
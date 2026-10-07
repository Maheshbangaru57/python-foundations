bill = float(input("Bill: "))
tip_percentage = float(input("Tip percentage: "))

tip = bill * tip_percentage / 100
total = bill + tip

print("Total:", total)

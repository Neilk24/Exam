kilowatts = int(input("Enter the number of kilowatts you have consumed this year: "))
if kilowatts<5:
    amount = ((kilowatts + 10)//2)**2
    surcharge = 0

elif kilowatts<20:
    amount = kilowatts*5.63
    surcharge = 45

elif kilowatts<=50:
    amount = kilowatts*9.83
    surcharge = 69

elif kilowatts<=100:
    amount = kilowatts**2
    surcharge = 75

else:
    amount = kilowatts**3
    surcharge = kilowatts**(1.5)

total_amount = amount + surcharge

print("Your total price is ~ %.2f" %total_amount)
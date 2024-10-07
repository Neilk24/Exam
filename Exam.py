medical_cause = input("Do you have a medical cause? Enter Y or N: ")
attendance = int(input("Enter the total amount of attendace for this student: "))

if medical_cause == "Y":
    print("You are allowed.")

else:
    if attendance>=75:
        print("You are allowed.")

    else:
        print("You are not allowed.")
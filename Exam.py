attendance=int(input("Enter Your Attendance (%): "))
fees=(input("Fees Paid (Yes/no): "))

if attendance >= 75 and fees == "Yes":
    print("Eligible!")

elif attendance < 75:
    print("short Attendance Bhai")

else:
    print("Pay Fees")
   
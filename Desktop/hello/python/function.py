print("Enter Marks Obtained in 5 Subjects: ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())
tot = markOne+markTwo+markThree+markFour+markFive
avg = tot/5
print("Average=%.2f"%avg)
if avg>=70 and avg<=100:
    print("Your Grade is A")
elif avg>=60 and avg<=69:
    print("Your Grade is B")
elif avg>=50 and avg<=59:
    print("Your Grade is C")
elif avg>=40 and avg<=49:
    print("Your Grade is D")
elif avg>=0 and avg<=39:
    print("Your Grade is F")
else:
    print("Invalid Input!")
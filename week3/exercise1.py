score = int(input("Enter your score: (0-100)"))
if score >= 90:
    Grade = "A"
    print("Excellent work")
elif score >=80:
    Grade = "B"
    print ("Good work")
elif score >=70:
    Grade = "C"
elif score >=60:
    Grade = "D"
else:
    Grade = "F"
    print("You failed")
print(f" Your Grade is: {Grade}")


#Bonus for excellent students
if score ==100:
    print(" You are the top student")
    


    


    
    

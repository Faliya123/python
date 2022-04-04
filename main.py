#1,2,3
#2
#type(2)
#str

#a=input("enter your number=")
#b=input("enter your number=")
#c=input("enter your number=")
#sum=(int(a)+int(b)+int(c))/(3)
#print(sum)

print("Hello karnataka")

def calculate_highest_in_Math(Student_list):
    Highest_score_in_Math = 0
    Highest_score_in_Math_Name = " "

    for student in Student_list:
        if (student.get("Math") > Highest_score_in_Math):
            Highest_score_in_Math = student.get("Math")
            Highest_score_in_Math_Name = student.get("Name")

    print(f"The Highest scores in Math is {Highest_score_in_Math} by {Highest_score_in_Math_Name}")


def calculate_highest_in_Social(Student_list):
    Highest_score_in_Social = 0
    Highest_score_in_Social_Name = " "

    for student in Student_list:
        if (student.get("Social") > Highest_score_in_Social):
            Highest_score_in_Social = student.get("Social")
            Highest_score_in_Social_Name = student.get("Name")

    print(f"The Highest scores in Social is {Highest_score_in_Social} by {Highest_score_in_Social_Name}")

student1={
    "Math":45,
    "Social":75,
    "Science":96,
    "Name":"Tanmay"
}

student2={
    "Math":74,
    "Social":83,
    "Science":100,
    "Name":"Dheeraj"
}

student3={
    "Math":98,
    "Social":62,
    "Science":23,
    "Name":"Sooraj"
}

Student_list = [student1, student2, student3]

calculate_highest_in_Math(Student_list)
calculate_highest_in_Social(Student_list)








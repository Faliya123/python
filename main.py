#1,2,3
#2
#type(2)
#str

#a=input("enter your number=")
#b=input("enter your number=")
#c=input("enter your number=")
#sum=(int(a)+int(b)+int(c))/(3)
#print(sum)

import random
print("Hello karnataka")
student_list = {
    "dammala_dinesh_paul": {
        "maths": random.randint(1, 100),
        "science": random.randint(1, 100),
        "english": random.randint(1, 100)
    },
    "faliya_khan": {
        "maths": random.randint(1, 100),
        "science": random.randint(1, 100),
        "english": random.randint(1, 100)
    },
    "ravi": {
        "maths": random.randint(1, 100),
        "science": random.randint(1, 100),
        "english": random.randint(1, 100)
    }
}


def get_the_highest_score(student_name):
    sorted_s1 = {}
    for i in sorted(student_list[student_name].values(), reverse=True):
        for j in student_list[student_name].keys():
            if student_list[student_name][j] == i:
                sorted_s1[j] = i
    return f"The Highest Scored Subject of the {student_name} in all the subject's is ____{str(list(sorted_s1)[0]).upper()}_____"


loop_student = True
while loop_student:
    get_student_name = input(f"Enter the name of the student in the list {[i for i in student_list.keys()]} = ")
    print(get_the_highest_score(get_student_name))
    loop_again = input("Do You Want to Repate(Yes/No)? = ").capitalize()
    if loop_again != "Yes":
        exit()








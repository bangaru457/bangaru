#SimpleIF Statements

#1 sample program enter the marksmarks = eval(input("Enter the Marks:"))
if marks>=35:
    print("you're passed")
    print("Congratulations")

#2 IF-ELSE Program.

    marks = eval(input("Enter the students:"))
    if marks >=35:
        print("you're passed")
        print("Congratulations......")
    else:
        print("you're failed...")
        print("better luck next time")

#3 If given given number is Even or odd number

n = eval(input("Enter the number:"))
if n%2 == 0:
    print("Print even number is:",n)



name = input("Enter the name: ")
age  = int(input("Enter the age: "))
if age >= 18:
    print("print you're eligible for the cast the vote...")
    print('Hello',name)
else:
        print("you're not eligible for the cast the vote..")
        print('hello',name)

#4 Calcluthe the Percentage marks for the Student.
p = eval(input("Enter the Student marks:" ))
if p >=0 and p < 35:
    print("youre failed..")
    print("better luck next time..")
elif p >35 and p<=60:
    print("Congratulations.....")
    print("youre passed B grade..")
elif p>=60 and p < 75:
        print("congaratulations...")
        print("youre passed in A grade")
elif p>=75 and p <=100:
        print("Congratulatuons....")
        print("DIStinct marks you got.")
else:
        print("Invalid marks...")

#5 check the course.

course = input("Enter the Course name: ")

courses = ['Python','java','AWS','C']

if course == 'Python':
    print("It's Good programming laungague..")
elif course == 'java':
    print("Java is good laungaue but no calls.")
elif course == 'AWS':
    print("It's emegring technology to get the jobs.")
elif course == 'C':
    print("One of the oldest programming laungage.")
elif course in courses:
    print("ok it's good")
else:
    print("Ok..learn well.")


#6 which city has famous for what?

city = input("Enter the City Name:").upper()
if city == 'HYD' :
    print("famous for biryani and educational corses")
elif city == 'Ban':
    print("Famous for IT jobs")
elif city == 'Che':
    print("famous for beaches")
elif city == "kerala" :
    print("famous for coconuts")
else:
    print("Invalid country")

#7 Numbers for even or add .

n = eval(input("Enter any Number:"))
if n > 0:
     if n%2 ==0:
          print("positive and even number")
     else:
          print("Negative and even number")

if n < 0 :
    if n%2 ==0:
          print("postive and odd number")
    else:
          print("negative and odd number")   
else:
    print("Inavlid Number")


#8 wrt program pass or fail

ans = input("did you attend the exam: ")
if ans == 'yes':
    marks = eval(input("what are your marks: "))
    if marks >=35:
          print("assignmnet is completed and pass")
    else:
        print("you have to practise more")
elif ans == 'no':
    print("you have to practise and submit the assignment")

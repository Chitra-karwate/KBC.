question_list = [
    "How many continents are there?",
    "What is the capital of India?",
    "NG mei kaun se course padhaya jaata hai?"
]

options_list = [
    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"],]
solution_list = [3, 4, 1]

lifeline = [
    ["(2)Nine" , "(3)Seven"],
    ["(2)Bhopal", "(4)Delhi"],
    ["(1)Software Engineering", "(4)Agriculture"]
]
print("WELCOME TO KBC 🙏 🙏")

i = 0
money = 0
c = 0
while i<len(question_list):
    print(question_list[i])
    j=0
    while j<len(options_list[i]):
        d=options_list[i][j]
        print(d)
        j=j+1
    if c <2:
        user_input=input("do you using lifeline : ")
        if user_input=="yes":
            c += 1
            print("5050",lifeline[i])
    else:
        print("Sorry !, you can't use lifeline becuase you already used lifeline.")
    b=int(input("choose the answer : "))
    if b==solution_list[i]:
        money+=5000
        print("your answer is correct")
        print("You win Rs./-", money)
    else:
        print("your ans is wrong ")
        break
    i += 1
    





import re
print("Our magical calculator")
print("Type 'q' and press enter to quit")
run = True
remain = ""
equation = 0
while run:
    check = str(input("type your equation"))
    check = re.sub('[A-Za-pr-z,.?><#@!()]', '', check)
    if check == "q":
        run = False
        print("Thanks for using our app")
    else:
        while check != "q":
            try:
                equation = eval(remain+check)
                remain = str(equation)
            except SyntaxError:
                print("Please check your equation")
            check = str(input(remain))
            check = re.sub('[A-Za-pr-z,.?><#@!()]', '', check)
        run = False
        print("Thanks for using our app")
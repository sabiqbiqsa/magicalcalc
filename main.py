import re
print("our magical calculator")
run=True
remain=0
while run:
    check = str(input("type your equation"))
    check= re.sub('[A-Za-pr-z,.?/><#@!()]','',check)
    if check=="q":
        run=False
        print("Thanks for using our app")
    else:
        while check!="q":
            remain += eval(check)
            check = str(input(remain))
            check = re.sub('[A-Za-pr-z,.?/><#@!()]', '', check)
        run = False
        print("Thanks for using our app")
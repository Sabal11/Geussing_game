a = 9 # correct answer
i = 1
while i <=3:
    num = input ("Guess The Number: ")
    if int(num) == a:
        print ("You Won Congratulation :-)")
        break
    i = i + 1
else: 
     print ("You lost...Try Again")
    


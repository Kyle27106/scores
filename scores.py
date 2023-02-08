def check(score):
    if score < 50: 
        print("Fail")
    else:
        print("Pass")

score = (int)(input("Please Enter a Score: "))
while score >= 0:
    check(score)
    score = (int)(input("Please Enter a Score: "))
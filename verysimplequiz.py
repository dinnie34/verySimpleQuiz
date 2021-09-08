##### Variables
score = 0
total_q = 4

##### Main
print('Hello, you smell bad!')

ans = input('Ready pal? (yes/no): ').lower()
if ans in ['yes']:
    ans = input('1.in What is 2 and 2 added together? ')
    if ans in ['4']:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")


    ans = input('2. What is the capital of Ohio? ').lower()
    if ans in ['columbus']:
        score += 1
        print('Correct')
    else:
        print('Incorrect')


    ans = input('3. Is Tyler gay? ').lower()
    if ans in ['yes']:
        score += 1
        print('Correct')
    else:
        print('y ou shou ld not h ave don e that')


    ans = input('4. Did you answer yes on the last question? ').lower()
    if ans in ['yes', 'y', 'yeah']:
        score += 1
        print('Correct')
    elif ans in ["maybe"]:
        print("gfgdfh")
    else:
        print('b ett er no t sl eep a lon e')


    print(' Thank you for playing, you got' ,score, "questions correct.")
    mark = (score/total_q) * 100

    print("Mark: ", mark)
print('I will be watching :)')
input()




    

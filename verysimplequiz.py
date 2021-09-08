print('Hello, you smell bad!')

ans = input('Ready pal? (yes/no): ')
score = 0
total_q = 4

if ans.lower() == 'yes':
    ans = input('1. What is 2 and 2 added together? ')
    if ans == '4':
        score += 1
        print('Correct')
    else:
        print('Incorrect')


    ans = input('2. What is the capital of Ohio? ').lower()
    if ans == 'columbus':
        score += 1
        print('Correct')
    else:
        print('Incorrect')


    ans = input('3. Is Tyler gay? ')
    if ans.lower() == 'yes':
        score += 1
        print('Correct')
    else:
        print('y ou shou ld not h ave don e that')


    ans = input('4. Did you answer yes on the last question? ')
    if ans.lower() == 'yes':
        score += 1
        print('Correct')
    else:
        print('b ett er no t sl eep a lon e')


    print(' Thank you for playing, you got' ,score, "questions correct.")
    mark = (score/total_q) * 100

    print("Mark: ", mark)
print('I will be watching :)')




    

def pay_ratio(option1, option2):
    
    procent1 = option1/100
    procent2 = option2/100
    
    ans1 = 1/procent1
    ans2 = 1/procent2
    
    print(ans1)
    print(ans2)
    
option1 = int(input())
option2 = 100 - option1

pay_ratio(option1, option2)


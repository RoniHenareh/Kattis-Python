ord = input()
nytt_ord = list(ord)

svar = 0
for i in range(len(nytt_ord)-1):
    
    första = nytt_ord[i]
    andra = nytt_ord[i+1]
    
    if första == 's' and andra == 's':
        svar += 1

if svar >= 1:
    print('hiss')
else:
    print('no hiss')



   
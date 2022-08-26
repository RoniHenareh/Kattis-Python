värden = input()
bokstäver = list(värden)

boll = 1

vänster = 1
mitten = 0
höger = 0

for i in bokstäver:
   
    if i == 'A' and vänster == 1:
        
        boll = 2
        vänster = 0
        mitten = 1
        
    elif i == 'A' and mitten == 1:
        
        boll = 1
        mitten = 0
        vänster = 1
        
    if i == 'B' and mitten == 1:
        
        boll = 3
        mitten = 0
        höger = 1
        
    elif i == 'B' and höger == 1:
        
        boll = 2
        höger = 0
        mitten = 1
        
    if i == 'C' and höger == 1:
        
        boll = 1
        höger = 0
        vänster = 1
    
    elif i == 'C' and vänster == 1:
        
        boll = 3
        vänster = 0
        höger = 1
    
print(boll)
    
        
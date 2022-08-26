
# impact factor = citations / published articles

x = input().split()

published_articles = int(x[0])
impact_factor = int(x[1])

svar = (impact_factor-1) * published_articles
    
print(svar+1)
import datetime

tal = input().split()
dag = int(tal[0])
månad = int(tal[1])

x = datetime.datetime(2009, månad, dag)

print(x.strftime("%A"))
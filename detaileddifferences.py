import sys

# skillnad = *, likhet = .

n = int(input()) * 2

lines = list()
for line in sys.stdin.readlines():
    line = line.strip("\n")
    lines.append(line)

def jämför(lines):

    try:

        i = 0
        j = 1
        
        while j <= len(lines):
        # 2 i taget
            
            första = lines[i]
            andra = lines[j]

            print(första)
            print(andra)

            första_list = list(första)
            andra_list = list(andra)

            sum = ''
            for k in range(len(första)):

                if första_list[k] == andra_list[k]:
                    sum += '.'
                else: 
                    sum += '*'
            print(sum)
            print('\n')

            i += 2
            j += 2

    except IndexError as e:
        pass

jämför(lines)

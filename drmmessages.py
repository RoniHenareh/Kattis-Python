letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def transfer_sentence(ord, n):
	s = ""
	for l in ord:
		s += letters[(letters.index(l)+n)%26]
	return s

def sum_sentence(ord): # effektivt
	return sum([letters.index(l) for l in ord])

def combine_sentences(ord1, ord2):
	s = ""
	for i in range(len(ord1)):
		s += letters[(letters.index(ord1[i])+letters.index(ord2[i]))%26]
	return s

ord = input()
part1, part2 = ord[:len(ord)//2], ord[len(ord)//2:] # // om ojämna tal
part1, part2 = transfer_sentence(part1, sum_sentence(part1)), transfer_sentence(part2, sum_sentence(part2))

print(combine_sentences(part1, part2))
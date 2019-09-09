import sys
import random

global turn
global score

def main():
	on = True
	sys.stdout.write("Welcome to the Latin Vocab Collection!\n")
	option = input("Type 'list' to see the list of our latin words.\n Type 'test' to test yourself on the latin words: \n")
	lang_file = "latin.txt"
	words = open_file(lang_file)
	if option == 'test':
		test(words)
	elif option == 'list':
		list(words)

def open_file(file):
	with open(file, 'r') as f:
		words = f.readlines()
	return words

def list(words):
	for w in words:
		print(w)

def test(words):
	global score
	#words = open_file()
	score = 0
	turn = 0
	sys.stdout.write("Get 10 correct to win!\n")
	while turn < 10:
		#print(turn)
		#print(score)
		test_word = random.choice(words).split(":")
		latin = test_word[0].strip()
		eng = test_word[1].strip()
		indexes = [0,1]
		lang = random.choice(indexes)
		if lang == 0:
			answer = input("{} is translated as? ".format(latin)).strip()
			check(eng, answer, "eng")
		else:
			answer = input("{} is translated as? ".format(eng)).strip()
			check(latin, answer, "latin")
		turn += 1
	if turn >= 10:
		on = False
		sys.stdout.write("Your score is {} out of 10.\n".format(score))
		if score >= 10:
			sys.stdout.write("You win!\n")
		else:
			sys.stdout.write("You lose!\n")
		main()

def check(answer, solution, lang):
	if lang == "latin":
		if validate_latin(answer, solution):
			correct()
		else:
			incorrect()
	elif lang == "eng":
		if validate_english(answer, solution):
			correct()
		else:
			incorrect()

def validate_english(answer, solution):
	"""If question is in latin, check if english solution is correct"""
	answer = answer.split(",")
	answer = [c.strip().replace(".", "") for c in answer]
	print(answer)
	print(solution)
	if len(answer) == 1:
		return evaluate(answer, solution)
	elif len(answer) > 1:
		return solution.strip() in answer

def evaluate(answer, solution):
	if answer[0].strip() == solution.strip():
		return True
	else:
		return False

def validate_latin(answer, solution):
	"""If question is in english, check if latin solution is correct"""
	answer = answer.strip().split()
	answer = [c.strip() for c in answer]
	if len(answer) == 1:
		return evaluate(answer, solution)
	elif len(answer) > 1:
		return solution.strip() in answer

def correct():
	global score
	score += 1
	sys.stdout.write("Correct!\n")

def incorrect():
	sys.stdout.write("Incorrect!\n")

if __name__ == "__main__":
	main()




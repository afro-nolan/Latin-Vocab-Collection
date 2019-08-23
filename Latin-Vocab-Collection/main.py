import sys
import random

global turn
global score

def main():
	on = True
	sys.stdout.write("Welcome to the Latin Vocab Collection!\n")
	option = input("Type 'list' to see the list of our latin words.\n Type 'test' to test yourself on the latin words: \n")
	words = open_file()
	if option == 'test':
		test(words)
	elif option == 'list':
		list(words)

def open_file():
	with open('crawled.txt', 'r') as f:
		words = f.readlines()
	return words

def list(words):
	for w in words:
		trans = w.split()
		print('{} = {}'.format(trans[0], trans[1]))

def test(words):
	global score
	words = open_file()
	score = 0
	turn = 0
	sys.stdout.write("Get 10 correct to win!\n")
	while turn < 10:
		#print(turn)
		#print(score)
		test_word = random.choice(words).split()
		latin = test_word[0]
		eng = test_word[1]
		indexes = [0,1]
		lang = random.choice(indexes)
		if lang == 0:
			answer = input("{} is translated as? ".format(latin))
			check(answer, eng)
		else:
			answer = input("{} is translated as? ".format(eng))
			check(answer, latin)
		turn += 1
	if turn >= 10:
		on = False
		sys.stdout.write("Your score is {} out of 10.\n".format(score))
		if score >= 10:
			sys.stdout.write("You win!\n")
		else:
			sys.stdout.write("You lose!\n")
		main()

def check(answer, lang):
	if validate(answer, lang):
		correct()
	else:
		incorrect()

def validate(answer, solution):
	if answer == solution:
		return True
	else:
		return False

def correct():
	global score
	score += 1
	sys.stdout.write("Correct!\n")

def incorrect():
	sys.stdout.write("Incorrect!\n")

if __name__ == "__main__":
	main()




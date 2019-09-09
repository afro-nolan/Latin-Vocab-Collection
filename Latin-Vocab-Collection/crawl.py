import requests
from general import *
from bs4 import BeautifulSoup
import os

def main():
	#homepage = "https://en.wikipedia.org/wiki/List_of_Latin_words_with_English_derivatives"
	homepage = "https://www.math.ubc.ca/~cass/frivs/latin/latin-dict-full.html"
	crawled_file = 'latin.txt'
	create_file(crawled_file)
	translations = gather_words(homepage)
	write_file(crawled_file, translations)

def create_file(crawled):
	"""Create a file"""
	if not os.path.isfile(crawled):
		write_file(crawled, "")

def write_file(file, data):
	"""Write data to file"""
	with open(file, "w") as f:
		for k in data:
			f.write("{} : {}\n".format(k, data[k]))

def append_to_file(path, data):
	"""Append date to file"""
	with open(path, "a") as f:
		f.write(data + "\n")

def gather_words(page):
	"""Get the words from the webpage and return them in a dictionary"""
	source_code = requests.get(page)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text, 'html.parser')
	latin = soup.find_all("strong")
	english = soup.find_all("em")
	trans = {}
	latin_words = []
	for i in range(len(latin)):
		word = latin[i].text
		word = word.replace(":", "")
		word = word.replace("(", "")
		word = word.replace(")", "").strip()
		if len(word) > 1:
			latin_words.append(word)
	english_words = [english[i].text.strip() for i in range(len(english))]
	for i in range(len(english_words)):
		trans[latin_words[i]] = english_words[i]
	return trans

if __name__ == "__main__":
	main()

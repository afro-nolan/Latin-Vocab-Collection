import requests
from general import *
from bs4 import BeautifulSoup
import os

def main():
	homepage = "https://en.wikipedia.org/wiki/List_of_Latin_words_with_English_derivatives"
	crawled_file = 'latin.txt'
	create_file(crawled_file)
	gather_words(homepage)

def create_file(crawled):
	if not os.path.isfile(crawled):
		write_file(crawled, "")

def write_file(file, data):
	print(file)
	with open(file, "w") as f:
		f.write(data)

def append_to_file(path, data):
    with open(path, "a") as f:
        f.write(data + "\n")

def gather_words(page):
	source_code = requests.get(page)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text, 'html.parser')
	table = soup.find_all('tbody')
	soup1 = table.text
	soup1 = BeautifulSoup(soup1, 'html.parser')
	print(soup1.find_all('a'))

if __name__ == "__main__":
	main()

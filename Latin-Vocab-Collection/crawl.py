import requests
from general import *
from bs4 import BeautifulSoup

def main():
	homepage = "https://en.wikipedia.org/wiki/List_of_Latin_words_with_English_derivatives"
	crawled_file = proj_name + '/crawled.txt'
	create_file(create_file)



def create_file(crawled):
	if not os.path.isfile(crawled):
        write_file(crawled, "")

def write_file(path, data):
    with open(path, "w") as f:
        f.write(data)

def append_to_file(path, data):
    with open(path, "a") as f:
        f.write(data + "\n")

def gather_words():
	pass


import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

num_threads = 8
proj_name = "Latin-Vocab-Collection"
homepage = "https://en.wikipedia.org/wiki/List_of_Latin_words_with_English_derivatives"
domain = get_domain_name(homepage)
queue_file = proj_name + '/queue.txt'
crawled_file = proj_name + '/crawled.txt'

#thread queue
queue = Queue()
Spider(proj_name, homepage, domain)

def create_jobs():
    for link in file_to_set(queue_file):
        queue.put(link)
    queue.join()
    crawl()

#spider threads, stops when main exists
def create_spiders():
    for _ in range(num_threads):
        t = threading.Thread(target=work)
        t.daemon = True   #ensures it dies when main exists
        t.start()

#crawls next job in queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


#crawl items from queue
def crawl():
    queued_links = file_to_set(queue_file)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + " links in the queue.")
        create_jobs()


create_spiders()
crawl()
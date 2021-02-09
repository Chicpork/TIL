from multiprocessing import Process
import os
import psutil
import test2
import giftcard.giftcard_crawler as giftcard_crawler

def f(name):
    print('hello', name)

if __name__ == '__main__':
    gc = giftcard_crawler.GiftcardCrawler()
    p = Process(target=gc.crawling, args=("hi", "36000", "37000"))
    p.start()
    p.join()
# this is kinda broken, imma fix this after the bot database

from gsearch.googlesearch import search

def apisearchg(query,num):
    results = search(searchg, num_results=num)
    return results

def searchg():
    qr = input("Enter search term: ")
    ns = input("Enter max results: ")
    rs = search(qr,num_results = 10)
    print(rs)

searchg()

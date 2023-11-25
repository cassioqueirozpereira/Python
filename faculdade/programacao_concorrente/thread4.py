import threading

import urllib.request as urllib2

import time

# request

start = time.time()

urls = ["https://www.google.com", "https://www.Apple.com", "https://www.Microsoft.com", "https://www.instagram.com"]

def chama_url(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    print("'%s\' carregado em %ss" % (url, (time.time() - start)))
    # print(the_page)

threads = [threading.Thread(target= chama_url, args= (url,)) for url in urls]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("Elapsed Time: %s" % (time.time() - start))
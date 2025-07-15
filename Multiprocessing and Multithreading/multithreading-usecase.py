### Real World scenario of multithreading
# web scraping
# web scraping often involves making numerous requests to fetch web pages
# these tasks are I/O bound and might take up a lot of time, waiting for reponses
# so multithreading can improve performance, by allowing multiple webpages to be fetched concurrently

### we are going to use these three urls
'''https://python.langchain.com/docs/introduction/
   https://python.langchain.com/docs/concepts/
   https://python.langchain.com/docs/tutorials/'''

import threading
import requests
from bs4 import BeautifulSoup


# we will store out 3 urls in the form of a list

urls=[
    "https://python.langchain.com/docs/introduction/",
    "https://python.langchain.com/docs/concepts/",
    "https://python.langchain.com/docs/tutorials/"
]


# now i will create three threads, and at a time, I will say, go and fetch from these urls


# response=requests.get("https://python.langchain.com/docs/tutorials/")  # it just fetches us the response from the webpage
# content=BeautifulSoup(response.content,"html.parser")      # this converts the response into HTML file, you get the HTML code for the page
# print(content.text)                                        # upon adding .txt,you can convert the HTML file, into text contents and you can finally fetch the contents of webpage


def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"html.parser")
    print(f"Fetched {len(soup.text)} characters from {url}")



threads=[] # creating an empty list, where each thread will be stored, no of threads=no of urls


# passing each url from our list as argument 
# then creating a thread for that particular url
# then appending the thread to the threads list, and then starting the thread
for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()


# now  once the threads have been started, we wait for them to finish and join with main thread
for thread in threads:
    thread.join()


# finally ending message
print("Webpages fetched")

# this will be the output

# Fetched 12257 characters from https://python.langchain.com/docs/introduction/  # carried out by thread 1
# Fetched 9846 characters from https://python.langchain.com/docs/tutorials/      # carried out by thread 2   
# Fetched 16308 characters from https://python.langchain.com/docs/concepts/      # carried out by thread 3
# Webpages fetched

# and it is carried out in a matter of seconds, since each thread works on an individual webpage, and we need not wait for it to finish extracting from one and move to another webpage
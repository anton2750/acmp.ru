# import requests
# from bs4 import BeautifulSoup
import threading
from queue import Queue

with open("url.txt") as f:
    lines = f.readlines()
    lines.split()
        url = line
        # google_read = requests.get('http://' + url)
        # soup = BeautifulSoup(google_read.text, "html.parser")

        # a_tags = soup.find_all("a")

        # result_list = []
        # for i in a_tags:
        #     result_list.append(i.get('href'))
        # print(url, 'HAS', len(result_list), 'LINK(S)')

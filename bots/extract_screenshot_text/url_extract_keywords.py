
import urllib.request
import requests
import re
import collections
import datetime
import json
from dotenv import load_dotenv
import os

load_dotenv()
TELEGRAM_BOT_API_KEY = os.getenv('TELEGRAM_BOT_API_KEY')
print(TELEGRAM_BOT_API_KEY)




# function to extract keywords from a given url and a list of keywords , 
# and count the frequency of each word
def extract_keywords(url, keywords):
    # get the html content of the url
    html_content = urllib.request.urlopen(url).read().decode('utf-8')
    # find all the keywords in the html content
    keywords_found = re.findall(r'\w+', html_content)
    # count the frequency of each word
    counter = collections.Counter(keywords_found)
    # create a dictionary of keywords and their frequency
    keywords_frequency = dict()
    keywords_frequency['url'] = url
    keywords_frequency['datetime'] = datetime.datetime.now()
    keywords_frequency['keywords'] = dict()
    for keyword in keywords:
        keywords_frequency['keywords'][keyword] = counter[keyword]
    return keywords_frequency

# function to connect to telegrambot and send the result to the user
def send_to_telegrambot(url, keywords):
    # create a message to send to the user
    message = f"Here are the results for {url} at {keywords['datetime']}\n"
    for keyword in keywords['keywords']:
        message += f"{keyword}: {keywords['keywords'][keyword]}\n"
    # send the message to the user
    requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_API_KEY}/sendMessage?chat_id=123456789&text={message}")
    


url = "https://edition.cnn.com/"
words = extract_keywords(url, ['Trump', 'Biden', 'Israel', 'Gaza'])
print(words)
send_to_telegrambot(url, words)

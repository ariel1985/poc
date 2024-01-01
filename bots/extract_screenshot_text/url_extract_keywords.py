
import urllib.request
import requests
import re
import collections
import datetime
import json



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


url = "https://edition.cnn.com/"
words = extract_keywords(url, ['Trump', 'Biden', 'Israel', 'Gaza'])
print(words)


# function to connect to telegrambot and send the result to the user
def send_to_telegrambot(url, keywords):
    # import the required libraries
    # specify the url of the telegrambot
    url = "https://api.telegram.org/bot<token>/sendMessage"
    # specify the chat_id of the user
    chat_id = "<chat_id>"
    # specify the text to be sent
    text = json.dumps(keywords)
    # specify the parameters
    parameters = {'chat_id': chat_id, 'text': text}
    # send the request
    response = requests.get(url, params=parameters)
    # print the response
    print(response.json())



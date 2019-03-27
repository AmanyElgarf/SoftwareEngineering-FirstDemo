import json
from pprint import  pprint
from datetime import date
from datetime import timedelta
import requests

class Webscraper:
    #CONSTRUCTOR:
    def __init__(self):
        self.url = ''
        self.response = []
        self.headlines = []
    
    #getHeadlines() function
    def getHeadlines(self, ticker):
        #utilizes News API
            #grabs headlines from, and inclusive of, 5 days prior user search
        self.url = ('https://newsapi.org/v2/everything?'
                'q=' + ticker + '&'
                'from=' + str(date.today() + timedelta(days=-5)) + '&'
                'sortBy=popularity&'
                'apiKey=22d271b54d1845858fbddf96cb9d20d2')
        #creates .json file of all the headlines grabbed
        self.response = requests.get(self.url).json()
        for article in self.response["articles"]:
            self.headlines.append(article["title"])
        return self.headlines 
        
        #TESTING:
        
            #with open('googletest.json', 'w') as outfile:
                #json.dump(self.response, outfile)


#print (response.json)

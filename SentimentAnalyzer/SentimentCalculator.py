import nltk
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class SentimentCalculator:
    
    #The constructor has two attributes, newsAnalyzer and financeLexicon.
    def __init__(self):  
        self.newsAnalyzer = SentimentIntensityAnalyzer()
        self.financeLexicon = {}
        with open("FinanceLexicon.txt") as dictFile:
            for line in dictFile:
                line = line.rstrip(',')
                (word, score) = line.split(',')
                self.financeLexicon[word] = int(eval(score))
        self.newsAnalyzer.lexicon.update(self.financeLexicon)
        
    #This function takes a string headline as an input, analyzes it sentiment score, and returns that score
    def calculate(self, message): 
        ss = self.newsAnalyzer.polarity_scores(message)
        return ss["compound"] 

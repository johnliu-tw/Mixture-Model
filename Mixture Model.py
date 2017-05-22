from Parser import Parser
import util
import math
import csv

parser=Parser()

with open('test.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         d1 = row['question1']
         d2 = row['question2']
         d1 = parser.tokenise(d1)
         d1 = parser.removeStopWords(d1)
         d2 = parser.tokenise(d2)
         d2 = parser.removeStopWords(d2)
         d1queryProbability = 1
         d2queryProbability = 1
         rate = 0
         for word in d1:
            wordCountOnd1 = float(d1.count(word))
            wordCountOnd2 = float(d2.count(word))
            wordCountOnBoth = float(d1.count(word)+d2.count(word))
            d1Len = float(len(d1))
            d2Len = float(len(d2))
            d1queryProbability = d1queryProbability*(wordCountOnd1/d1Len+wordCountOnBoth/(d1Len+d2Len))/2
            d2queryProbability = d2queryProbability*(wordCountOnd2/d2Len+wordCountOnBoth/(d1Len+d2Len))/2     
            rate = d2queryProbability/d1queryProbability
         print rate






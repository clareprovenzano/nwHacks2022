

from textblob import TextBlob


words = []

wordData=open('test.csv', encoding = "ISO-8859-1")
for i in wordData:
    words.append(i)

# for i in words:
#    print (i)

# setting the added polarity to 0


# beginning weight of each statement
#weight = 1

# analyse the sentiment of each statement
# 
#sentiments = [b.sentiment for b in [TextBlob(l) for l in words]]

# printing sentiment for each statement & adjusting variables


#for l,s in zip(words, sentiments):
    # p is polarity, s is subjectivity
    # higher subjectivity means more opinionated vs lower subjectivity is more factual
 #   print('{} \n   (p={}, s={})'.format(l, s[0], s[1]), '\n')

  #  #the later statements have more weight to them
   # polarity += s[0]
    # polarity += s[0]*weight
    #weight += .5

# calculate & print average polarity
#avg_polarity = polarity / len(words)
#print('The polarity of this story is '+ str(avg_polarity))

# stating the mood of the story 


# tweets must be in a word list
def runSentimentAnalysis(tweets):
  polarity = 0
  sentiments = [b.sentiment for b in [TextBlob(l) for l in tweets]]
  for l,s in zip(words, sentiments):
    # p is polarity, s is subjectivity
    # higher subjectivity means more opinionated vs lower subjectivity is more factual
    # print('{} \n   (p={}, s={})'.format(l, s[0], s[1]), '\n')
    polarity += s[0]
    avg_polarity = polarity / len(words)
    # print('The polarity of this story is '+ str(avg_polarity))
    # polarity += s[0]*weight
    #weight += .5
  if avg_polarity > .2 : 
    print('Overall, this story is happy :)')
  elif avg_polarity > -.2 and avg_polarity < .2 :
    print('This story is neutral')
  else : 
    print('This is a sad story :(')
  

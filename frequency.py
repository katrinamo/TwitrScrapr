from collections import Counter

def main():

    f = open("MeTooTweets.json", "r")

    #empty strings that will contain the tweet text and the specific 
    #word we are looking at, respectively    
    tweet =""
    word =""
    
    #empty dictionary. It will look like "word" : <number of occurrences>
    allWords = {} 
    
    #only look at the tweet's text and not the other data
#1    for tweet in f:
#1        content = tweet.split()
#1        for word in content:
#1            if word in allWords:
#1                allWords[word] = allWords[word] + 1
#1            else:
#1                allWords[word] = 1
#1
#1    print allWords
#1    print len(allWords)

    wordCounter = Counter()
    for tweet in f:
        content = tweet.split()
        for word in content:
            formatFree = word.lower()
            if formatFree != 'the' and formatFree != 'a' and formatFree !='an' and formatFree !='metoo' and formatFree != 'to' and formatFree != 'of':
                wordCounter[formatFree] +=1

    currWord = ""
    count = 0
    f = open("frequentWords.txt", "w")
    for currWord, count in wordCounter.most_common(1000):
        f.write(currWord +  " ")
        f.write(str(count))
        f.write("\n")
    f.close()

main()

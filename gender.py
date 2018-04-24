import requests
import json
import time

def main():
    term = raw_input("Which file would you like to use? ")
    
    f = open(term + " MeTooTweets.txt", "r")

    line = ""
    name = []
    prevLine =""
    fileLines = []  
  
    outTerm = open(term+"GenderBreakdown.txt", "w")

    for line in f:
        fileLines.append(line)

    #determines which term was used by a tweeter
    used = -9

   #Now we see which sexual violence descriptor is used
    for i in range (8957, len(fileLines)):
        if fileLines[i-2]  == "\n" and fileLines[i-1] == "\n":
            print i
            name = fileLines[i].split()
            r = requests.get("https://api.genderize.io/?name="+name[0]+"&country_id=us", verify = False)
            results = r.json()
    
            if ('gender' in results):    
                if results['gender'] == None:
                    outTerm.write(str(results['gender']) + " " )
                    outTerm.write(str(results) + " ")
                    outTerm.write(str(name))
                    outTerm.write(" CHECK NEEDED**")                    
    
                elif results['probability'] > 0.5 and results['gender'] != None:
                    outTerm.write(results['gender'])
    
                else:    
                    outTerm.write(str(results['gender']) + " " + str(results['probability']))
                    outTerm.write(" " + str(results) + " ")
                    outTerm.write(str(name))
                    outTerm.write(" CHECK NEEDED**")                    
                        

            outTerm.write("\n")
          
    outTerm.close()
    f.close()
        
        

main()

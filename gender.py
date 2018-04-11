import requests
import json

def main():
    f = open("MeTooTweets.txt", "r")
    violenceTerms = ["sexual assault", "sexual abuse", "sexual harassment"]
    vicVsSurv = ["victim", "survivor"]

    line = ""
    name = []
    prevLine =""
    fileLines = []  
  
    outTerm = open("genderBreakdown.txt", "w")
    outVicSurv = open("vicVsSurvGender.txt", "w")

    for line in f:
        fileLines.append(line)

    #determines which term was used by a tweeter
    used = -9

    #Now we see which sexual violence descriptor is used
    for i in range (2, len(fileLines)):
        if fileLines[i-2]  == "\n" and fileLines[i-1] == "\n":
            if violenceTerms[0] in fileLines[i+1]: 
                used = 0
            elif violenceTerms[1] in fileLines[i+1]:
                used = 1
            elif violenceTerms[2] in fileLines[i+1]:
                used = 2
            else:
                used = -9
            
            if used != -9:    
                name = fileLines[i].split()
                r = requests.get("https://api.genderize.io/?name="+name[0]+"&country_id=us", verify = False)
                results = r.json()
                outTerm.write(violenceTerms[used]+" ")

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

    #now we see which is used: victim vs survivor.
    for i in range (2, len(fileLines)):
        if fileLines[i-2]  == "\n" and fileLines[i-1] == "\n":
            if vicVsSurv[0] in fileLines[i+1]: 
                used = 0
            elif vicVsSurv[1] in fileLines[i+1]:
                used = 1
            else:
                used = -9
            
            if used != -9:    
                name = fileLines[i].split()
                r = requests.get("https://api.genderize.io/?name="+name[0]+"&country_id=us", verify = False)
                results = r.json()
                outVicSurv.write(vicVsSurv[used]+" ")

                if results['gender'] == None:
                    outVicSurv.write(str(results['gender']) + " " )
                    outVicSurv.write(str(results) + " ")
                    outVicSurv.write(str(name))
                    outVicSurv.write(" CHECK NEEDED**")                    

                elif results['probability'] > 0.5 and results['gender'] != None:
                    outVicSurv.write(results['gender'])

                else:    
                    outVicSurv.write(str(results['gender']) + " " + str(results['probability']))
                    outVicSurv.write(" " + str(results) + " ")
                    outVicSurv.write(str(name))
                    outVicSurv.write(" CHECK NEEDED**")                    
                
                outVicSurv.write("\n")

    outVicSurv.close()

    f.close()
        
        


main()

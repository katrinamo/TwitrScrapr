import requests
import json
import sys

def main():
    #grab the filename from the command line argument
    filename = sys.argv[-1]
    
    #check to make sure there is a file given before opening
    if (sys.argv[0] != filename):
        f = open(filename, "r")
    else:
        print "ERROR: Requires filename."
        print "USAGE: python gender.py <FILENAME>"
        return 1

    #remove the file extension
    parts = filename.split(".")
    
    #use only the first part to open out file
    outTerm = open(parts[0]+"GenderBreakdown.txt", "w")

    #intialize all the variables needed later
    #not strictly needed but C habits die hard
    line = ""
    name = []
    prevLine =""
    fileLines = []  
  
    

    for line in f:
        fileLines.append(line)

    #Now we see which sexual violence descriptor is used
    for i in range (2, len(fileLines)):
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

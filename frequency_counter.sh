#! /bin/bash
if [ $# -gt 0 ]
then
    echo "Sorting $1."
    cat $1 | tr ' ' '\n'|  tr '[:upper:]' '[:lower:]' > tokenized.txt
    echo "Cleaning $1 of trailing and leading punctuation."
    # delete leading punctuation
    # delete trailing punctuation
    cat tokenized.txt | sed -e ' s/^[[:punct:]]//g; s/[[:punct:]]$//g;'| tr -s '\n' > cleaned.txt
    #sort the stuff
    #sort -nr is a numeric sort that reverses the results (most to least)
    cat cleaned.txt | sort | uniq -c | sort -nr > sorted.txt

    #delete intermediary files
    if [ $# -eq 1 ]
    then
        rm cleaned.txt tokenized.txt        
    #if specified, keep all intermediary files
    elif [ $# -eq 2 ]
    then
        if [ $2 == '--expanded' ]
        then
            echo "Keeping all intermediary files."
        else
            echo "Unrecognized argument. Recognized argument:"
            echo "      --expanded"
            echo 
            echo "      Keeps all intermediary files for debugging."
        fi
        
    fi
else
    echo "NOT ENOUGH ARGUMENTS. NEEDS A FILENAME"
    echo "Usage: ./frequency_counter [FILENAME] [options]"
fi

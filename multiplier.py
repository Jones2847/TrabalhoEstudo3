# multiplier.py
import sys

def multiplier(pList:list):
    result = 1
    for n in pList:
        result*=float(n)
    # for
    return result
# def multiplier

if __name__=="__main__": # was I called from the CLI?
    if(len(sys.argv)>1): # check if there are args
        the_values:list = sys.argv[1:] # except the script name
        the_mult = multiplier(the_values)
        the_output =\
        f"The mult of {the_values} is {the_mult}"
        print(the_output)
    # if
    else:
        the_output = "Please provide some numbers."
        print(the_output)
    # if-else
else: # for example, it was an import
    pass
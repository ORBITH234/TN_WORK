#question
# #create a function that takes in a slice and maps the individual element of that slice to a dictionary starting from key 1
## to the last element of that slice 

["the", "man", "is", 12, "years", "old"]
# this should be the answer 
{1 : "the", 2 : "man", 3 : "is", 4 : 12, 5: "years", 6 : "old"}

def Tap(grow):
    if not grow:
        return "nothing is given"
    
    result = {}
    key = 1

    for item in grow:
        result[key] = item 
        key += 1            
    
    return result

print(Tap(["the", "man", "is", 12, "years", "old"]))
# remove word from the list

def remov(l,word):
    for i in l:
        l.remove(word)
        return l
    

l = ["Afaque", "Nishu","Unwanted"]
print(remov(l,"Unwanted"))
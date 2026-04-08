def match_words(words):
    ctr=0
    emptyList=[]
    for i in words:
        if len(i)>1 and i[0]==i[-1]:
            ctr+=1
            emptyList.append(i)
    print("List of words with first and last character same",emptyList)
    return ctr

count=match_words(["aba","xyz","cdc","jln","mnm"])
print("Number of words ",count)
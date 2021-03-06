def JaccardDistance(str1,str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    coff = float((2*(len(set1 & set2)))/(len(set1)+len(set2)))
    distance = 1-coff
    return round(distance,2)

base = ("jason java php ajax ruby")
Set1 = ("java php ajax ruby html")
Set2 = ("java php ajax python R")
Set3 = ("html Python java php html") 
Set4 = ("jason java php ajax ruby R php tableau SQL")
Set5 = ("ruby jason php R python tableau jquery")

ans1 = JaccardDistance(Set1,Set3)
ans2 = JaccardDistance(base,Set2)
ans3 = JaccardDistance(base,Set3)
ans4 = JaccardDistance(base,Set4)
ans5 = JaccardDistance(base,Set5)

print('The distance Between base and Set1 is', ans1)
print('The distance Between base and Set2 is', ans2)
print('The distance Between base and Set3 is', ans3)
print('The distance Between base and Set4 is', ans4)
print('The distance Between base and Set5 is', ans5)

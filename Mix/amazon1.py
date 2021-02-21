numreview=5
repository=['code','codePhone','coddle','coddles','codes']
CustomerQuery='coddle'

#Contraints
    # Add max 3 keywords
    # Case insensitive

#Create print list
#iterate through word from 1 to len(word)
#get subquery
#Iterate over repository and check

output=[]
sorted_repository=sorted([word.lower() for word in repository])
CustomerQuery.lower()
for i in range(1,len(CustomerQuery)):
    listOfList=[]
    for r in sorted_repository:
        if len(listOfList)==3:
            break
        else:
            if CustomerQuery[:i+1]==r[:i+1]:
                listOfList.append(r)
    output.append(listOfList)

print(output)

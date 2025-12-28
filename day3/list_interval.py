moker = [10,20,56,77,100,109]
index = 0
number_to_insert = 99
for number in moker:
    if number > number_to_insert:
        break
    else:
        index+=1
    
number_to_insert = 99
moker.append(None)

for i in range(len(moker)-1,index,-1):
    moker[i] = moker[i-1]

moker[index]= number_to_insert
print(moker)
print(index)




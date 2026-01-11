strings1 = "789"
strings2 = "654"
def add_two_strigs(string1,string2):
    result = [0]*(len(string1)+len(string2))
    string1,string2 = string1[::-1],string2[::-1]
    for i1 in range (len(string1)):
        for i2 in range (len(string2)):
            digit = int(string1[i1])*int(string2[i2])
            result[i1+i2] += digit
            carry = result[i1+i2] // 10
            result[i1+i2] %= 10
            result[i1+i2+1]+=carry
    result = result[::-1]
    beg = 0
    while beg<len(result) and result[beg] == 0:
        beg+=1
    
    return"".join(map(str,result[beg:]))

        
print(type(add_two_strigs(strings1,strings2)))



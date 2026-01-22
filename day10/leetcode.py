def longestCommonPrefix() -> str:      
        data = ["restructure", "rest", "restart", "restaurant"]

        data =data.sort()

        first = data[0]
        last = data[-1]
        i = 0
        while i<len(data) and first[i] == last[i]:
            i+=1
        return first[:i]

print(longestCommonPrefix())




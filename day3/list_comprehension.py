# maker= []
# for i in range(1,11):
#     if i%2==0:

#         maker.append(i)
# print(maker)

# maker = [i if i%2==0 else None for i in range (1,11) ]
# print(maker) 

labour = {"mahesh":500,"ramesh":400,"mithilesh":400,"sumesh":300,"jagmohan":1000,"rampyare":800}
total = 0
days = 50

for cost in labour:
    total +=labour[cost]

total = (total*days)-((7*labour["mahesh"])+(4*labour["jagmohan"]))
print(total)
list=[1,2,3,3,3,4,5,6,6,7,8]

result = []
for item in list:
    if item not in result:
        result.append(item)
print(result)
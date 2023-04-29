list=[3,3,3,3,3,3]

result = []
for item in list:
    if item not in result:
        result.append(item)
print(result)
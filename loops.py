# list
scores=[90,65,34,71,55,77,89]

#access a value
print(scores[0]) #first
print(scores[2]) #third

# add
scores.append(71)
print(scores)

#remove
scores.pop(4)
print(scores)

scores.sort(reverse=True)
print(len(scores))
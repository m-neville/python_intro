# data structures
# collection
# list, dictionary, set
scores = [78, 43, 67, 89, 45, 76, 99, 90, 56, 43, 65, 55, 61, 23, 54, 89, 90, 49, 69]

# access a score
print(scores[0])

# add a score
scores.append(51)
print(scores)

# remove
scores.remove(43)
print(scores)

print(len(scores))

print(scores.count(45))

scores.sort() # asce. manner
print(scores)

scores.sort(reverse=True) # desc. manner
print(scores)

# slice a list
top_5 = scores[-5:] # cutting the list, # the last position is not included
print(top_5)

# dictionary

person = {'name':'Moses', 'age':19, 'weight':58, 'county':'Nairobi'}
print(person['name'])
print(person['age'])

# set - only one occurence
days = {'mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun', 'mon'}
print(days)

for s in scores:
    if s < 50:
        pass
    print(s)

for d in days: #for each day in days
    print(d)
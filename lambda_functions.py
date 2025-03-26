import math
# lambda_functions
def add_two_numbers(a, b):
    return a + b


print(add_two_numbers(5, 10))

add_two = lambda a, b: a + b

print(add_two(46, 5))

scores = [{"eng": 56, "mat": 60},
          {"eng": 71, "mat": 68},
          {"eng": 37, "mat": 49},
          {"eng": 71, "mat": 63}]

sorted_by_maths = sorted(scores, key=lambda s: s['mat'])

print(sorted_by_maths)

def get_eng_score(score):
    return score["eng"]


sorted_by_eng = sorted(scores, key=get_eng_score)

print(sorted_by_eng)

ages = [55, 32, 32, 45, 67, 68, 78, 96, 54, 41, 12, 21, 18, 43, 56, 65, 78, 90, 54, 6, 43, 13, 12, 11, 19, 20,]

# total_age = reduce(lambda x,y: x+y, ages, 0)
#
# print(total_age)

new_ages = map(lambda x: x+1, ages)

print(list(new_ages))

above_60 = filter(lambda age: age > 60, ages)

print(list(above_60))


def add(*numbers):
    print(type(numbers)) # tuple
    return sum(numbers)
    
print(add(1,2,3))

# def add(*numbers):
#    result = 0
#    for n in numbers:
#       result += n
#    return result


def movie(**kwargs):
    print(type(kwargs)) # dict

print(movie(name='더 글로리', writer= '김은숙'))
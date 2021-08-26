import random

def a_list(size, of=-10, to=10):
    return[random.randint(of, to) for _ in range(size)]

a = a_list(8)

count = len(list(filter(lambda el: el <=10, a)))
sum1 = sum(el for el in a if el > 0)
sum2 = (sum(el for el in a if el%2 == 0)/len(list(el for el in a if el%2==0)))
print(a)
print(count)
print(sum1)

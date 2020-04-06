
my_list = ['a', 'b', 'c', 'd']

def my_function(test):
    Counter = 0
    for i in test:
        Counter = Counter + 1
        print(Counter, '...', i)

my_function(my_list)
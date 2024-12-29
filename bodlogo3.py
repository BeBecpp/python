import random
x = int(input(""))
my_arr= []
for i in range(x):
    rand = random.randint(1,100)
    my_arr.append(rand)
for item in my_arr:
    print(item)

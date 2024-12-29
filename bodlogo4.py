import random


rows = int(input("Мөрүүдийн тоо: "))
cols = int(input("Эгнээний тоо: "))


matrix = []


for i in range(rows):
    row = [random.randint(0, 100) for _ in range(cols)]  # 0-100 хоорондын санамсаргүй тоо
    matrix.append(row)

for row in matrix:
    print(matrix)    
max_value = max(max(row) for row in matrix)

print( max_value)

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(matrix)

#Number of rows
print(len(matrix))

#Number of columns
print(len(matrix[0]))

print(matrix[0][1])

print(matrix[2][2])

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        print(matrix[i][j],end=" ")
    print("\n")

rows = int(input("Please enter the number of rows -- "))
columns = int(input("Please enter the number of columns -- "))

matrix = []

for i in range(rows):
    temp = []
    for j in range(columns):
        x = int(input("Please enter your number -- "))
        temp.append(x)
    matrix.append(temp)

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        print(matrix[i][j],end=" ")
    print("\n")
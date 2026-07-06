stuDetails=('Surabhi', 89)
print(stuDetails)

address=('111', 'Hazerswoudestraat', 'Zoetermeer', 'Zuid-Holland', '2729 CL')

for x in address:
    print (x, end = ' ')

houseno, street, city, province, postalcode = address

print()
print(houseno)
print(street)
print(city)
print(province)
print(postalcode)


my_tuple = 3, 4.6, "dog"
print(my_tuple)

n_tuple = ("Mouse", [1, 2, 3], (4, 5, 6))

print(n_tuple[0][3])
print(n_tuple[1][1])
print(n_tuple[2][2])

my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

print(my_tuple[1:4])

print(my_tuple[:-7])

print(my_tuple[7:])

print(my_tuple[:])

my_tuple = (4, 2, 3, [6, 5])

my_tuple[3][0] = 4
print(my_tuple)
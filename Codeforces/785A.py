n=int(input())
Tetrahedron =4
Cube = 6
Octahedron =8
Dodecahedron = 12
Icosahedron = 20
count=0
for i in range(n):
    shape=input()
    if shape == "Tetrahedron":
        count+=4
    elif shape == "Cube":
        count+=6
    elif shape == "Octahedron":
        count+=8
    elif shape == "Dodecahedron":
        count+=12
    elif shape == "Icosahedron":
        count+=20

print(count)
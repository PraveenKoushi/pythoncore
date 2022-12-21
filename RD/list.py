print("Printing Triangle ")
picture = [[0, 0, 0, 1, 0, 0, 0],
           [0, 0, 1, 1, 1, 0, 0],
           [0, 1, 1, 1, 1, 1, 0],
           [1, 1, 1, 1, 1, 1, 1],
           [0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0]
           ]

print(picture)

fill = '$'
empty = ' '
for row in picture:
    for pixel in row:
        if pixel == 1:
            print(fill, end="")
        else:
            print(empty, end="")

    print("")  # Need a line after every row

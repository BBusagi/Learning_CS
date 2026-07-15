#22 2D List & Nested Loops

number_grid = [
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0])
print(number_grid[2][1])

for row in number_grid:
    print(row)

for row in number_grid:
    for col in row:
        print(col)

#扩展
number_grid2 = [
    [1, 2, 3], 
    [4, 5, 6, 7],
    [8, 9, 10, 11, 12, 13],
    [0]
]

print(number_grid2[2][3])
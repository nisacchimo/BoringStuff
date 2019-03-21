#print(len(grid[0]))
#for y in range(len(grid[0]):
#    for x in range(len(grid)):
#        print(grid[x][y],end = "")
#    print("")


def print_grid(grid):
    width = len(grid)
    height = len(grid[0])
    for y in range(height):
        for x in range(width):
            print(grid[x][y],end='')
        print()

grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]


print_grid(grid)

import sys
import time
import csv
import numpy as np

SNAKE_SIZE = 7

def generate_random_grid():
    size = np.random.randint(10, 101)
    grid = np.zeros((size,size), np.int32)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            grid[i,j] = np.random.randint(1, 257)
    t1 = time.time()
    return grid

def load_grid():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        if len(sys.argv) > 2:
            delimiter = sys.argv[2]
        else:
            delimiter = ';'
        reader = csv.reader(open(input_file, "r"), delimiter=delimiter)
        l = list(reader)
        return np.array(l).astype("int")
    else:
        return generate_random_grid()

def get_shapes(shape, shapes, n):
    if len(shape)==7:
        minx = min(shape, key=lambda x: x[0])[0]
        if minx<0:
            shape = [(x-minx, y) for x, y in shape]
        miny = min(shape, key=lambda x: x[1])[1]
        if miny<0:
            shape = [(x, y-miny) for x, y in shape]
        shape.sort()
        if shape not in shapes:
            shapes.append(shape)
    else:
        x, y = shape[-1]
        if     (x+1, y)   not in shape \
           and (x+2, y)   not in shape \
           and (x+1, y+1) not in shape \
           and (x+1, y-1) not in shape:
            new_shape = shape + [(x+1, y)]
            shapes = get_shapes(new_shape, shapes, n) 
        if     (x,   y+1) not in shape \
           and (x,   y+2) not in shape \
           and (x+1, y+1) not in shape \
           and (x-1, y+1) not in shape:
            new_shape = shape + [(x, y+1)]
            shapes = get_shapes(new_shape, shapes, n)
        if     (x-1, y)   not in shape \
           and (x-2, y)   not in shape \
           and (x-1, y+1) not in shape \
           and (x-1, y-1) not in shape:
            new_shape = shape + [(x-1, y)]
            shapes = get_shapes(new_shape, shapes, n)
        if     (x,   y-1) not in shape \
           and (x,   y-2) not in shape \
           and (x+1, y-1) not in shape \
           and (x-1, y-1) not in shape:
            new_shape = shape + [(x, y-1)]
            shapes = get_shapes(new_shape, shapes, n)
    return shapes

def share_cells(a, b):
    for cell in a:
        if cell in b:
            return True
    return False

def get_matching_snake(snakes, new_snake, value):
    if value not in snakes.keys():
        snakes[value] = [new_snake]
        return None
    else:
        for snake in snakes[value]:
            if not share_cells(snake, new_snake):
                return snake
        snakes[value].append(new_snake)
    return None

def search_snakes(grid, snakes, shapes):
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            for shape in shapes:
                value = 0
                snake = [(x+i, y+j) for x, y, in shape]
                for x, y in snake:
                    if x<grid.shape[0] and  y<grid.shape[1]:
                        value += grid[x, y]
                    else:
                        value = 0
                        break
                if value > 0:
                    match = get_matching_snake(snakes, snake, value)
                    if match != None:
                        return match, snake, value
    return 'Fail'



shapes = []
shape = [(0, 0)]
shapes = get_shapes(shape, shapes, SNAKE_SIZE)
snakes = dict()
grid = load_grid()

print(search_snakes(grid, snakes, shapes))
t1 = time.time()
#print(t1-t0)
 
#print(get_shapes(shape, shapes, n))

print(grid)
#print(grid[0,1])










grid = []
x = int(input('Grid size: '))
for i in range(x):
  row = []
  for j in range(x):
    row.append('.')
  grid.append(row)
grid[0][0]='x'
def griddle():
    for line in grid:
        print(' '.join(line))
griddle()
h = 0
v = 0
m = input("Direction: ")
while m != "":
  if m.lower() == "right":
    h = h+1
    grid[v][h] = 'x'
    griddle()
    m = input("Direction: ")
  elif m.lower() == "left":
    h = h-1
    grid[v][h]= 'x'
    griddle()
    m = input("Direction: ")
  elif m.lower() == "up":
    v = v-1
    grid[v][h]= 'x'
    griddle()
    m = input("Direction: ")
  elif m.lower() == "down":
    v = v+1
    grid[v][h]= 'x'
    griddle()
    m = input("Direction: ")
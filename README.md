# Hexway

An implementation of conway's game of life on a hexagonal grid. 

## Table of Contents

- [Rules](#rules)
- [Support](#support)
- [Contributing](#contributing)


## Rules

The rules for this version of the game of life are as follows:
- Any live cell with fewer than two live neighbors dies, as if by underpopulation.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies, as if by overpopulation.
- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
- Every dead cell resurrects after 6 generations irrespective of the number of live neighbors. [TODO]
- All the resurrected cells can not die by the way in which they previously died.
- Every 4 generations a random dead cell comes to life irrespective of the number of live neighbors. [TODO]

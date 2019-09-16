from src.map import Map, Cell, Terrain


dungeon = Map()

for x in range(20):
    for y in range(20):
        cell = Cell(dungeon, Terrain.DUNGEON, (x, y))
        dungeon.add_cell(cell)

for cell in dungeon.all_cells():
    cell.link_to_adj()

c = dungeon.get_cell((0, 0))
print([x.coord.coord for x in c.links])


def make_matrix(n):
	return [[0] * n for _ in range(n)]
def projections(n, cell):
    result = {key:make_matrix(n) for key in ['xy','xz','yz'] }

    for c in cell:
        x, y, z = cell
        result['xy'][y][x] = 1
        result['xz'][z][x] = 1
        result['yz'][z][y] = 1
    return result

print(projections(4,[0,0,0]))

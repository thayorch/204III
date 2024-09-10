def life_path(n: int) -> int:
    if len(str(n)) == 1:
        return n
    return life_path(sum(map(int, str(n))))

if __name__ == '__main__':
    assert life_path(13092004) == 1
    assert life_path(7) == 7
def moltiplicazione(n: int, m: int) -> int:
    p = 0
    for i in range(m):
        p += n
    return p


if __name__ == '__main__':
    print(moltiplicazione(5, 7))
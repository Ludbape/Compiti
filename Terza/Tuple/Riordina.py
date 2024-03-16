def riordina(a):
    a = list(a)
    a.sort()
    return tuple(a)


if __name__ == '__main__':
    t1 = ('mela', 'pera', 'banana', 'ananas', 'kiwi', 'arancia')
    print(riordina(t1))
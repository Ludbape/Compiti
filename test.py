def pal(s: str):
    if len(s) == 1 or len(s) == 0:
        return True
    else:
        if s[0] != s[-1]:
            return False
        else:
            return pal(s[1:-1])


if __name__ == '__main__':
    print(pal("non"))
